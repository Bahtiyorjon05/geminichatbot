
#   Factorial of a number

# def factorial(num):
#     result = 1
#     while num > 1:
#         result *= num  
#         num -= 1   
#     return result
# print(factorial(5))


#  Total price dict


# import matplotlib.pyplot as plt

# # Your provided shop_sales data
# shop_sales = {
#     "January": {"Suit": {"sold": 10, "price": 100}, "Jacket": {"sold": 25, "price": 150}, "Cap": {"sold": 200, "price": 20}},
#     "February": {"Suit": {"sold": 15, "price": 100}, "Jacket": {"sold": 20, "price": 150}, "Cap": {"sold": 180, "price": 20}},
#     "March": {"Suit": {"sold": 18, "price": 100}, "Jacket": {"sold": 30, "price": 150}, "Cap": {"sold": 210, "price": 20}},
#     "April": {"Suit": {"sold": 22, "price": 100}, "Jacket": {"sold": 28, "price": 150}, "Cap": {"sold": 250, "price": 20}},
#     "May": {"Suit": {"sold": 20, "price": 100}, "Jacket": {"sold": 35, "price": 150}, "Cap": {"sold": 230, "price": 20}},
#     "June": {"Suit": {"sold": 25, "price": 100}, "Jacket": {"sold": 40, "price": 150}, "Cap": {"sold": 240, "price": 20}},
#     "July": {"Suit": {"sold": 30, "price": 100}, "Jacket": {"sold": 45, "price": 150}, "Cap": {"sold": 250, "price": 20}},
#     "August": {"Suit": {"sold": 28, "price": 100}, "Jacket": {"sold": 38, "price": 150}, "Cap": {"sold": 220, "price": 20}},
#     "September": {"Suit": {"sold": 32, "price": 100}, "Jacket": {"sold": 42, "price": 150}, "Cap": {"sold": 260, "price": 20}},
#     "October": {"Suit": {"sold": 35, "price": 100}, "Jacket": {"sold": 50, "price": 150}, "Cap": {"sold": 270, "price": 20}},
#     "November": {"Suit": {"sold": 38, "price": 100}, "Jacket": {"sold": 55, "price": 150}, "Cap": {"sold": 280, "price": 20}},
#     "December": {"Suit": {"sold": 12, "price": 100}, "Jacket": {"sold": 30, "price": 150}, "Cap": {"sold": 220, "price": 20}},
# }

# # Calculate total revenue per item
# total_revenue = {"Suit": 0, "Jacket": 0, "Cap": 0}
# for month, items in shop_sales.items():
#     for item, data in items.items():
#         total_revenue[item] += data["sold"] * data["price"]

# # Calculate average monthly revenue per item
# total_months = len(shop_sales)
# avg_revenue = {item: total_revenue[item] / total_months for item in total_revenue}

# # Calculate revenue trends per item (monthly breakdown)
# monthly_revenue = {"Suit": [], "Jacket": [], "Cap": []}
# for month, items in shop_sales.items():
#     for item, data in items.items():
#         monthly_revenue[item].append(data["sold"] * data["price"])

# # Calculate revenue share (percentage of total revenue)
# total_all_revenue = sum(total_revenue.values())
# revenue_share = {item: (total_revenue[item] / total_all_revenue) * 100 for item in total_revenue}

# # Plotting the graphs

# # 1. Bar chart for Total Revenue per item
# plt.figure(figsize=(10, 6))
# plt.bar(total_revenue.keys(), total_revenue.values(), color=['blue', 'green', 'orange'])
# plt.title("Total Revenue per Item")
# plt.ylabel("Revenue ($)")
# plt.show()

# # 2. Bar chart for Average Monthly Revenue per item
# plt.figure(figsize=(10, 6))
# plt.bar(avg_revenue.keys(), avg_revenue.values(), color=['blue', 'green', 'orange'])
# plt.title("Average Monthly Revenue per Item")
# plt.ylabel("Average Revenue ($)")
# plt.show()

# # 3. Line chart for Revenue Trend per item (Monthly Breakdown)
# plt.figure(figsize=(10, 6))
# for item, revenues in monthly_revenue.items():
#     plt.plot(shop_sales.keys(), revenues, label=item)
# plt.title("Revenue Trend per Item")
# plt.ylabel("Revenue ($)")
# plt.xlabel("Month")
# plt.legend()
# plt.xticks(rotation=45)
# plt.show()

# # 4. Pie chart for Revenue Share per Item
# plt.figure(figsize=(8, 8))
# plt.pie(revenue_share.values(), labels=revenue_share.keys(), autopct='%1.1f%%', startangle=90, colors=['blue', 'green', 'orange'])
# plt.title("Revenue Share per Item")
# plt.show()


################################################################

# shop_sales = {
#     "January": {
#         "Suit": {"sold": 10, "price": 100},
#         "Jacket": {"sold": 25, "price": 150},
#         "Cap": {"sold": 200, "price": 20}
#     },
#     "February": {
#         "Suit": {"sold": 15, "price": 100},
#         "Jacket": {"sold": 20, "price": 150},
#         "Cap": {"sold": 180, "price": 20}
#     },
#     "March": {
#         "Suit": {"sold": 18, "price": 100},
#         "Jacket": {"sold": 30, "price": 150},
#         "Cap": {"sold": 210, "price": 20}
#     },
#     "April": {
#         "Suit": {"sold": 22, "price": 100},
#         "Jacket": {"sold": 28, "price": 150},
#         "Cap": {"sold": 250, "price": 20}
#     },
#     "May": {
#         "Suit": {"sold": 20, "price": 100},
#         "Jacket": {"sold": 35, "price": 150},
#         "Cap": {"sold": 230, "price": 20}
#     },
#     "June": {
#         "Suit": {"sold": 25, "price": 100},
#         "Jacket": {"sold": 40, "price": 150},
#         "Cap": {"sold": 240, "price": 20}
#     },
#     "July": {
#         "Suit": {"sold": 30, "price": 100},
#         "Jacket": {"sold": 45, "price": 150},
#         "Cap": {"sold": 250, "price": 20}
#     },
#     "August": {
#         "Suit": {"sold": 28, "price": 100},
#         "Jacket": {"sold": 38, "price": 150},
#         "Cap": {"sold": 220, "price": 20}
#     },
#     "September": {
#         "Suit": {"sold": 32, "price": 100},
#         "Jacket": {"sold": 42, "price": 150},
#         "Cap": {"sold": 260, "price": 20}
#     },
#     "October": {
#         "Suit": {"sold": 35, "price": 100},
#         "Jacket": {"sold": 50, "price": 150},
#         "Cap": {"sold": 270, "price": 20}
#     },
#     "November": {
#         "Suit": {"sold": 38, "price": 100},
#         "Jacket": {"sold": 55, "price": 150},
#         "Cap": {"sold": 280, "price": 20}
#     },
#     "December": {
#         "Suit": {"sold": 12, "price": 100},
#         "Jacket": {"sold": 30, "price": 150},
#         "Cap": {"sold": 220, "price": 20}
#     }
# }
# prices = {"Suit": 150, "Jacket": 100, "Cap": 20}
# total_revenue = {"Suit": 0, "Jacket": 0, "Cap": 0}

# for month, items in shop_sales.items():
#     for item, data in items.items():
#         total_revenue[item] += data["sold"] * data["price"]

# for item, revenue in total_revenue.items():
#     print(f"The total revenue for {item.lower()} is {revenue} $")

# july_sales = shop_sales["July"]
# max_revenue = 0
# max_item = ""

# for item, data in july_sales.items():
#     revenue = data["price"] * data["sold"]
#     if revenue > max_revenue:
#         max_revenue = revenue
#         max_item = item

# print(f"The max revenue for July sales is from {max_item} with {max_revenue} $")

# spring_months = ["March", "April", "May"]
# spring_revenue = {"Suit": 0, "Jacket": 0, "Cap": 0}

# for month in spring_months:
#     for item, data in shop_sales[month].items():
#         spring_revenue[item] += data["price"] * data["sold"]
# for item, revenue in spring_revenue.items():
#     print(f"The total revenue for {item} in spring is {revenue} $")


# most_profitable_item = max(total_revenue, key=total_revenue.get)
# least_profitable_item = min(total_revenue, key=total_revenue.get)

# print(f"The most profitable item is {most_profitable_item} with {total_revenue[most_profitable_item]} $")
# print(f"The least profitable item is {least_profitable_item} with {total_revenue[least_profitable_item]} $")

####################################################################3


#    File handling

with open("student.txt", "w") as file:
    content = file.write("Welcome to Student database system!")
    file.close()


with open("student.txt", "r") as file:
    content = file.read()
    file.close()
print(content)
























































####################################################33


#   Student database system with dict and file handling























