# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.
def main():
    while True:
        word = input("Enter a word (or 'quit' to exit): ")
        if word.lower() == 'quit':
            print("Exiting the program.")
            break
        else:
            print(f"The length of the word '{word}' is: {len(word)}")

if __name__ == "__main__":
    main()
