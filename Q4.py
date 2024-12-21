# Step 4
# Defining the translation does not in itself translate the string. The translate method must be called on the string to be translated with the translation table as an argument:

# Example Code
# my_string = "tamperlot"
# translation_table = str.maketrans({'t': 'c', 'l': 'b'})
# translated_string = my_string.translate(translation_table)
# Create a variable called translated_card_number and assign it the result of calling the translate method on card_number with card_translation as an argument.

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})

    translated_card_number = card_number.translate(card_translation)
    print(translated_card_number)