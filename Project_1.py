#Jeffrey Wong CPSC-323
#Project 1 - Data Processing Project

import re

input = 'testcases.txt' 
output = 'output.txt'  

def remove_spaces(input, output=None):
    # Open the file and read lines
    with open(input, 'r') as f:
        lines = f.readlines()

    # Removes the comments 
    no_comment = []
    for line in lines:
        remove_comment = line.split('#')[0].rstrip()
        no_comment.append(remove_comment)

    # Remove excess spaces for each line while keeping line breaks intact
    no_excess_space = [' '.join(line.split()) for line in no_comment if line.strip()]

    # Join the cleaned lines with '\n' to keep the original format
    no_excess_space = '\n'.join(no_excess_space)

    # Write to the output file
    with open(output, 'w') as output_file:
        output_file.write("This is the text with excess spaces removed\n")
        output_file.write(no_excess_space)
    print(f"Cleaned text written to {output}")

    def token_counter(input):
        tokens = []
        for line in lines:
            if line.split() == '#':
                tokens.append('#')


        print(tokens)



remove_spaces(input, output)
