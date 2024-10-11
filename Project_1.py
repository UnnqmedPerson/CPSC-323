#Jeffrey Wong CPSC-323
#Project 1 - Data Processing Project

import re
import keyword

input_file = 'testcases.txt'
output_file = 'output.txt'

# Python reserved keywords
keywords_set = set(keyword.kwlist)

# Regular expressions for literals and operators
literal_regex = r'\b\d+\b|".+?"|\'.+?\''  # Matches numbers and strings inside single or double quotes
operator_regex = r'[+\-*/%=<>&|^~()]+'


def remove_quotes_and_comments(input_path):
    with open(input_path, 'r') as f:
        text = f.read()

    # Find all text in triple quotes and remove them from consideration
    triple_quote = re.findall(r'\"\"\"(.*?)\"\"\"', text, flags=re.DOTALL)
    text = re.sub(r'\"\"\"(.*?)\"\"\"', '', text, flags=re.DOTALL)
    
    lines = text.splitlines()
    cleaned_lines = []
    comments = []

    for line in lines:
        # Finds and removes inline comments
        if '#' in line:
            comment = line.split('#', 1)[1].strip()
            comments.append(f'#{comment}')
            line = line.split('#', 1)[0].strip()
        cleaned_lines.append(line)

    cleaned_text = '\n'.join(cleaned_lines)
    comments_text = ', '.join(comments)  # Join comments into one string separated by commas
    
    return cleaned_text, comments_text, triple_quote

 
def remove_spaces(cleaned_text):
    return '\n'.join([' '.join(line.split()) for line in cleaned_text.splitlines() if line.strip()])


def tokenizer(cleaned_text, comments_text, triple_quote):
    token_list = {
        'keywords': set(),
        'identifiers': set(),
        'literals': set(),
        'operators': set(),
        'separators': set(),
        'comments': set(),
        'triple_quotes': set()
    }

    # Tokenize the cleaned text (excluding comments and triple-quoted text)
    tokens = re.findall(r'\b\w+\b|[^\w\s]', cleaned_text)
    
    for token in tokens:
        if token in keywords_set:
            token_list['keywords'].add(token)
        elif re.fullmatch(operator_regex, token):
            token_list['operators'].add(token)
        elif re.fullmatch(literal_regex, token):  # Check for literals (numbers, quoted strings)
            token_list['literals'].add(token)
        elif re.fullmatch(r'[:()]+', token):
            token_list['separators'].add(token)
        elif re.fullmatch(r'[a-zA-Z_]\w*', token):
            token_list['identifiers'].add(token)

    # Count comments as one token and include them as a string
    if comments_text:
        token_list['comments'].add(comments_text)

    # Count triple-quoted text as one token
    if triple_quote:
        token_list['triple_quotes'].add('Triple Quoted Block')

    return token_list


def write_file(output_path, cleaned_text, token_list):
    with open(output_path, 'w') as output_file:
        output_file.write("This is the text with excess spaces removed and comments/triple-quoted text stripped:\n")
        output_file.write(cleaned_text)
        output_file.write("\n\nToken Classification:\n")

        # Formats the output into the file
        for category, classified_tokens in token_list.items():
            if classified_tokens:
                formatted_tokens = ', '.join(sorted(classified_tokens))
                output_file.write(f"{category.capitalize()}: {formatted_tokens}\n")
    

# Run the process
cleaned_text, comments_text, triple_quote = remove_quotes_and_comments(input_file)
cleaned_text = remove_spaces(cleaned_text)
token_list = tokenizer(cleaned_text, comments_text, triple_quote)
write_file(output_file, cleaned_text, token_list)
