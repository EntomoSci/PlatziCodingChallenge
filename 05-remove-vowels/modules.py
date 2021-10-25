import re


def stop():
    user_answer = input('Enter to continue ')


def remove_vowels(file_path):
    '''Function to create a new file without vowels from a text file passed by argument.'''

    print('\nStarting to create the file...\n')

    file_object = open(file_path, 'r')
    reading_file = file_object.readlines()
    vowels_regex = '[aeiouAEIOU]'

    file_without_vowels = open('without_vowels.txt', 'w')
    
    # print(reading_file)
    for line in reading_file:
        # line = line.strip()
        words = line.split()

        line_without_vowels = []

        for word in words:
            word_without_vowels = ''
            index = 0
            while index < len(word):
                if not re.match(vowels_regex, word[index]):
                    word_without_vowels += word[index]
                    # print('Regex match!\nword_without_vowels variable is: {}\n'.format(word_without_vowels))
                    # stop()
                index += 1
            line_without_vowels.append(word_without_vowels)
            # print('Ending word iteration!\nline_without_vowels variable is now: {}\n'.format(line_without_vowels))
            # stop()

        new_line = ' '.join(line_without_vowels)
        file_without_vowels.write(new_line)
        
        # print('Exit word array processing loop!\new_line variable is: {}\n'.format(new_line))
        # print('Proceding to write new line:\n\t"{}"\n'.format(new_line))
        # stop()

    print('\nThe file was successfully created.\n')
        

history = './history.txt'
remove_vowels(history)
new_file_object = open('./without_vowels.txt', 'r')
# reading_file_without_vowels = new_file_object.read()
print(new_file_object.read())
