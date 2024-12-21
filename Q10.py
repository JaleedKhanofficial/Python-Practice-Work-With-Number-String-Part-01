# Step 10
# You have accessed elements (characters) of a string before, using the index operator []. You can also use the index operator to access a range of characters in a string with string[start:stop:step]:

# Example Code
# my_string = 'camperbot'
# my_string[0:6] == 'camper' # True
# my_string[0:6:3] == 'cp' # True
# Where start is the starting index (inclusive), stop is the ending index (exclusive), and step is the amount of characters to skip over. If not specified, step is default to 1.

# Create a variable named card_number_reversed and assign it the value of the first 4 characters of card_number.

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[0:4]
    
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    print(translated_card_number)

    verify_card_number(translated_card_number)

main()