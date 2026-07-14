def caesar(text, shift, encrypt=True): 
 if not isinstance(shift, int):
        return 'Shift must be an integer value.'

 if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

 alphabet = 'abcdefghijklmnopqrstuvwxyz'

 if not encrypt:
        shift = - shift
    
 shifted_alphabet = alphabet[shift:] + alphabet[:shift]
 translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
 encrypted_text = text.translate(translation_table)
 return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)
'''
#text to decrypt
encrypted_text = "Tflcu pfl gcvrjv izuv dv yriu dfddp?"
decrypted_text=decrypt(encrypted_text,17)
print(decrypted_text) '''

#text to encrypt
'''encrypted_text_2="I wanna."
encrypted_text_2 = encrypt(encrypted_text_2, 13)
print(encrypted_text_2)'''

s="Hello world"
print(s.isspace())

