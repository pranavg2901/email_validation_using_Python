# email validation using regex
import re

condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
email = input("Enter Your Email Id: ")
if re.search(condition, email):
    print("True")
else:
    print('False')
