from pathlib import Path

path = Path(r"C:/Users/times/git/rc_testingrepo/python/learning_python.txt")
contents = path.read_text()

#test 1
for line in contents.splitlines():
    print(line)

# #test 2
# for line in lines:
#     line.replace("Python", "Javascript")
#     file_string += line + "\n"
# print(file_string)
    