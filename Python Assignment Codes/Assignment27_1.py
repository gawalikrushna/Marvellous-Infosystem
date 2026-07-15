class BookStore:

    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author

        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. Number of books {BookStore.NoOfBooks}")

bobj1 = BookStore("Python", "Guido")
bobj2 = BookStore("Java", "James Gosling")
bobj3 = BookStore("C", "Dennis Ritchie")

bobj1.Display()

bobj2.Display()

bobj3.Display()