f = open("test.txt")
f_lines = f.readlines()
for l in f_lines:
    print(l)

def count_words():
    name = input("Enter the file name: ")
    f = open(name, "r")
    f_lines = f.readlines()
    total_words = 0
    for l in f_lines:
        words = l.split()
        total_words = total_words + len(words)
    print(total_words)


count_words()