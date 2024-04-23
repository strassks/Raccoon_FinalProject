# Name: Kaileb Strasser, Max Schiller, & Connor Laughlin
# email: strassks@mail.uc.edu, schillms@mail.uc.edu, laughlcd@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/23/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Decrypt text and json files to uncover details about taking a group photo on campus with a movie quote
# Brief Description of what this module does: Calls all the functions and classes that we created and prints desires results to console
# Citations: Chat GPT
# Anything else that's relevant:

#decryption.py

import json
from cryptography.fernet import Fernet
from PIL import Image
import os,sys
from io import BytesIO

def decrypt_location(encrypted_data, english_file):
    with open(english_file, 'r', encoding='utf-8') as file:
        english_words = file.readlines()
    
    decrypted_location = ""
    for index in encrypted_data:
        try:
            line_number = int(index) # Adjusting to 0-based indexing
            decrypted_location += english_words[line_number].strip() + " "
        except IndexError:
            print(f"Index {index} is out of range.")
    
    return decrypted_location.strip()
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return    decrypted_message.decode('utf-8')



