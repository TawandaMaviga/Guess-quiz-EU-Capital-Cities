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


cities = ["Brussels", "Frankfurt", "Luxemborg", "Strasbourg"]
cities_to_guess = random.choice(cities) #Pick random cities from this list

#correct_city = cities_to_guess("Luxemborg") #i have put the correct city for easier access

print("Guess the capital city of the European Union")
for city in cities:
    print(city)

while True:
    guess = input("Enter your guess(or 'quit' to exit): ").lower() #Converted guess to lower case

    if guess == 'quit':
        break  # Exit the loop if user enters "quit"

    if guess == "brussels":
        print("Congratulations! You guessed correctly.")
        break #Exit the loop if the user guesses correctly

    print("incorrect. Try again.")







