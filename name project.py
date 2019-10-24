names = [ ]
count=0
while count<10:
    name = input("Enter a name:")
    names.append(name)
    count+=1
print (names)

print("Enter a name to search for or type 'End' to end the program")
Endprog=False
while (Endprog!= True) :
    search = input("Search for a name:")
    if search in names:
        print(search, "was found")
    elif search =="End":
        print("Thank you for testing this program")
        Endprog=True
    else:
        print(search, "was not found")
