import printDIP
from parseAddressString import parseAddressString

userInput = ""
## ================================================================
def printMenu():
    """Print a simple menu."""
    
    print()
    print("1 - set address on DIP")
    print("2 - get address from DIP ")
    print("q - exit")
    print()    
## ================================================================
def setAddress():
    """Set address on DIP switches from user input."""
    
    print("Please, input an necessary data:")
    
    try:
        domainNumber = int(input("Domain number (1-16) --> "))
        stationNumber = int(input("Station number (1-64) --> "))
        
        if domainNumber > 16 \
           or domainNumber < 1 \
           or stationNumber > 64 \
           or stationNumber < 1:
            raise ValueError

        # Output to console.        
        printDIP.printDIP(domainNumber, stationNumber)
        
    except ValueError:
        print()
        print("Error:")
        print("Input should be an integer in range.")
## ================================================================
def getAddress():
    """Get address from user input (from DIP switches)."""

##    domainString = ""
##    stationString = ""
    
    print("Please input DIP switches configuration \
as string (domain number: 010101101...):")
    domainString = input("DOMAIN --> ")
    stationString = input("STATION --> ")
    
    print()
    address = parseAddressString(domainString, stationString)
    print("Domain, station")
    print(address)
##    print(f"Domain number: {0}\nStation number: {1}", address[0], address[1])
    
## ===================== Main cycle =====================
while (userInput != 'q'):
    
    printMenu()
    userInput = input("--> ")

    try:
        caseNumber = int(userInput)
    except ValueError:
        continue
    else:
        print()
        match (caseNumber):
            case 1:
                setAddress()
            case 2:
                getAddress()


    
