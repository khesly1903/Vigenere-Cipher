
# Vigenère Cipher

A Python implementation of the Vigenère cipher, a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution.
For more detailed information, you can read my Medium article.   
[EN]: https://medium.com/@kayaberkay1626/a-legend-in-the-history-of-cryptography-the-vigenère-cipher-99f270ea9f66   
[TR]: https://medium.com/@kayaberkay1626/kriptografi-tarihinde-bir-efsane-vigenère-şifresi-c5e1f5940664


## Features

- Encrypt and decrypt text using the Vigenère cipher
- Generate random keys or use manual keys
- Input validation for both text and keys
- Preserves case (uppercase/lowercase) in the output
- Handles only English alphabetic characters (A-Z, a-z)


## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/vigenere-cipher.git
   cd vigenere-cipher
2. Run the program:
   ```bash
   python vigenere.py

3. Fallow the promts:
- Choose to encrypt or decrypt
- Enter your text
- Choose to generate a random key or enter one manually

## Example Usage

Encryption with manual key
```bash
(E)ncrypt or (D)ecrypt the text: e
Plaintext: Hello Cryptography World 1729! 
(G)enerate or (M)anual key: m
Key: cryptokey
Original Text:  Hello Cryptography World 1729!
          Key:  cryptokey
Processed Key:  crypt okeycryptoke ycryp 1729!    
       Result:  Jvjah Qbcnvfegtdrc Uqijs 1729!
````

Decryption with manual key
```bash
(E)ncrypt or (D)ecrypt the text: d
Ciphertext: Jvjah Qbcnvfegtdrc Uqijs 1729!
(G)enerate or (M)anual key: m
Key: cryptokey
Original Text:  Jvjah Qbcnvfegtdrc Uqijs 1729!
          Key:  cryptokey
Processed Key:  crypt okeycryptoke ycryp 1729!    
       Result:  Hello Cryptography World 1729! 
```

Encryption with generated key
```bash
(E)ncrypt or (D)ecrypt the text: e
Plaintext: Hello Cryptography World 1729! 
(G)enerate or (M)anual key: g
Original Text:  Hello Cryptography World 1729! 
          Key:  owqdqijuyzyvbrzfcyredujarecopiu   
Processed Key:  owqdq ijuyzyvbrzfc yredu 1729!    
       Result:  Vaboe Kasnsmbsroma Ufvox 1729! 
```





  

