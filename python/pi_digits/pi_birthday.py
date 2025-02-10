from pathlib import Path

path = Path(r"C:\Users\times\git\rc_testingrepo\python\pi_digits\pi_million_digits.txt")  # Example for Windows

contents = path.read_text()
lines = contents.splitlines()
pi_string = ""

for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday in the form of MMDDYY: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday doesn't appear in the first million digits of pi!")