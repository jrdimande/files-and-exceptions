filepath = '/home/vboxuser/files-and-exceptions/txts/guest.txt'

name = input('Enter your name: ')

with open(filepath, 'w') as file_object:
    file_object.write(f'{name}\n')