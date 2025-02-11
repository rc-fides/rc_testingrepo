from pathlib import Path

name = input("Hello, nice to meet you. What is your name?: ")

path = Path('guest.txt')
path.write_text(name)