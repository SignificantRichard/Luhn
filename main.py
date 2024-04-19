# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor

information: str = ""

def printMenu():
    print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          Enter menu option (1-9)
          ''')

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def enterCustomerInfo():
    # brian decided to declare types.
    firstname: str = "";
    lastname: str = "";
    city: str = "";
    postalcode: str = "";
    creditcard: str = "";

    # enter in user information
    firstname = input("First Name:\n")
    lastname = input("Last Name:\n")
    city = input("City:\n")
    
    # calls validate postal code to check if that postal code is in the loop
    while not validatePostalCode(postalcode):
        postalcode = input("Postal Code:\n").upper()

    # calls validate credit card to check if the card is valid
    while not validateCreditCard(creditcard):
        creditcard = input("Card:\n") # TO DO: ADD CREDIT CARD CHECK
    
    # returns to set global infomation
    return f"{firstname}|{lastname}|{city}|{postalcode}|{creditcard}"

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validatePostalCode(code: str):
    # check length of postal code first. Less expensive if we get this before looping through everything
    if len(code) >= 3:
        # reads the file
        with open("postal_codes.csv","r") as f:
            # since the first line is just a title, we can just ignore this line
            line = f.readline()
            # loops through everything
            while line:
                # reads current line and splits
                line = f.readline().split("|")
                # checks the postal code
                if line[0] == code:
                    return True
                elif line == [""]:
                    # returns false if end of the list is reached (marked by an empty string in list)
                    return False
                

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''

# TODO: Test everything.

def evenLuhnSum(evenintnums: int):
    doublednum: int = 0;
    sum: int;
    i: int;

    for i in range(len(evenintnums)):
        doublednum = evenintnums[i] * 2;
        
        # A little bit of an explanation on how the following two lines of code work:
        # The interesting thing about the Luhn algorithm is that, assuming that you
        # are only working with numbers from 1-9, you will always get a range of numbers
        # that is less than 20.
        #
        # One other interesting thing to note about the Luhn algorithm is that, for as
        # long as that holds true, when one goes about summing all of the digits in one's
        # number, it will always be equal to double the original number minus 9.
        #
        # To be completely honest, I do not know why this holds true mathematically as I
        # only ever managed to find this interesting quirk when looking at the examples
        # of the algorithm working on Google Classroom, noticing that there existed a
        # consistent pattern when one summed the digits of every number that was greater
        # than 9.
        #
        # It seems cursed, but it _does_ work, so who cares.
        
        if (doublednum > 10):
            doublednum -= 9;

        sum += doublednum;

    return sum;


def validateCreditCard(creditcard: str):
    validlen: int = 9;
    evenintnums: int = [];
    sum: int = 0;
    i: int;
    
    if (len(creditcard) ==  validlen and creditcard.isnumeric):
        creditcard = creditcard.reversed();
        
        for i in range(validlen):
            if (i % 2):
                evenintnums += [int(creditcard[i])]
            else:
                sum += int(creditcard[i]);
        
        sum += evenLuhnSum(evenintnums);

    # Return 0 if the final Luhn sum is not fully divisible by 10 (i.e. after dividing by
    # 10, there exists a remainder) to indicate that the given credit card number was invalid
    # Else, return 1 to indicate that the given credit card number was valid.
    return 0 if (sum % 10) else 1;


'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def generateCustomerDataFile(data):
    
    # writes data to fileOutput ... \fileName.csv
    # ex: c:\users\john\desktop\jane.csv
    fileOutput: str = ""
    fileName: str = ""

    fileOutput = input("Output location\nEx: c:\\users\\john\\desktop\\\n")
    fileName = input("File Name:\n")
    
    with open(fileOutput + fileName + ".csv", "w") as f:
        f.write(data)

def validateCustomerDataFile(fileName, fileOutput):
    # checks if file contains invalid characters (windows only)
    # TO DO: ADD MACOS FORBIDDEN FILES
    # TO DO: CHECK IF FILE LOCATIONS EXIST
    # TO DO: CHECK IF FILE NAME IS VALID
    # TO DO: CHECK IF DRIVE IS VALID

    characters = "*\"/\\<>:|?"
    for i in characters:
        if i in fileName:
            return False
    ["CON", "PRN", "AUX", "NUL" ,
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"]

    # check if the file name is the above and return false if true

    return True # as the final line for validation

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################




####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"

# More variables for the main may be declared in the space below


while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        information = enterCustomerInfo()

    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile(information)

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")
