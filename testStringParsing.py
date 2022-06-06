from parseAddressString import parseAddressString

firstArgument = "01110110"
secondArgument = "01011110"

parseAddressString(firstArgument, secondArgument)

##encodingType = "ascii"
##
##testBytes = bytes(b' ')
##tstBytes = b'still'
##
####simpleByte = bytes('s', encodingType)
##simpleByte = bytes(range(20))
####print(simpleByte)
##
##
####print(format(simpleByte,'s'))
##
####for k in tstBytes:
####    
####    print(type(k), k)
####    t = bytes(k)
####    
####    print(type(t), t)
####    
####    print("================================")
##
##
####testBytes.join(bytes(k) for k in bytes(firstArgument, encodingType))
##
##testBytes.join(format(k, 'b') for k in bytes(b'still'))
####
##print(type(testBytes))
##print(testBytes)
####

##bytesExample1 = bytes(k for k in b'sdfsdf')
##print("bytesExample1:")
##print(bytesExample1)
##print()
##
##for k in b'stooll':
##    print(type(k))
##    print(type(format(k, 'b')))
##    print(format(k, 'b'))
##    
##bytesExample2 = bytes()
##bytes3 = bytesExample2.join(bytes(format(k, 'b'), encodingType) for k in b'sfsdfsdf')
##print(bytes3)
##values = bytes(b'sdfsdf')
##
##
##bytesExample2 = b''
##values = [b'sdfsdf', b'sdfs', b'qwe']
##
##
##print("bytesExample2 :")
##print(bytesExample2.join(values) )
##print()


##it = iter(k for k in range(10))
##print(list(it))


