import re


def remove_vowels(file_path):
    '''Function to create a new file without vowels from a text file passed by argument.'''

    file_object = open(file_path, 'r')
    reading_file = file_object.readlines()
    vowels_regex = '[aeiouAEIOU]'

    file_without_vowels_name = input('Name of the new file: ')

    file_without_vowels = open('./files_without_vowels/{}.txt'.format(file_without_vowels_name), 'w')
    
    print('\nStarting to create the file...')

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
                index += 1

            line_without_vowels.append(word_without_vowels)

        line_without_vowels.append('\n')
        new_line = ' '.join(line_without_vowels)
        file_without_vowels.write(new_line)

    print('The file was successfully created!\n')
