from pathlib import Path

path = Path(r"C:/Users/times/git/rc_testingrepo/python/learning_python.txt")
contents = path.read_text()
lines = contents.splitlines()
file_string = ""

#test 1
for line in lines:
    print(line)

#test 2
for line in lines:
    file_string += line + "\n"
print(file_string)
