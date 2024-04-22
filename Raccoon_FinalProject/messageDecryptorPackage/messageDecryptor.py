# Name: Kaileb Strasser, Max Schiller, & Connor Laughlin
# email: strassks@mail.uc.edu, schillms@mail.uc.edu, laughlcd@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/23/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Decrypt text and json files to uncover details about taking a group photo on campus with a movie quote
# Brief Description of what this module does:
# Citations:
# Anything else that's relevant:

#messgaeDecryptor.py

from cryptography.fernet import Fernet

class MessageDecryptor:
    def __init__(self, key):
        """
        Constructor for MessageDecryptor.

        @Param:key (bytes): The key used for decryption.
        """
        self.key = key
        self.cipher = Fernet(self.key)

    def decrypt(self, encrypted_message):
        """
        Decrypt the provided message.

        @Param: encrypted_message (bytes): The encrypted message.

        @return: str: The decrypted message as a UTF-8 encoded string.
        """
        try:
            # Decrypt the message
            decrypted_message = self.cipher.decrypt(encrypted_message)
            return decrypted_message.decode('utf-8')
        except Exception as e:
            print(f"Error during decryption: {e}")
            return None
    
