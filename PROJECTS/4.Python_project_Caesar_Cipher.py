'''
Caesar cipher: Technique to send secret messages
            : basic method to encrypt and decrypt messages

    plain text --> caesar text      == encryption
    caesar text --> plain text      == decryption
'''
"""
general formula : 
                encryption: (x+n) % 26
                decryption: (x-n) % 26
                            x: position of given letter
                            n: no of shifts you want

"""

def encryption(plain_text, shift_key):
    



print("Welcome to Password encrypter and decrypter")
work=input("Type 'encrypt' for encryption and 'decrypt' for decryption")

text=input("Type your message \n")
shift= int(input("Enter shift key"))

if work=="encrypt":
    encryption(text, shift)     # fn calling
if work=="decrypt":
    decryption(text, shift)     # fn calling
