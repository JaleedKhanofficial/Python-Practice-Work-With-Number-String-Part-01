# Step 8
# Within your main function, call the verify_card_number function and pass in the translated_card_number variable as an argument.

def verify_card_number(card_number): 
    pass

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    print(translated_card_number)
    verify_card_number(translated_card_number)