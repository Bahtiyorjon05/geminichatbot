

import torch
import time



#print(torch.__version__)

# x = torch.tensor([1.0, 2.0, 3.0])
# print(x)

# # Tensor with random values
# random_tensor = torch.rand(3,3)
# print("Random Tensor:\n", random_tensor)


# # Tensor with all zeros
# zeros_tensor = torch.zeros(2,2)
# print("\nZeros Tensor:\n", zeros_tensor)


# # Tensor with all ones
# ones_tensor = torch.ones(2,2)
# print("\nOnes Tensor:\n", ones_tensor)


# Tensor with specific values
#custom_tensor = torch.tensor([[5,10], [15,20]])
#print("\nCustom Tensor:\n", custom_tensor)




# print("\nShape of custom_tensor:", custom_tensor.shape)
# print("Data type of custom_tensor:", custom_tensor.dtype)



# a = torch.tensor([2,4,6])
# b = torch.tensor([1,2,3])

# # Addition
# print("\nAddition:", a + b)

# # Subtraction
# print("Subtraction:", a - b)

# # Multiplication
# print("Multiplication:", a * b)

# # Division
# print("Division:", a / b)


#tensor_example = torch.tensor([[10,20,30], [40,50,60]])


# # Access a single element (row 0, column 1)
# print("Element at [0,1]:", tensor_example[0, 1])

# # Access a full row
# print("Row 1:", tensor_example[1])  

# # Access a full column
# print("Column 2:", tensor_example[:, 2])



# # Slicing rows and columns
# print("First two rows:\n", tensor_example[:2])  # First two rows
# print("First two columns:\n", tensor_example[:, :2])  # First two columns
# print("Last row:\n", tensor_example[-1])  # Last row


# tensor_example[0, 1] = 99  # Change a single element
# print("Modified Tensor:\n", tensor_example)

# tensor_example[:, 2] = torch.tensor([100, 200])  # Change a full column
# print("\nAfter Changing Column 2:\n", tensor_example)



# x = torch.arange(6)
# x = x.view(3,2)
# print("X", x)


# W = torch.arange(10).view(2,5) # We can also stack multiple operations in a single line
# print("W", W)

# h = torch.matmul(x, W) # Verify the result by calculating it by hand too!
# print("h", h)



###########################################################33


#    INDEXING


# x = torch.arange(12).view(3, 4)
# print("X", x)

# print(x[2,1:3])


############################################3

#    Dynamic computations


# x = torch.ones((3,))

# a = x + 2
# b = a ** 2
# c = b + 3
# y = c.mean()
# # print("Y", y)

# y.backward()

# print(x.grad)


##########################################################


#   GPU   Vs   CPU

#device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
# print("Device", device)


# x = torch.zeros(2, 3)
# x = x.to(device)
# print("X", x)



# x = torch.randn(5000, 5000)

# ## CPU version
# start_time = time.time()
# _ = torch.matmul(x, x)
# end_time = time.time()
# print(f"CPU time: {(end_time - start_time):6.5f}s")

# ## GPU version
# x = x.to(device)
# _ = torch.matmul(x, x)  # First operation to 'burn in' GPU
# # CUDA is asynchronous, so we need to use different timing functions
# start = torch.cuda.Event(enable_timing=True)
# end = torch.cuda.Event(enable_timing=True)
# start.record()
# _ = torch.matmul(x, x)
# end.record()
# torch.cuda.synchronize()  # Waits for everything to finish running on the GPU
# print(f"GPU time: {0.001 * start.elapsed_time(end):6.5f}s")  # Milliseconds to seconds



###########################################3

#   Learning by example: Continuous XOR


# Simple classifier



# import torch
# import torchvision
# import torchvision.transforms as transforms
# import matplotlib.pyplot as plt
# import numpy as np
# import torch.nn as nn
# import torch.utils.data as data


# class SimpleClassifier(nn.Module):

#     def __init__(self, num_inputs, num_hidden, num_outputs):
#         super().__init__()
#         # Initialize the modules we need to build the network
#         self.linear1 = nn.Linear(num_inputs, num_hidden)
#         self.act_fn = nn.Tanh()
#         self.linear2 = nn.Linear(num_hidden, num_outputs)

#     def forward(self, x):
#         # Perform the calculation of the model to determine the prediction
#         x = self.linear1(x)
#         x = self.act_fn(x)
#         x = self.linear2(x)
#         return x


# model = SimpleClassifier(num_inputs=2, num_hidden=4, num_outputs=1)
# # # Printing a module shows all its submodules
# # print(model)


# # for name, param in model.named_parameters():
# #     print(f"Parameter {name}, shape {param.shape}")


class XORDataset(data.Dataset):

	def __init__(self, size, std=0.1):
		"""
		Inputs:
			size - Number of data points we want to generate
			std - Standard deviation of the noise (see generate_continuous_xor function)
		"""
		super().__init__()
		self.size = size
		self.std = std
		self.generate_continuous_xor()

	def generate_continuous_xor(self):
		# Each data point in the XOR dataset has two variables, x and y, that can be either 0 or 1
		# The label is their XOR combination, i.e. 1 if only x or only y is 1 while the other is 0.
		# If x=y, the label is 0.
		data = torch.randint(low=0, high=2, size=(self.size, 2), dtype=torch.float32)
		label = (data.sum(dim=1) == 1).to(torch.long)
		# To make it slightly more challenging, we add a bit of gaussian noise to the data points.
		data += self.std * torch.randn(data.shape)

		self.data = data
		self.label = label

	def __len__(self):
		# Number of data point we have. Alternatively self.data.shape[0], or self.label.shape[0]
		return self.size

	def __getitem__(self, idx):
		# Return the idx-th data point of the dataset
		# If we have multiple things to return (data point and label), we can return them as tuple
		data_point = self.data[idx]
		data_label = self.label[idx]
		return data_point, data_label


dataset = XORDataset(size=200)
# print("Size of dataset:", len(dataset))
# print("Data point 0:", dataset[0])

# def visualize_samples(data, label):
#     if isinstance(data, torch.Tensor):
#         data = data.cpu().numpy()
#     if isinstance(label, torch.Tensor):
#         label = label.cpu().numpy()
#     data_0 = data[label == 0]
#     data_1 = data[label == 1]

#     plt.figure(figsize=(4,4))
#     plt.scatter(data_0[:,0], data_0[:,1], edgecolor="#333", label="Class 0")
#     plt.scatter(data_1[:,0], data_1[:,1], edgecolor="#333", label="Class 1")
#     plt.title("Dataset samples")
#     plt.ylabel(r"$x_2$")
#     plt.xlabel(r"$x_1$")
#     plt.legend()


# visualize_samples(dataset.data, dataset.label)
# plt.show()


##################################################33


# data loader class

import torch
from torch.utils.data import Dataset, DataLoader
import torch.utils.data as data
data_loader = data.DataLoader(dataset, batch_size=16, shuffle=True)

data_inputs, data_labels = next(iter(data_loader))

# The shape of the outputs are [batch_size, d_1,...,d_N] where d_1,...,d_N are the
# dimensions of the data point returned from the dataset class
print("Data inputs", data_inputs.shape, "\n", data_inputs)
print("Data labels", data_labels.shape, "\n", data_labels)