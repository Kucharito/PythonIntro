inputString=input("Input your string here: ")
print("Original string is ", inputString )
print("Printing only even index chars")
for i in inputString:
    if inputString.index(i)%2==0:
        print(i)