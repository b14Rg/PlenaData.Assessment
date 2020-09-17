
def buildDictionary(word):
    char_count = {}
    for character in word:
        if character in char_count.keys():
            char_count[character] = char_count[character] + 1
        else:
            char_count[character] = 1
    return char_count

def sortDictionary(char_dict):
    char_dict = {k: v for k, v in sorted(char_dict.items(), key=lambda item: item[1])}
    return char_dict

def printNonrepeat(char_dict):
    print(f'  >{next(iter(char_dict))}')

def printResult(char_dict):
    output = ''
    for key in char_dict:
        for x in range(char_dict[key]):
            output += key
    print(f'  >{output}')

def processWord(word):
    char_dict = buildDictionary(word)
    char_dict = sortDictionary(char_dict)
    printNonrepeat(char_dict)
    printResult(char_dict)

def nonRepeat():
    print("Enter 'c' to quit")
    run = True
    while run:
        word = input().lower()
        if word == 'c':
            run = False
        else:
            processWord(word)

if __name__ == '__main__':
    nonRepeat()
