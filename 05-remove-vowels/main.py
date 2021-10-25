# This Python program remove all the vowels of the text passed 
# by argument to the program. Idea based on the hebrew language.

from modules import remove_vowels


def run():
    welcome_message = open('./program_messages/welcome.txt', 'r')
    print(welcome_message.read())

    while True:
        file_path = input('Enter the file path: ')
        file_path = file_path.strip()
        try:
            remove_vowels(file_path)
        except:
            print('\nError, the path you entered do not exist.\nTry again\n')
            continue
        break

    print('\nAll done.\n')


if __name__ == '__main__':
    run()
