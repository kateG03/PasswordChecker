import PG_console
#Characters that are accepted in my password checker. Here for the comparisons
special = {"!", "@", "#", "$", "%", "^", "&", "*", "(",")", "<", ">", "~", ";", ":", ",", "-", "_", "+", "=" }
lowercase = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
uppercase = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}
number = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}

def checks():
    #Define the local number of elements (for checking)
    local_upper = 0
    local_lower = 0
    local_number = 0
    local_special = 0

    #For every character in the given user string
    for x in [*PG_console.PASSWORD]:
        #Print password
        print(x)

        #If character is an uppercase letter, local_upper++
        if(uppercase.__contains__(x) == True):
            #DEBUG: print("FOund upper")
            local_upper+=1

        #If character is a lowercase letter, local_lower++
        elif(lowercase.__contains__(x) == True):
            #DEBUG: print("FOund lower")
            local_lower+=1

        #If character is a number, local_number++
        elif(number.__contains__(x) == True):
            #DEBUG: print("FOund number")
            local_number+=1

        #If character is a special character, local_special++
        elif(special.__contains__(x) == True):
            #DEBUG: print("FOund special")
            local_special+=1

        else:
            #DEBUG: print("Matched nothing!")
            msg = "Clarity"
    #Check if the given elements match the number of user input elements. If true, return true.
    return ((int)(PG_console.UPPERCASE) == local_upper and (int)(PG_console.LOWERCASE) == local_lower and (int)(PG_console.NUMBER) == local_number and (int)(PG_console.SPECIAL) == local_special)