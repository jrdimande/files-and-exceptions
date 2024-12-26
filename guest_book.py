filepath = '/home/vboxuser/files-and-exceptions/txts/guest_book.txt'
flag = True


while flag:
    name = input('Enter your name: ')
    if name == '0':
        flag = False
    else:
        print(f'Hello {name.title()}')

        with open(filepath, 'a') as file_object:
            file_object.write(f'{name}\n')


