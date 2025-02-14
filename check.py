import string 
try:
    with open("data.txt", "r") as file:
        data = file.read()
        print(data)
        print("calculaing the capital ,small letter in file : ")
        lower =[]
        upper =[]
        number =[]
        punctuation = []

        for i in data:
            if i.islower():
                lower.append(i)
            elif i.isupper():
                upper.append(i)
            elif i.isdigit():
                number.append(i)
            elif i in string.punctuation:
                punctuation.append(i)   

        print("lower case letters :",','.join(lower))
        print("upper case letters :",','.join(upper))
        print("number letters :",','.join(number))
        print("puntuation marks:",','.join(punctuation))

except FileNotFoundError:
     print("error : file not found  !!")        
  
except IOError as e:
    print("error reading the file: {e}")