
# Osztály definiálása:
class FirstRepeatingCharacter:

    # Keressük meg az adott szövegben lévő első ismétlődő karaktert
    def findFirstRepeatingCharacter(self, text: str) -> str:

        # Ellenőrizzük a megadott szöveg hosszát:
        str_length = len(text.strip())
        if str_length == 0 or str_length == 1:
            raise ValueError("Kérem, adjon meg egy 1-nél hosszabb szövegrészt!")

        # Bontjuk a megadott szöveget karakterekre
        repeating_char = ""
        characters = [x for x in text]
        for idx, char in enumerate(characters):
            l = len(characters)
            if idx < (l - 1):
                next_item = characters[idx + 1]
                if next_item == char:
                    repeating_char = char

        return repeating_char

text = "Hello, world"
first_repeating_character = FirstRepeatingCharacter()
result = first_repeating_character.findFirstRepeatingCharacter(text)

if result != "":
    print("Az első ismétlődő karakter: " + result)
else:
    print("Nincs ismétlődő karakter.")
