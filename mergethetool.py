def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        genline = string[i:i+k]

        process = ""
        for i in genline:
            if i not in process:
                process += i
        print(process)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
