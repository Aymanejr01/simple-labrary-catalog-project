import os 
books_catalog = {}

def clear() :
    os.system ("cls" if os.name == "nt" else "clear")

def add_book() :
    while True :
        clear ()
        print ("\n let's add a book : ")
        isbn = int (input ("Tap the ISBN : "))
        title = input ("Enter the title : ")
        author = input ("Enter the name of the auhtor : ")
        print (f"The book {title} by the author {author} with the ISBN : {isbn} has add to the catalog ✅")

        #add to the dictionary
        books_catalog[isbn] = {"title" : title , "author" : author , "availble" : True }

        #add another ?
        if input ("\n Do you want to add another book ? (y/n) : ").lower() != "y" : 
            break

def check_out() : 
    while True : 
        clear()
        print ("\n Let's check out a book : ")
        isbn = int ( input ("Tap the ISBN of the book : "))
        if isbn in books_catalog :
            if books_catalog[isbn]["availble"] : 
                print (f"The book {books_catalog[isbn]["title"]} has been check out succefully ✅ ")
                books_catalog[isbn]["availble" ] = False
            else : 
                print (f"Sorry , the book {books_catalog[isbn]["titel"]} is already checked out ◾◾◾ ")
        else : 
            print ("The ISBN you entered is not in the catalog to be checked out ◾◾◾")
        
        if input ("Do you want to check out another book ? (y/n) : ").lower() != "y" : 
            break

def check_in() : 
    while True :
        clear () 
        print ("\n Let's check in a book : ")
        isbn = int ( input ("Tap the ISBN : "))
        if isbn in books_catalog : 
            if books_catalog[isbn]["availble"]:
                print ("This book is not checked out ! It stell with us ◾◾◾")
            else :
                print ("Thank you for the cheking in 🙌 ")
                books_catalog[isbn]["availble"] = True 

        else :
            print ("This book is not the catalog ◾◾◾")

        if input ("\nDo you want to check in another book ? (y/n) :").lower() != "y" :
            break

def show_all_books() :
    while True : 
       clear()
       print ("\n These are all the books in the catalog : ")
       for isbn in books_catalog :
        # for key in isbn : 
            book = books_catalog[isbn]
            print (f"ISBN : {isbn} , Title : {book["title"]} , Author : {book["author"]} , Availble : {book["availble"]}")
       if input ("Do you want to return to the main menu ? (y/n) : ").lower() != "y" :
           break

while True :
    clear ()
    print ("\n** ** The catalog : ** ** ")
    print ("1 - Add a book .")
    print ("2 - Check out a book .")
    print ("3 - Check in a book .")
    print ("4 - Show all the books .")
    print ("5 - Exit . ")
    choice = input ("\nTap a number : ")

    if choice == "1"  :
        add_book()
    elif choice == "2" :
        check_out()
    elif choice == "3" :
        check_in()
    elif choice == "4" :
        show_all_books()
    elif choice == "5" :
        print ("Thank you for your time .. \n")
        break
    else :
        input ("The number you entered is not inviled ! ")