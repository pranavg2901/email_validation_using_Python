
email = input("Enter Your Email: ")
k = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '-']
w=j=d=0
if len(email) >= 6:
    if "@" in email and email.count('@') == 1:
        if email[0].isalpha():
            if (email[-5] == '.') ^ (email[-4] == '.') ^ (email[-3] == '.'):
                if email.count('.') <= 3:
                    if ' ' not in email:
                        if str(k) in email:
                            print("Invalid,Special Character Not allowed")
                        else:
                            print("Congrats...!\nYour Email Address Is Appropriate")
                    else:
                        print("Invalid,Space is not allowed")
                else:
                    print("Invalid, Too much in dot '.' in mail\nOnly 3 dots are allowed")
            else:
                print("Invalid, dot '.' is missing before domain\nPlease give dot before 'com','in','yahoo'")
        else:
            print("First letter of email id is always character")
    else:
        print("Invalid, '@' missing")
else:
    print("Invalid,Your email address is too short")
