import printDIP


userInput = ""

def printMenu():
    """Print a simple menu."""
    
    print()
    print("1 - set address on DIP")
    print("2 - get address from DIP ")
    print("q - exit")
    print()    

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

def getAddress():
    """Get address from user input (from DIP switches)."""

    inputString = ""
    getDipList = []
    print("Please, input DIP switches configuration \
as list (domain number, station number: 0 1 0 0 1 0 1 1...):")
    inputString = input("-->").split(None)

    
    
    for k in inputString:
        if k == '1':
            getDipList.append(True)
        else:
            getDipList.append(False)

    if len(getDipList) != 16:
        print("Error with a list members quantity.")
        return

    ## Дописать прогу!!!!
    
        
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


    
