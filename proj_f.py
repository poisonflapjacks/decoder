import math
import random
from wonderwords import RandomWord

def is_perfect_square(num):

    sqrtt = math.sqrt(num)
    return sqrtt.is_integer()

def is_triangular(num):

    numb = int(num)
    return is_perfect_square(8 * numb + 1)

def decode_triangular():

    output_arr = []

    with open('encoded_message.txt', 'r') as File:
        
        for line in File:

            full_line = line.split()
            
            if is_triangular( int(full_line[0]) ):
                output_arr.append([ int(full_line[0]), full_line[1]])

    output_arr.sort()

    print(output_arr)

def create_fake_list(message):

    full_list = []
    full_fake_list = []
    z = 0

    message_as_list = message.split()
    message_len = len(message_as_list)

    for x in range(message_len):

        z = int(((x + 1)*(x + 2))/2)
        full_list.append([str(z), message_as_list[x]])

    for y in range(z):

        if (is_triangular(y+1)):
            added = full_list.pop(0)
            full_fake_list.append(added)

        else:
            RandW = RandomWord()
            full_fake_list.append([str(y+1), RandW.word()])

    return full_fake_list

#TODO: Fix scramble poriton
    # def scramble(file_size):

    #with open('encoded_message.txt', 'r+') as File:

       # for i in range( file_size/2 ):

        #    File.write(line)

def create_encoded_file(message):

    file_size = 0

    with open('encoded_message.txt', 'w') as File:

        full_fake_list = create_fake_list(message)
        file_size = len(full_fake_list)

        for i in range( file_size ):

            line = full_fake_list[i][0] + " " + full_fake_list[i][1] + "\n"
            File.write(line)

    #scramble(file_size)

def main():

    message = input("Enter your phrase: ")

    print(f"\nEntered: {message}\n")

    create_encoded_file(message)
    decode_triangular()

main()
