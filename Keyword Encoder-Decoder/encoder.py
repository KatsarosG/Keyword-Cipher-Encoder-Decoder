abc = "abcdefghijklmnopqrstuvwxyz"

while True:
    key = str(input("Key? : "))
    string = str(input("Str? : "))
    abc = "abcdefghijklmnopqrstuvwxyz"

    string = string.upper()
    key = key.upper()
    NumStr = []
    NumKey = []

    NumAbc = []

    for n in string:
        if ord(n) - 64 < 27 and ord(n) - 64 > 0:
            NumStr.append(ord(n) - 64)

    for n in key:
        if ord(n) - 64 < 27 and ord(n) - 64 > 0:
            NumKey.append(ord(n) - 64)

    NewNumStr = []
    loop = 0 
    while len(NewNumStr) < len(NumStr): 
        for i in NumKey:
            if len(NewNumStr) < len(NumStr):
                new = NumStr[loop] + i
                if new > len(abc):
                    new = new - len(abc)
                new = chr(new + 64)
                NewNumStr.append(str(new))
                loop += 1 

    converted = ''.join(NewNumStr)
    print(converted)
