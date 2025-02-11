from pathlib import Path
new_name = ""

while True:
    name = input("What is your name: ")
    new_name += name + "\n"
    if name == "Roy":
        break

path = Path('guest_book.txt')
path.write_text(new_name)