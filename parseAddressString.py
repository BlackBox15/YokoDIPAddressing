def parseAddressString(domainString, stationString):
    """Parsing input strings to Domain and Station addresses."""

##    print(domainString)
##    print(stationString)

    encodingType = "ascii"
    
    domainByteArray = b''.join(bytes(k, encodingType) for k in domainString)
    stationByteArray = b''.join(bytes(k, encodingType) for k in stationString)

    print(f"domainByteArray = {domainByteArray}")
    print(domainByteArray)
    print(stationByteArray)

    print(format(domainByteArray[1], 'b'))
    
##    for oneByte in domainByteArray:
##        print(oneByte)
##    domainByteArray = bytearray(domainString, "utf-8")
##    testByteArray = bytearray()
##
##    testByteArray.join(format(domainString, 'b'))
##    
##    for k in domainByteArray:
##        testByteArray.join(k)
##    domainByteArray.join(format(k, 'b') for k in bytearray())
##    
##    print(domainByteArray)

