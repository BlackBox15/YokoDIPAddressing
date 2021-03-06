def parseAddressString(domainString, stationString):
    """Parsing input strings to Domain and Station addresses."""

    domainNameInList = []
    stationNameInList = []
    result = []
    
    ## Проверка входящей строки (номер домена) на длину.
    ## Адрес домена должен состоять из 8 символов,
    ## 1, 2-й бит должен быть всегда равен 0.
    lengthOfDomain = len(domainString)
    if lengthOfDomain == 8 and \
            domainString[1] == '0' and \
            domainString[2] == '0':
        
        domainNameInList = packStringToInteger(domainString)
        
    else:
        print("Domain parameter error")
        return;
    
    ## Проверка входящей строки (номер станции) на длину.
    ## Адрес станции должен состоять из 8 символов.
    if len(stationString) == 8:
        
        stationNameInList = packStringToInteger(stationString)
        
    else:
        print("Station parameter error")
        return;

    ## Parity bits.
    domainParityBit = domainNameInList[0]
    stationParityBit = stationNameInList[0]

    ## Quantity of addressing 1-bits.
    domainQnttyBits = domainNameInList[3:].count(1)
    stationQnttyBits = stationNameInList[1:].count(1)

    if (domainQnttyBits % 2 == 0 and domainParityBit == 1) or \
       (domainQnttyBits % 2 != 0 and domainParityBit == 0):
        
        domainAddress = listBinToInteger(domainNameInList[3:])
        result.append(domainAddress)
        
    else:
        print("Error in domain number.")
        return
        
    if (stationQnttyBits % 2 == 0 and stationParityBit == 1) or \
       (stationQnttyBits % 2 != 0 and stationParityBit == 0):
        
        stationAddress = listBinToInteger(stationNameInList[1:])
        result.append(stationAddress)
        
    else:
        print("Error in station number.")
        return
    
    return result
## ================================================================
def listBinToInteger(inputInteger):
    """Convert Binary List to Integer"""

    result = 0
    powerOfTwo = len(inputInteger) - 1

    for number in inputInteger:
        
        if number == 1:
            
            result += 1 * pow(2, powerOfTwo)
            
        powerOfTwo -= 1

    return result
## ================================================================
def packStringToInteger(inputString):
    """String \"010101011010\" to Integer array [0,1,0,1,0...]"""

    ## Empty Integer list.
    result = []
    
    for oneString in inputString:
        match(oneString):
            case("0"):
                result.append(0)
            case("1"):
                result.append(1)

    return result
