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

#main.py

file_path = "../Files/UCEnglish.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

line_numbers = [42061, 44404, 28799, 298, 8848, 27781, 105654, 21723, 47096, 8021, 28420, 19312, 22147, 42049, 23887, 599, 105655, 24232, 19312, 9443]

for line_number in line_numbers:
    line_content = lines[line_number ].strip()  # Adjusting for 0-based index
    print(line_content)
