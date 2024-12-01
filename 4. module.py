
#  this module is only for practice everything we learned so far


##  Problem 1: File Handling - Count words and lines in .txt files


import os

# To count lines and words in each file, and handle subdirectories
def count_lines_and_words_in_txt_files(directory="."):
    # List to store file details
    file_details = []
    
    # Walk through the directory and its subdirectories
    for dirpath, files in os.walk(directory):
        for file in files:
            # Only process .txt files
            if file.endswith(".txt"):
                file_path = os.path.join(dirpath, file)
                
                try:
                    with open(file_path, "r") as f:
                        lines = f.readlines()
                        line_count = len(lines)
                        word_count = sum(len(line.split()) for line in lines)
                        
                        file_details.append((file, line_count, word_count, file_path))
                
                except Exception as e:
                    print(f"Error reading file {file}: {e}")
    
    # Sort by line count (descending) or word count (ascending)
    file_details.sort(key=lambda x: x[1], reverse=True)  # Sort by line count in descending order

    # Print details of each file
    for file, line_count, word_count, file_path in file_details:
        print(f"File: {file_path}")
        print(f"Lines: {line_count}, Words: {word_count}")
        print("-" * 40)

# Call the function
count_lines_and_words_in_txt_files()









