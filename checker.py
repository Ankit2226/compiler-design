import string
try:
    with open("data.txt","r") as file:
      print("file open sucessfuly !!!")
      content =file.read()
      lowercase=[]
      uppercase=[]
      numbercase=[]
      puncutationscase=[]
      for char in content:
           if char.islower():
               lowercase.append(char)
           elif char.isupper():
               uppercase.append(char)
           elif char.isdigit():
               numbercase.append(char)
           elif char in string.punctuation:
               puncutationscase.append(char)
      print("lower case letters :",','.join(lowercase))
      print("upper case letters :",','.join(uppercase))
      print("number letters :",','.join(numbercase))
      print("puncation marks:",','.join(puncutationscase))

    if content:
       print("file content is :: >>>>>>")
       print(content)
        


    else:
       print("the file is empty !!")
except FileNotFoundError:
     print("error : file not found  !!")        
  
except IOError as e:
    print("error reading the file: {e}")