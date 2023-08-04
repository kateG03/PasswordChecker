# User input + password generator. Second highest file to main.
import random
from PG_checks import checks

#Define "global" variables
UPPERCASE = ""
LOWERCASE = ""
NUMBER = ""
SPECIAL = ""
PASSWORD = ""
#Checks if user has inputed a password that meets all the critera
bool = False

#Generates a random password based on the user's selected level. Assigns the length of the 
#final string to PASSWORD
def generator(UPPERCASE, LOWERCASE, NUMBER, SPECIAL):
    #Make the password accessible outside of this function.
    global PASSWORD
    PASSWORD = input("Create a password that contains " + UPPERCASE + " uppercase letter(s)," + LOWERCASE + " lowercase letter(s)," + NUMBER + " number(s), and " + SPECIAL + " special character(s).")

#Asks user for their leve. Calls generator() and checks().
#Assigns the difficulty as well via number of elements.
def passwordlevel():
    #Make these assignments accessible outside of this function.
    global UPPERCASE
    global LOWERCASE
    global NUMBER
    global SPECIAL
    global bool
    #Ask user for their level
    ans = input("Select your level for the password game (1 : 2 : 3): ")
    #Level 1 (easiest)
    if(ans == "1"):
        UPPERCASE = random.choices("0234", weights = (1, 3, 3, 3))[0]
        LOWERCASE = random.choices("0123", weights = (1, 3, 3, 3))[0]
        NUMBER = random.choices("0123", weights = (1, 3, 3, 3))[0]
        SPECIAL = random.choices("012", weights = (1, 3, 3))[0]
        generator(UPPERCASE, LOWERCASE, NUMBER, SPECIAL)
        bool = checks()

    #Level 2 (regular)
    elif (ans == "2"):
        UPPERCASE = random.choices("0345", weights = (1, 3, 3, 3))[0]
        LOWERCASE = random.choices("0345", weights = (1, 3, 3, 3))[0]
        NUMBER = random.choices("012345", weights = (1, 3, 3, 3, 3, 3))[0]
        SPECIAL = random.choices("01234", weights = (1, 3, 3, 3, 3))[0]
        generator(UPPERCASE, LOWERCASE, NUMBER, SPECIAL)
        bool = checks()

    #Level 3 (hardest)
    elif (ans == "3"):
        UPPERCASE = random.choices("04567", weights = (1, 3, 3, 3, 3))[0]
        LOWERCASE = random.choices("0123456", weights = (1, 3, 3, 3, 3, 3, 3))[0]
        NUMBER = random.choices("012345678", weights = (1, 3, 3, 3, 3, 3, 3, 3, 3))[0]
        SPECIAL = random.choices("012345", weights = (1, 3, 3, 3, 3, 3))[0]
        generator(UPPERCASE, LOWERCASE, NUMBER, SPECIAL)
        bool = checks()

    #If user inputs a number other than 1/2/3 try again (rest from the top)
    else:
        print("No such number, try again")
        passwordlevel()

    #After user inputs a password, check the critera.
    #If it meets the criteria:
    if bool:
        x = input("Nice password! Would you like to play again? (Y/N): ")
        if (x == "Y" or x == "y"):
            passwordlevel()
        else:
            return
        
    #If it does not meet the criteria:
    else:
        x = input("Sorry! You didn't make a good password. Would you like to play again? (Y/N): ")
        if (x == "Y" or x == "y"):
            passwordlevel()
        else:
            return