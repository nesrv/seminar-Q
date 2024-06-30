# Shuffle the letters of a stri

import random
def shuffle_string(string):
    # Convert the string to a list of characters
    char_list = list(string)
    
    # Shuffle the list of characters
    random.shuffle(char_list)
    
    # Convert the shuffled list back to a string
    shuffled_string = ''.join(char_list)
    
    return shuffled_string



    