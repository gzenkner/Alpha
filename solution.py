import sys 
import re

# specify file path as path
# file_name = sys.argv[0]
path = sys.argv[1]
with open(path) as f:
    lines = f.readlines()


# split source_text and source_term, source_term always last in txt, strip whitespaces
source_text, search_term = lines[:-1], lines[-1].strip()

# loops through each linebreak
list = []
for i in range(len(source_text)):
    if search_term in source_text[i].lower():
        keep = re.sub(r'[^a-zA-Z]+', ' ', source_text[i]).strip()
        list.append('['+keep+']')
        print('['+keep+']')