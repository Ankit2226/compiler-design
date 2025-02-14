import string
from tabulate import tabulate

# Define keywords for simplicity
keywords = {"import", "from", "as", "is", "return", "def", "try", "except", "with", "open", "file", "read", "print", "for", "in", "if", "elif", "else", "class", "while", "break", "continue", "pass", "global", "nonlocal", "lambda", "assert", "yield", "raise", "del"}

# Function to simulate address and byte size
def get_address_and_size(var_name):
    return hex(id(var_name)), len(var_name.encode('utf-8'))

try:
    with open("data.txt", "r") as file:
        data = file.read()
        print("Calculating the capital, small letters, and other details in the file:")

        lower = []
        upper = []
        number = []
        punctuation = []
        variables = {}
        keyword_list = []

        for i in data:
            if i.islower():
                lower.append(i)
            elif i.isupper():
                upper.append(i)
            elif i.isdigit():
                number.append(i)
            elif i in string.punctuation:
                punctuation.append(i)

    
        words = data.split()
        for word in words:
            if word in keywords:
                keyword_list.append(word)
            elif word.isidentifier() and word not in keywords:
                address, size = get_address_and_size(word)
                variables[word] = (address, size)

        print("Lower case letters:", ','.join(lower))
        print("Upper case letters:", ','.join(upper))
        print("Number letters:", ','.join(number))
        print("Punctuation marks:", ','.join(punctuation))

       
        table_data = []
        for keyword in keyword_list:
            table_data.append(["Keyword", keyword, "str", f"{len(keyword.encode('utf-8'))} bytes", "-"])
        for var, details in variables.items():
            table_data.append(["Variable", var, "str", f"{details[1]} bytes", details[0]])

        # Print table
        print("\nCollected Data Table:")
        print(tabulate(table_data, headers=["Symbol", "Name", "Data Type", "Length", "Address"], tablefmt="grid"))

except FileNotFoundError:
    print("Error: file not found!!")

except IOError as e:
    print(f"Error reading the file: {e}")