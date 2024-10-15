import nltk
import re

f = open('InputProgForPythonCode.c', 'r')
program = f.read()

count = 0
Identifiers_Output = []
Keywords_Output = []
Symbols_Output = []
Operators_Output = []
Numerals_Output = []
Headers_Output = []
Comments_Output = []

def remove_Spaces(program):
    scanned_Program = []
    for line in prog:
        if (line.strip() != ''):
            scanned_Program.append(line.strip())
    return scanned_Program

def detect_comments(lines):
    comments = []

    for line in lines:
        if re.search(r"\/\/", line):
            comments.append("Single-line Comment is detected\n")
        elif re.search(r"\/\*", line):
            comments.append("Multi-line Comment is detected\n")
        else:
            #comments.append("No Comment")
            continue

    return comments

def remove_Comments(program):
    program_Multi_Comments_Removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", program)
    program_Single_Comments_Removed = re.sub("//.*", "", program_Multi_Comments_Removed)
    program_Comments_removed = program_Single_Comments_Removed
    
    return program_Comments_removed

RE_Keywords = r"include|break|case|char|const|continue|default|do|double|else|main|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|string|class|struc|auto"
RE_Operators = r"[+\-*/%=<>\-]+"
RE_Numerals = r"^(\d+)$"
RE_Special_Characters = r"[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
RE_Identifiers = r"^[a-zA-Z_]+[a-zA-Z0-9_]*"
RE_Headers = r"([a-zA-Z]+\.[h])"

attribute_values = {'+': 'addition','-': 'subtraction','*': 'multiplication','/': 'division','%': 'remainder','=': 'assignment','<=': 'less than or equal', '>=': 'greater than or equal','++': 'increment','--': 'decrement','{': 'left curly brace','}': 'right curly brace',';': 'semicolon', ',': 'comma','(': 'opening brace',')': 'closing brace','>': 'greater than','<': 'less than','++': 'increament','--': 'decreament','#': 'hash sign'}

program_Comments_removed = remove_Comments(program)
prog = program_Comments_removed.split('\n')

scanned_Prog = remove_Spaces(prog)
scanned_Program = '\n'.join([str(elem) for elem in scanned_Prog])
scanned_Program_lines = scanned_Program.split('\n')
match_counter = 0
Source_Code=[]

for line in scanned_Program_lines:
        Source_Code.append(line)

display_counter = 0

file_path = 'InputProgForPythonCode.c'
with open(file_path, 'r') as f:
    program_lines = f.readlines()

comments = detect_comments(program_lines)

for comment in comments:
    print(comment)

if comments and comments[0] == "Multi-line Comment is detected" and comments[-1] == "Multi-line Comment is detected":
    print("The entire code is commented out.")
else:
    for line in Source_Code:
        count = count + 1

        if(line.startswith("#include")):
            tokens = nltk.word_tokenize(line)
        else:
            tokens = nltk.wordpunct_tokenize(line)

        for token in tokens:
            if(re.findall(RE_Keywords, token)):
                Keywords_Output.append(token)
            elif(re.findall(RE_Headers,token)):
                Headers_Output.append(token)
            elif(re.findall(RE_Operators, token)):
                Operators_Output.append(token)
            elif(re.findall(RE_Numerals,token)):
                Numerals_Output.append(token)
            elif (re.findall(RE_Special_Characters, token)):
                Symbols_Output.append(token)
            elif (re.findall(RE_Identifiers, token)):
                Identifiers_Output.append(token)

        for identifier in Identifiers_Output:
            attribute_values[identifier] = 'pointer to symbol table entry'

        for number in Numerals_Output:
            attribute_values[number] = '\tconstant'

        for keyword in Keywords_Output:
            attribute_values[keyword] = '\t-'
        
        for headers in Headers_Output:
            attribute_values[headers] = '\t-'

    print("\nLexemes\t\t|\tToken Names\t\t|\tAttribute Values ")
    print("--------------------------------------------------------------------------------------")
    for token, identifier in zip(Keywords_Output + Headers_Output + Symbols_Output + Operators_Output + Numerals_Output + Identifiers_Output, ["Keyword"] * len(Keywords_Output) + ["Header"] * len(Headers_Output) + ["Special Symbol"] * len(Symbols_Output) + ["Operator"] * len(Operators_Output) + ["Number"] * len(Numerals_Output) + ["Identifier"] * len(Identifiers_Output)):
        attribute = attribute_values.get(token, '')
        print(f"{token}\t\t\t{identifier}\t\t\t{attribute}")
        print("______________________________________________________________________________________")
    print("\n")
