def word_count(text):
    # Function to count words in the input text
    words = text.split()
    return len(words)

def main():
    # Main function to handle user input and display output

    # User input
    user_input = input("Enter a sentence or paragraph: ")

    # Check for empty input
    if not user_input.strip():
        print("Error: Empty input. Please enter a valid text.")
        return

    # Calculate word count using the word_count function
    count = word_count(user_input)

    # Display output
    print("\nWord Counter Result:")
    print(f"Input Text: '{user_input}'")
    print(f"Word Count: {count}")

if __name__ == "__main__":
    main()