import csv

BOOK_FILE = "books.csv"


# Add Book Function
def add_book():

    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    quantity = input("Enter Quantity: ")

    with open(BOOK_FILE, 'a', newline='') as file:

        writer = csv.writer(file)
        writer.writerow([book_id, book_name, author, quantity])

    print("Book Added Successfully!")


# Search Book Function
def search_book():

    search = input("Enter Book Name or Author Name: ")

    found = False

    with open(BOOK_FILE, 'r') as file:

        reader = csv.reader(file)

        for row in reader:

            if search.lower() == row[1].lower() or search.lower() == row[2].lower():

                print("\nBook Found!")
                print("Book ID:", row[0])
                print("Book Name:", row[1])
                print("Author:", row[2])
                print("Quantity:", row[3])

                found = True

    if found == False:
        print("Book Not Found")


# Issue Book Function
def issue_book():

    student_name = input("Enter Student Name: ")
    book_id = input("Enter Book ID: ")

    books = []
    found = False

    with open(BOOK_FILE, 'r') as file:

        reader = csv.reader(file)

        for row in reader:

            if row[0] == book_id:

                found = True

                if int(row[3]) > 0:

                    row[3] = str(int(row[3]) - 1)

                    print("Book Issued Successfully!")
                    print("Issued To:", student_name)

                else:
                    print("Book Not Available")

            books.append(row)

    if found == False:
        print("Book ID Not Found")

    with open(BOOK_FILE, 'w', newline='') as file:

        writer = csv.writer(file)
        writer.writerows(books)


# Return Book Function
def return_book():

    book_id = input("Enter Book ID To Return: ")

    books = []
    found = False

    with open(BOOK_FILE, 'r') as file:

        reader = csv.reader(file)

        for row in reader:

            if row[0] == book_id:

                found = True

                row[3] = str(int(row[3]) + 1)

                print("Book Returned Successfully!")

            books.append(row)

    if found == False:
        print("Book ID Not Found")

    with open(BOOK_FILE, 'w', newline='') as file:

        writer = csv.writer(file)
        writer.writerows(books)


# Display Reports Function
def display_reports():

    total_books = 0
    available_books = 0

    with open(BOOK_FILE, 'r') as file:

        reader = csv.reader(file)

        for row in reader:

            total_books += 1
            available_books += int(row[3])

    print("\n===== Library Reports =====")
    print("Total Books:", total_books)
    print("Available Books:", available_books)


# Main Menu
while True:

    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Reports")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        add_book()

    elif choice == '2':
        search_book()

    elif choice == '3':
        issue_book()

    elif choice == '4':
        return_book()

    elif choice == '5':
        display_reports()

    elif choice == '6':
        print("Program Closed")
        break

    else:
        print("Invalid Choice")