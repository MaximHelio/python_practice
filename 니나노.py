s = input()
if "a" <= s <= "z":
    result = s + "(ASCII: " + str(ord(s)) + ")" + \
    " => " + s.upper() +"(ASCII: " + str(ord(s.upper())) +")"
    print(result)
if "A" <= s <= "Z":
    result = s + "(ASCII: " + str(ord(s)) + ")" + \
    " => " + s.lower() +"(ASCII: " + str(ord(s.lower())) +")"
    print(result)
 
 
