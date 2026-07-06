def String():
    Name = (input("Enter a name : "))
    count = 0

    for ch in Name:
        count += 1

    print("Length of string is : ",count)
        
if __name__ ==  "__main__":
    String()