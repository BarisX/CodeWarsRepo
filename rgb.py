def xToHex(number):
    actualNumber, afterPoint = int(number/16),float(number/16.00)-int(number/16)
    print(actualNumber,afterPoint)
    first, second = "",""
    if actualNumber < 10: first = actualNumber
    elif actualNumber >= 10: first = chr((65+actualNumber%10))
    else: print("error")
    
    afterPoint = int(afterPoint * 16)
    if afterPoint < 10: second = afterPoint
    elif afterPoint >= 10: second = chr((65+afterPoint%10))
    else: print("error")
    
    return str(first)+str(second)
def rgb(r, g, b):
    return xToHex(r)+xToHex(g)+xToHex(b)
    

print(rgb(220,20,60))