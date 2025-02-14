import string 
try:
    with open("data.txt", "r") as file:
        data = file.read()
       # print(data)
        print("calculaing the capital ,small letter in file : ")
        lower =[]
        upper =[]
        number =[]
        punctuation = []
        keyword_list=[]
        keywords = {"import", "from", "as", "is", "return", "def", "try", "except", "with", "open", "file", "read", "print", "for", "in", "if", "elif", "else", "class", "while", "break", "continue", "pass", "global", "nonlocal", "lambda", "assert", "yield", "raise", "del"}

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

        print("lower case letters :",','.join(lower))
        print("upper case letters :",','.join(upper))
        print("number letters :",','.join(number))
        print("puntuation marks:",','.join(punctuation))
        print("keywords in the file :",','.join(keyword_list))

except FileNotFoundError:
     print("error : file not found  !!")        
  
except IOError as e:
    print("error reading the file: {e}")