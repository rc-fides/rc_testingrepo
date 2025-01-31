from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()


lines = contents.splitlines()
learning_python = ""
for line in lines:
    learning_python += line.strip()
    learning_python.replace("Python", "Javascript")

print(learning_python)

