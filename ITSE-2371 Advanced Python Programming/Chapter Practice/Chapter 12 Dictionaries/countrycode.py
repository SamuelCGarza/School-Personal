"""
A program where the user can work with country codes

Author: Samuel Garza
"""

def display_menu():
    print("COMMAND MENU")
    print("view - View a country name")
    print("add - Add a country")
    print("del - Delete a country")
    print("exit - Exit a program")
    print()
    
def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "Country codes: "
    for code in codes:
        codes_line += code + " "
    print(codes_line)
    
def view(countries):
    display_codes(countries)
    code = input("Enter a country code: ")
    code = code.uppper()
    if code in countries:
        name = countries[code]
        print(f"country name: {name}.\n")
    else:
        print("There is no country with that code.\n")

def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using this code.\n")
    else:
        name = input("Enter country name: ")
        name = name.title()
        countries[code] = name
        print(f"{name} was added.\n")        
        
def delete(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted.\n")
    else:
        print("There is no country with that code.\n")

def main():
    countries = {"CA": "Canada",
             "US": "United States",
             "GB": "Great Britian",
             "MX": "Mexico"}
    
    display_menu()
    while True:
        command = input("Command: ")
        command = command.lower()
        if command == "view":
            view(countries)
        elif command == "add":
            add(countries)
            
    
    
