def starts_with_vowel(string):
    if len(string) > 0:
        if string[0] in ["A", "E", "I", "O", "U"]:
            return True
    return False


def minion_game(string):
    kevin = 0
    stuart = 0
    for position in range(len(string)):
        if starts_with_vowel(string[position]) is True:
            kevin += len(string)-position
        else:
            stuart += len(string)-position
    if kevin > stuart:
        print(f'Kevin {kevin}')
    elif stuart > kevin:
        print(f'Stuart {stuart}')
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
