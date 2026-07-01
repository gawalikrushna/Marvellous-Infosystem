Square = lambda No : No * No

def main():
    Data = [2,3,4,5,6]

    MData = list(map(Square, Data))

    print("Squares of list elements : ",MData)
if __name__ == "__main__":
    main()