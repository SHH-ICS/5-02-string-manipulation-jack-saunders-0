# Create a program that will accept a word and output the word one letter at a time in reverse.
def main():
    word = input("Enter a word: ")
    for letter in reversed(word):
        print(letter)

if __name__ == "__main__":
    main()
