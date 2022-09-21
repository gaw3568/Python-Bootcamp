# 카이사르 암호 프로젝트
# 알파벳을 미리 정해진 수 만큼 뒤의 알파벳을 사용하는 방식의 암호화.
from Caesar_Cipher_Art import logo as Art_logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(Art_logo)

def caesar(text, shift, direction):
    cipher_text = ""

    for letter in text:
        if not letter in alphabet:
            cipher_text += letter
        else:
            position = alphabet.index(letter)

            if direction == "encode":
                position += shift
                if position >= len(alphabet):
                    position %= 26
                cipher_text += alphabet[position]
            elif direction == "decode":
                position -= shift
                if position < 0:
                    position = len(alphabet) + position
                cipher_text += alphabet[position]
            else:
                print("It is fault input text. Try Again")

    print(f"The {direction}d text is {cipher_text}")

isCipher = True

while isCipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text=text, shift=shift, direction=direction)
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if answer == "no":
        isCipher = False
        print("Goodbye")