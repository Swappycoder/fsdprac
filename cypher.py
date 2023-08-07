def encrypt_text(plaintext,key):
    text = ""
   
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        if ch==" ":
            text+=" "
         
        elif (ch.isupper()):
            text = text + chr((ord(ch) + key-65) % 26 + 65)
        
        else:
            text = text + chr((ord(ch) + key-97) % 26 + 97)
    
    return text



plaintext = "MOHIT"
key = 1
print("Plain Text is : " + plaintext)
print("Shift : " + str(key))
print("Cipher Text is : " + encrypt_text(plaintext,key))

