import printDIP
from parseAddressString import parseAddressString

# User input for menu.
# This variable is initialized with "_" (not empty string) because
# in checking for memebership empty string "" will return True in
# any other string (6.10.2. Membership test operations).
menuInput = "_"

#===============================================================================
def printMenu():
    """Print a menu."""
    
    print()    
    print("--------[ Yoko DIP addressing ]--------")
    print()    
    print("1 set address on DIP")
    print("2 get address from DIP ")
    print("q quit")
    print()    

#===============================================================================
def setAddress():
    """Set address on DIP switches from user input."""
    
    MAXDOMAIN = 31
    MAXSTATION = 64
    
    try:
        domainNumber = int(input("Domain number (1-31) --> "))
        stationNumber = int(input("Station number (1-64) --> "))
        
        if domainNumber > MAXDOMAIN \
           or domainNumber < 1 \
           or stationNumber > MAXSTATION \
           or stationNumber < 1:
            raise ValueError

        # Output to console.        
        printDIP.printDIP(domainNumber, stationNumber)
        
    except ValueError:
        print()
        print("Error:")
        print("Input should be an integer in range.")

#===============================================================================
def getAddress():
    """Get address from user input (from DIP switches)."""

    print("""Please input DIP switches configuration \
as string (domain number: 10000011...).""")
    
    domainString = input("DOMAIN --> ")
    stationString = input("STATION --> ")

    address = parseAddressString(domainString, stationString)
    print()
    match(address[0]):
        case 0:
            print("Domain input parameter error.")
        case 1:
            print("Station input parameter error.")
        case 2:
            print("Domain decode error.")
        case 3:
            print("Station decode error.")
        case 4:
            print(f"""\t=========================
        |Domain address:\t{address[1]}
        =========================
        |Station address:\t{address[2]}  
        =========================""")


#====================   Menu cycle  ============================================
while (True):
    
    printMenu()
    menuInput = input("--> ")
    print()
    match (menuInput):
        case '1':
            print("Set address to DIP.")
            setAddress()
        case '2':
            print("Get address from DIP.")
            getAddress()
        case 'q' | 'Q':
            print("Programm is closing...")
            break
        case _:
            print("\tInput a menu item.")
        

