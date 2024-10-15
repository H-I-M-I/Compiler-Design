def main():
    keywords = ["int", "main", "float", "break", "long", "char", "for", "if", "switch", "else", "while", "return", "double", "const", "struct", "typedef", "case", "enum"]

    while True:
        # s = input("Enter any string: ")
        file_path = 'InputProgForPythonCode.c'
        with open(file_path, 'r') as f:
            s = f.readlines()

        if s.lower() == 'exit':
            print("Exiting the program.")
            break

        key = 0

        for keyword in keywords:
            if compare_strings(s, keyword):
                key = 1
                break

        if key == 1:
            print(s, "is a keyword.")
        else:
            if s.startswith(' '):
                print(s, "is not a valid identifier. Reason: Starts with a space.")
            elif ' ' in s:
                print(s, "is not a valid identifier. Reason: Contains space(s).")
            elif (alphabet(s[0]) or s[0] == '_'):
                flag = 0
                for i in range(1, len(s)):
                    if not (alphabet(s[i]) or number(s[i]) or s[i] == '_'):
                        flag = 1
                        break
                if flag == 1:
                    print(s, "is not a valid identifier. Reason: Invalid character(s) detected.")
                else:
                    print(s, "is a valid identifier.")
            else:
                print(s, "is not a valid identifier. Reason: Starts with an invalid character.")

def compare_strings(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def alphabet(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z')
     
def number(c):
    return '0' <= c <= '9'

if __name__ == "__main__":
    main()


