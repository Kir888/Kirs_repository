list_mails = []
for n in range(10):
    print("Enter a full name")
    name = input()
    email = name.lower().replace(" ","")+"@gmail.com"
    list_mails.append(email)
print(list_mails)