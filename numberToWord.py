import inflect

def number_to_words(number):
    # Create an inflect engine
    p = inflect.engine()

    # Convert the number to words
    words = p.number_to_words(number)

    return words

# Example usage
number = 1234
print(f"{number} in words is: {number_to_words(number)}")


