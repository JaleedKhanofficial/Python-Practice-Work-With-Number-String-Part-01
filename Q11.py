# Step 11
# Print the value of the card_number_reversed variable to the console.

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[0:4]
    print(card_number_reversed)
    
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    print(translated_card_number)

    verify_card_number(translated_card_number)

main()