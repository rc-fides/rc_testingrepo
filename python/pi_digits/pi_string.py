from pathlib import Path

#standard pi_string file (just read through pi_digits.txt)

#relearn why path is showing up as "U" / unmarked and why I need an absolute path -- OVER using standard path 
# path = Path("C:/Users/times/git/rc_testingrepo/python/pi_digits/pi_digits.txt")
# contents = path.read_text()
# pi_string = ""

# lines = contents.splitlines()
# for line in lines:
#     pi_string += line

# print(pi_string)
# print(len(pi_string))

#pi to a million digits
path = Path("C:/Users/times/git/rc_testingrepo/python/pi_digits/pi_million_digits.txt")
contents = path.read_text()
pi_string = ""

lines = contents.splitlines()
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}")
print(len(pi_string))