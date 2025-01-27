from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()

# lines = contents.splitlines()
# for line in lines:
#     print(line)

# lines = contents.splitlines()
# pi_string = ""
# for line in lines:
#     pi_string += line.lstrip()

# print(f"{pi_string[:52]}")
# print(len(pi_string))


lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday in the form of MMDDYY: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday doesn't appear in the first million digits of pi!")