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

def decrypt_text(text,key):
    ciphertext = ""
   
    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        
        if ch==" ":
            ciphertext +=" "
         
        elif (ch.isupper()):
            ciphertext = ciphertext + chr((ord(ch) + key-65) % 26 + 65)
        
        else:
            ciphertext = ciphertext + chr((ord(ch) + key-97) % 26 + 97)
    
    return ciphertext


key = 1
text = encrypt_text(plaintext,key)
print("Plain Text is : " + ciphertext)
print("Shift : " + str(n))
print("plaintext Text is : " + decrypt_text(text,key))

plaintext = "MOHIT"
key = 1
print("Plain Text is : " + plaintext)
print("Shift : " + str(n))
print("Cipher Text is : " + encrypt_text(plaintext,key))

