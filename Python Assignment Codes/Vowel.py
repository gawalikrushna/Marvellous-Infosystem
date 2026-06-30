def Vowel():

    Char = input("Enter character : " )

    if len(Char) != 1:
        print("Enter only one character")

    elif Char in "aeiouAEIOU":
        print("Its vowel")

    else:
        print("Not vowel")

if __name__ == "__main__":
    Vowel()