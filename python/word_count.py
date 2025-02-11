from pathlib import Path

def count_words(filenames):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} doesn't exist.")
    else:
        #count the words
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ["siddhartha.txt", "alice.txt", "mobydick.txt"]
for filename in filenames:
    path = Path(filename)
    count_words(path)   