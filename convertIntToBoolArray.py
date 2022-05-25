def intToBoolArray(inputNumber):
    """Convert inputNumber to binary array."""

    # Convert integer to binary view string.
    tempString = f"{inputNumber:b}"

    result = []
    parityCheck = 0
    parityBit = False
    
    conversionList = []
    for k in tempString:
        if k == "0":
            conversionList.append(False)
        else:
            conversionList.append(True)
            parityCheck += 1

    if parityCheck % 2 == 0:
        parityBit = True

    result.append(parityBit)
    
    for k in range(1, 8 - len(conversionList)):
        result.append(False)
        
    result.extend(conversionList)
    
    return result

