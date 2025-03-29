import random
import string

def charToPos(letter: chr):
    if letter.islower():
        return ord(letter) - 97  
    elif letter.isupper():
        return ord(letter) - 65  
    else:
        return -1  

def posToChar(pos, is_upper: bool):
    if is_upper:
        return chr(pos + 65)  
    else:
        return chr(pos + 97) 
    
# makes it suitable for encryption
def vigeneredeKey(text: str, key: str) -> str:
    vigenereKey = ""
    vCount = 0
    
    for i in range(len(text)):
        if text[i].isalpha():
            vCount += 1
    
    if len(key) <= vCount:      
        for i in range(vCount):    
            vigenereKey += key[i % len(key)]
            
        for i in range(len(text)):
            if not text[i].isalpha():
                vigenereKey = vigenereKey[:i] + text[i] + vigenereKey[i:]
    else:
        key_index = 0
        for i in range(len(text)):
            if text[i].isalpha():
                vigenereKey += key[key_index % len(key)]
                key_index += 1
            else:
                vigenereKey += text[i]
                
    return vigenereKey
    
        
# 0 for encryption
# 1 for decryption
def vigenereFunction(text:str, key:str, type:bool) -> str:
    vigenereText = ""

    for i in range(len(text)):
        currentChar = text[i]
        currentIndex = charToPos(currentChar)
        
        currentKeyChar = key[i]
        currentKeyIndex = charToPos(currentKeyChar)
                
        if currentIndex == -1:
            vigenereText += currentChar
        else:            
            if type == False:
                vigenereIndex = (currentIndex + currentKeyIndex) % 26 
            else:
                vigenereIndex = (currentIndex - currentKeyIndex) % 26 
                
            vigenereChar = posToChar(vigenereIndex, currentChar.isupper())
            vigenereText += vigenereChar
            
    return vigenereText

# generate a random key of the same length as the text
def createVigenereKey(text:str) -> str:
    key = ""
    for i in range(len(text)):
        char = random.choice(string.ascii_lowercase)
        key += char
    return key

# check if the key is valid
def getKey() -> str:
    while True:
        try:
            key = input("Key: ")
            if not all(char.isalpha() and ord(char.lower()) < 128 for char in key):
                raise ValueError("Key must contain only English letters (A-Z, a-z), not special charcters or numbers.")
            return key
        except ValueError as e:
            print(e)
           
# check if the plaintext is valid 
# 0 for encryption
# 1 for decryption
def getText(type: bool) -> str:
    while True:
        try:
            if type == 0:
                text = input("Plaintext: ")
            else:
                text = input("Ciphertext: ")
            if not all(char.isalpha() and ord(char.lower()) < 128 for char in text if char.isalpha()):
                raise ValueError("Only English alphabetic characters allowed.")
            return text
        except ValueError as e:
            print(e)
            

def vigenere():
    while True:
        try:
            operation = input("(E)ncrypt or (D)ecrypt the text: ").lower()
            if operation not in ['e', 'd', 'encrypt', 'decrypt']:
                raise ValueError("Please enter 'E' for encrypt or 'D' for decrypt.")
            break
        except ValueError as e:
            print(e)
    
    if operation.startswith('e'):
        text = getText(0)
    else:
        text = getText(1)

    
    while True:
        try:
            key_option = input("(G)enerate or (M)anual key: ").lower()
            if key_option not in ['g', 'm', 'generate', 'manual']:
                raise ValueError("Please enter 'G' to generate a key or 'M' to enter manually.")
            break
        except ValueError as e:
            print(e)
    
    if key_option.startswith('g'):
        key = createVigenereKey(text)
    else:
        key = getKey()
    
    processed_key = vigeneredeKey(text, key)
    
    if operation.startswith('e'):
        result = vigenereFunction(text, processed_key, False)
    else:
        result = vigenereFunction(text, processed_key, True)
    
    print(f"Original Text:  {text}")
    print(f"          Key:  {key}")
    print(f"Processed Key:  {processed_key}")
    print(f"       Result:  {result}")
    
    
if __name__ == "__main__":
    vigenere()
