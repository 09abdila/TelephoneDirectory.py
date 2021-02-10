# Telephone Directory

# Import The Copy Function
import copy

# Initial Dictionary List
teleDirec = {"Abdul":121,
             "Barry":122,
             "Flash":123
             }

def addNewNumber():

    # Prints a Space
    print ()

    # Complete Directory
    print ("Add New Contact:")
    
    # Prints a Space
    print ()
    
    # Prompt The User To Enter Information
    name = input("Enter a Name: ")
    number = int(input("Enter a Number: "))

    # Add The New Record To The Dictionary
    teleDirec.update({name:number})

    # Print a Space
    print ()

    # Exit Function
    return

def displayRecords():

    # Prints a Space
    print ()

    # Complete Directory
    print ("Contact List:")
    
    # Prints a Space
    print ()

    # Loop Through Every Key And Value In Order From teleDirec
    for name, number in sorted(teleDirec.items()):

        # Print Record
        print ("Name:", name)
        print ("Number:", number)
        
        # Print a Space
        print ()

    # Prints a Space
    print ()

    # Exit Function
    return


def searchRecord():

    # Prints a Space
    print ()

    # Complete Directory
    print ("Contact Search:")
    
    # Prints a Space
    print ()
    
    # Prompt The User To Enter a Name
    userIn = input("Enter a Name: ")

    # Loop Through Every Key And Value In Order From teleDirec
    for name, number in (teleDirec.items()):

        # If The User Input Equals The name Field In The Dictionary
        if name == userIn:

            # Print The Name And Number Of The Person Found
            print (name, "\nTelephone Number:", teleDirec[name])

    # Print a Space
    print ()

    # Exit The Function
    return

def deleteRecord():

   # Prints a Space
    print ()

    # Complete Directory
    print ("Delete a Contact:")
    
    # Prints a Space
    print ()

    # Make a Deep Copy Of The Dictionary
    teleDirec2 = copy.deepcopy(teleDirec)

    # Prompt The User To Enter a Name To Delete
    deleteName = input("Which Contact Would You Like To Remove: ")

    # Loop Through The Deep Copy Dictionary
    for name, number in (teleDirec2.items()):

        # If name Equals The User Input
        if name == deleteName:

            # Delete The Name From The Original Dictionary
            teleDirec.pop(name, number)

            # Let The User Know That The Conatct Has Been Deleted
            print ("Contact Deleted.")

    # Prints a Space
    print ()

    # Exit The Function
    return
    

def programExit():
    # Closes Program
    print ("Goodbye!")


while True:

    # Start Of The Menu
    print ("Telephone Directory Menu:")
    print ("Telephone Records:" , len(teleDirec))

    # Prints a Space
    print ()

    # Display All The Options
    print ("a - Add New Record")
    print ("b - View All Records")
    print ("c - Search/View For Single Entry")
    print ("d - Delete Record")
    print ("x - Exit")

    # Prints a Space
    print ()

    # Prompt The User To Choose An Option
    option = input("Enter An Option: ").lower()

    # Assigning All The Options
    if option == "a":
        addNewNumber()

    elif option == "b":
        displayRecords()

    elif option == "c":
        searchRecord()

    elif option == "d":
        deleteRecord()

    elif option == "x":
        programExit()
        break

    else:
        # If The Option Doesn't Exist
        print ("Option Does Not Exist")
        print ("Program Will Termniate")

        # End The Program
        pass
