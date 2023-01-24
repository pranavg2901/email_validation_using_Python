e = input("Enter Your Email: ")
k = j = d = 0

if len(e) >= 6:
    if e[0].isalpha():
        if "@" in e and e.count("@") == 1:
            if (e[-4] == '.') ^ (e[-3] == '.'):
                for i in e:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == '_' or i == '.' or i == '@':
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong 5")
            else:
                print("Wrong 4")
        else:
            print('Wrong 3')
    else:
        print("Wrong 2")
else:
    print("Wrong 1")
