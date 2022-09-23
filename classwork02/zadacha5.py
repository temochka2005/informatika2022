with open('input.txt') as f:
    for text in reversed(f.readlines()):
        print(text.rstrip()[len(text)-1::-1])