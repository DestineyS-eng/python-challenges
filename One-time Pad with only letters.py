import secrets


ALPHA = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# ALPHA_ENCRYPT has twice as many elements compared to ALPHA to compensate for max math (26+26=52)
ALPHA_ENCRYPT=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#creates a random sequence of the list i will refer back to with the join number output so 
# even if you have the key its impossible to find the orginal message 
secrets.SystemRandom().shuffle(ALPHA_ENCRYPT)

#this choices any thing within ALPHA at the same length to be the key
def Key(s):
    return secrets.SystemRandom().sample(ALPHA,len(s))
#find the index value of of each letter in the key and message
def store_values(s, key):
    value = []
    key_value = []
    for letter in s:
        for i in range(len(ALPHA)):
            if letter==ALPHA[i]:
                value.append(i)
    for char in key:
        for x in range(len(ALPHA)):
            if char == ALPHA[x]:
                 key_value.append(x)
    return value,key_value

#adds the total of the numbers and finds its element in the second alpha list using the number found as index 
def encrypt(message, key):
    encrypted = ""
    store = []
    for i in range(len(message)):
        a = (message[i] + key[i])
        store.append(a)
    for num in store:
        encrypted += ALPHA_ENCRYPT[num]
    return encrypted
  
#finds the orginal message using the key and encrypted letters 
def decrypt(encrypted, key):
    key_values = []
    encryted_values = []
    total = []
    letters =""
    key = "".join(key)

    for char in key:
        for i in range(len(ALPHA)):
            if char == ALPHA[i]:
                key_values.append(i)
                break
    for Echar in encrypted:
        for x in range(len(ALPHA_ENCRYPT)):
            if Echar == ALPHA_ENCRYPT[x]:
                encryted_values.append(x)
                break

    for j in range(len(key_values)):
        if encryted_values[j]>key_values[j]:
            total.append(encryted_values[j] - key_values[j])
        elif encryted_values[j]>key_values[j]:
            total.append(key_values[j]-encryted_values[j]) 
        elif encryted_values[j]==key_values[j]:
            total.append(encryted_values[j] - key_values[j])

    for num in total:
        letters+=ALPHA[num]

    return letters


userinput=input("Enter your message:  ")

if userinput.replace(" ","").isalpha():
    userinput=userinput.replace(" ","").upper()
            
    OGkey=Key(userinput)

    message,key=store_values(userinput,OGkey)
    
    encrypted=(encrypt(message,key))
    decrypted=decrypt(encrypted,OGkey)
  #puts the ciphertext and plaintext in a text file 
    with open("ENCRYPTandDECRYPT.txt","w") as file:
        file.write(f"encrypted: {encrypt(message,key)}")
        file.write(f"\nYour orginal message was: {decrypted}")
    print("Message sent!")

