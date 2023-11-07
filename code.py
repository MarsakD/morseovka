from machine import Pin
from time import sleep_ms

pin = Pin(25, Pin.OUT)

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

def text_to_morse(text):
    morse_code = ''
    for char in text:
        if char != ' ':
            morse_code += MORSE_CODE_DICT[char.upper()] + ' '
        else:
            morse_code += ' '
    return morse_code

def blink_morse_code(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            pin.on()
            sleep_ms(100)
            pin.off()
            sleep_ms(100)
        elif symbol == '-':
            pin.on()
            sleep_ms(300)
            pin.off()
            sleep_ms(100)
        elif symbol == ' ':
            sleep_ms(300)

zprava = input("Zadej zpravu: ")
morse = text_to_morse(zprava)
blink_morse_code(morse)