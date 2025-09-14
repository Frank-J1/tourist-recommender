import difflib

ALIASES = {
    "us": "united states",
    "usa": "united states",
    "u.s.": "united states",
    "u.s.a": "united states",
    "america": "united states",
}
from data import DESTINATIONS   # import our dictionary from data.py

def normalize(s: str) -> str:
    # trim, lowercase, collapse inner whitespace
    return " ".join(s.strip().lower().split())

def supported():
    # returns a list of all supported countries
    return [k.title() for k in sorted(DESTINATIONS.keys())]

def show_country(key: str):
    # prints all attractions for the chosen country
    print(f"\nTop places in {key.title()}:")
    for spot in DESTINATIONS[key]:
        print(f"- {spot['name']}: {spot['blurb']}")
    print()  # blank line for spacing

def find_best_country(key: str):
    if key in DESTINATIONS:
        return ("exact", key)
    
    if key in ALIASES:
        return ("alias", ALIASES[key])
    
    partial_hits = [k for k in DESTINATIONS.keys() if key and key in k]
    if partial_hits:
        return ("partial", partial_hits[0])
    
    fuzzy = difflib.get_close_matches(key, DESTINATIONS.keys(), n = 1, cutoff = 0.6)

    if fuzzy:
        return ("fuzzy", fuzzy[0])
    
    return ("none", None)


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
        else:
            status, target = find_best_country(key)
            if status in ("exact", "alias", "partial"):
                show_country(target)
                continue

            elif status == "fuzzy":
                print(f"No exact match for {raw}. Did you mean {target.title()} ?")
                continue
            
            else:
                print(f"No match for {raw}. Type list to see the supported countries")
                
        if key in DESTINATIONS:       # if we know this country
            show_country(key)
        else:                         # otherwise, no match
            print(f'No exact match for "{raw}". Try "list" to see supported countries.')

if __name__ == "__main__":
    main()
