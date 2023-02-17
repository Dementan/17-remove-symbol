#create program to remove any symbol in a string

str1 = input("Enter any string: ")
symbol = input("Enter a symbol you want to remove: ")
# create empty string
str2 = ""
for i in str1:
    # if element in the string is not equal to symbol to remove, add it in the empty string
    if i != symbol:
        str2 = str2 + i
print(str2)
