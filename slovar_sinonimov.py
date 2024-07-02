import sys


def main():
    n = int(input())
    d = dict()
    for i in range(n):
        s = input().split()
        d[s[0]] = s[1]
    word = input()
    if word in d.keys():
        print(d[word])
    elif word in d.values():
        for key in d:
            if d[key] == word:
                print(key)


if __name__ == '__main__':
    main()