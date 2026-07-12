import os


def generate_dictionary(name, year, number):
    words = []

    # Basic combinations
    words.append(name)
    words.append(name.lower())
    words.append(name.upper())

    # Name + year
    words.append(name + year)
    words.append(name.lower() + year)

    # Name + number
    words.append(name + number)
    words.append(name.lower() + number)

    # Symbol combinations
    symbols = ["@", "#", "!", "$"]

    for symbol in symbols:
        words.append(name + symbol)
        words.append(name + symbol + year)
        words.append(name.lower() + symbol + number)

    # Leetspeak examples
    leet_name = (
        name.lower()
        .replace("a", "@")
        .replace("e", "3")
        .replace("i", "1")
        .replace("o", "0")
    )

    words.append(leet_name)
    words.append(leet_name + year)

    # Remove duplicates
    words = list(set(words))

    # Create output folder
    os.makedirs("wordlists", exist_ok=True)

    # Save file
    with open("wordlists/generated.txt", "w") as file:
        for password in words:
            file.write(password + "\n")

    return words


if __name__ == "__main__":

    name = input("Enter name: ")
    year = input("Enter birth year: ")
    number = input("Enter favorite number: ")

    result = generate_dictionary(name, year, number)

    print("\nDictionary Generated Successfully!")
    print("Total Password Candidates:", len(result))
    print("Saved at: wordlists/generated.txt")