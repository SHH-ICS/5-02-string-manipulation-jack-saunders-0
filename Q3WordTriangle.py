# Create a program that will prompt the user for a word, and return a 'word triangle'. For example, if the user types in the word "PYTHON", your program will output:
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON
def main():
    word = input("Enter a word: ")
    for i in range(1, len(word) + 1):
        print(word[:i])

if __name__ == "__main__":
    main()
