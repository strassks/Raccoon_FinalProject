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

#main.py

from TextFileExtractorPackage.TextFileExtractor import TextFileExtractor
from ImageLoaderPackage.ImageLoaderClass import ImageLoader

def main():
    # TextFileExtractor
    file_path = "../Files/UCEnglish.txt"
    line_numbers = [42061, 44404, 28799, 298, 8848, 27781, 105654, 21723, 47096, 8021, 28420, 19312, 22147, 42049, 23887, 599, 105655, 24232, 19312, 9443]
    TextFileExtractor(file_path, line_numbers)

    # ImageLoader
    image_path = "../Files/sample_image.jpg"
    image_loader = ImageLoader(image_path)
    image = image_loader.load_image()

    # Print the image to the console
    print(image)

if __name__ == "__main__":
    main()
