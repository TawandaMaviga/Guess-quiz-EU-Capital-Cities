import gspread
import random
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", 
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("guess.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Guess Quiz-EU Capital Cities')

print("Welcome to the European Capital Guessing Game!")
print("Are you ready to test your knowledge?")

def display_instructions():
    """"""
    ("Displays instructions on how to play the game.")
    """"""
    print("/n--- instructions ---")
    print("The quiz will ask you to guess the capital city of the European Union.")
    print("Four city names will be displayed, including the correct one.")
    print("Choose the correct city by typing its name correctly.")
    print("You can exit the game at anytime by typing 'quit'.")
    print("Goodluck!")

    def main_menu():
        """"""
        ("Displays the main menu options.")
        """"""
        print("/nMain Menu")
        print("Start Game")
        print("Instructions")
        print("Exit")

cities = ["Brussels", "Frankfurt", "Luxemborg", "Strasbourg"]
cities_to_guess = random.choice(cities) #Pick random cities from this list

print("Guess the capital city of the European Union")
for city in cities:
    print(city)

while True:
    guess = input("Enter your guess(or 'quit' to exit):/n ").lower() #Converted guess to lower case

    if guess == 'quit':
        break  # Exit the loop if user enters "quit"

    if guess == "brussels":
        print("Congratulations! You guessed correctly.")
        break #Exit the loop if the user guesses correctly

    print("incorrect. Try again.")







