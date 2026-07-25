import os

def main():
    FileName = input("Enter file name : ")

    if os.path.exists(FileName):
        print(f"{FileName} is present in current directory")
    else:
        print(f"{FileName} is not present in current directory")

if __name__ == "__main__":
    main()