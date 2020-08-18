def encrypt(a):
    result = ""
    s = 4
    for i in range(len(a)):
        char = a[i]
        #uppercase , lowercase , digits
        #uppercase 
        # A -> 65 -> 69 -> E
        if char.isupper():
            result += chr((ord(char)+ s -65) %26 +65)
        #lowercase
        elif char.islower():
            result += chr((ord(char)+ s -97) %26 +97)
        elif char.isdigit():
            x = int(char)
            y = x + 4
            result += str(y)
        else:
            result += char
    return result
mystring = input("Enter text to hash : ")
hash_obj = hashlib.md5(mystring.encode())
a = hash_obj.hexdigest()
#print(a)
a = a[::-1]
#print(a)
a = encrypt(a)
#print(a)
hash_obj1 = hashlib.blake2b(a.encode())
b = hash_obj1.hexdigest()
#print(b)
hash_obj2 = hashlib.md5(b.encode())
b = hash_obj2.hexdigest()
print(b)
