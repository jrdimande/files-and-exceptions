filename = 'ian.txt'

try:
    with open(filename) as file_object:
        content = file_object.read()

except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist")
else:
    print(content)


