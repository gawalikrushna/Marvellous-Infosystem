String = lambda Name : len(Name) > 5

def main():

    Data = ["Krushna", "Ram", "Dhananjay", "John", "Kartik", "Deepak","Sham"]

    FData = list(filter(String, Data))

    print("Strings having length greater than 5 : ",FData)

if __name__ == "__main__":
    main()