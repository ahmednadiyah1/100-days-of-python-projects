def encrypt(text, s):
    result=""
    for i in range(len(text)):
        char=text[i]
        if (char.isupper()): #if character is uppercase
            result+=chr((ord(char)+s-64)%26+65) #unicode of A is 65

        if (char.islower()): #if character is lowercase
            result+=chr((ord(char)+s-96)%26+97) #unicode of a is 97

    return result

def decrypt(text, s):
    result=""
    for i in range(len(text)):
        char=text[i]
        if (char.isupper()): #if character is uppercase
            result+=chr((ord(char)-s-66)%26+65)

        if (char.islower()):
            result+=chr((ord(char)-s-98)%26+97)

    return result

text=input("Enter text: ")
shift=int(input("Enter shift: "))
encrypted_text=encrypt(text,shift)
decrypted_text=decrypt(encrypted_text, shift)
print(encrypted_text," ", decrypted_text)

