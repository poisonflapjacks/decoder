# Decoder Project

# Summary:
For this project the goal is to create a encoder/decoder in python. Users should be able to input a string of their choice. The deliverables should be an output to the console of the original message. The big take away is that during the inbetween steps, the code stores the original message in an encoded text file. The encoding will separate each word on it's own line and scramble the order so that if the text file was viewed before encoding, the input message would be indecipherable. 

# Methodology:
The basis of this project was that during an interview recently I was given the task of: Given a text file where input is in the form 

*image*

Create a decoder that rearranges the words in the files in order, then arrange the words in a pyramid pattern. The final message would be the last word in each row of the pyramid. This pattern was found to be a pattern of Triangular Numbers. My thought for this project was to expand on the original question and create the encoder portion as well. 

Prompt: The project starts by asking the user to input their phrase that they would like to be encoded. After this, the phrase is returned to the user and sent to be encoded. 

Encoder: All functions relevant to the encoder start with the call within prompt to the function create_encoded_file(). Within the create function, the encoded_message.txt is created as a writeable file. From here, the create_fake_list() function is called. This function creates two empty list and init. The first empty list, message_as_list, takes the user's input message and splits to a python readable list. The length of this list is taken for the range of the next for loop. Within the for loop, the input message is iterated through and each word is assigned its relevant triangular number. 

*image*

From here, the full_fake_list is expanded upon. If the location is a triangular value, our ful_list is popped. If it is not a triangular value, a random word from the wonderwords library is pulled. 

Decoder: 

# Tools:
Python 3.12, Math Library, WonderWords Library
Designed in PyCharm Community Edition

# Results:
