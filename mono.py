plaintext = input("Enter a msg:")
key = "qwertyuiopasdfghjklzxcvbnm"

ciphertext = ""

for c in plaintext :
    if(c == " "):
        ciphertext += " "
        continue

    elif (c.isupper()):
            cipher =  key[(ord(c) - 65)]
            ciphertext = ciphertext + cipher.upper()

    else:
        cipher =  key[(ord(c) - 97)]
        ciphertext = ciphertext + cipher   

print("Cipher is : "+ ciphertext)
