print("Enter a string")
str1 = input()
changed_str = ""
for n in str1:
      if changed_str.count(n) < 1 or n == " ":
         changed_str += n
changed_str = changed_str.strip(" ")
print(changed_str)