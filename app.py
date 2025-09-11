# app.py
from data import DESTINATIONS   # import our dictionary from data.py

def normalize(s: str) -> str:
    # takes whatever the user typed and makes it lowercase, no spaces
    return s.strip().lower()

def supported():
    # returns a comma-separated list of all supported countries
    return [k.title() for k in sorted(DESTINATIONS.keys())]

def show_country(key: str):
    # prints all attractions for the chosen country
    print(f"\nTop places in {key.title()}:")
    for spot in DESTINATIONS[key]:
        print(f"- {spot['name']}: {spot['blurb']}")
    print()  # blank line for spacing

def main():
    print("Welcome to TripTaster!")
    print("Type a country, 'list' to see options, or 'quit' to exit.")

    while True:  # keeps running until the user exits
        raw = input("> ")      # get user input
        key = normalize(raw)   # clean it up (e.g., ' Brazil ' → 'brazil')

        if key in ("quit", "exit"):   # exit option
            print("Goodbye! Safe travels.")
            break
        elif key == "list":             # show supported countries
            print("Supported countries:")
            for country in supported():
                print(f"- {country}")
            continue
        if key in DESTINATIONS:       # if we know this country
            show_country(key)
        else:                         # otherwise, no match
            print(f'No exact match for "{raw}". Try "list" to see supported countries.')

if __name__ == "__main__":
    main()
