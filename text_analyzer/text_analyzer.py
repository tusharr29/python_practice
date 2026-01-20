#Text Analyzer 

text = []

def enter_text():
    input_text = input("Enter Text to analyze: ")
    text.append(input_text)
    print("Text added successfully.")

def analyze_text():
    if not text:
        print("No text available to analyze. Please enter text first.")
        return

    combined_text = " ".join(text)
    word_count = len(combined_text.split())
    char_count = len(combined_text)
    sentence_count = combined_text.count('.') + combined_text.count('!') + combined_text.count('?')

    print(f"Text Analysis:")
    print(f"Total Words: {word_count}")
    print(f"Total Characters: {char_count}")
    print(f"Total Sentences: {sentence_count}")

def main():
    while True:
        print("\nText Analyzer Menu:")
        print("1. Enter Text")
        print("2. Analyze Text")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            enter_text()
        elif choice == '2':
            analyze_text()
        elif choice == '3':
            print("Exiting Text Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

