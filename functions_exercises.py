#1.Define a function named is_two. It should accept one input and return True if the passed input is 
#either the number or the string 2, False otherwise.
def is_two(n):
    result = n
    if result == 2:
        return True
    elif result == '2':
        return True
    else: 
        return False
     
is_two(2)

#2 Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(n):
    vowel = n
    if vowel in ("a","e","i","o","u"):
        return True

    else:
        return False
is_vowel('b')
#3 Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(n):
    consonant = n
    if is_vowel(consonant)==True:
        return False
    else:
        return True
is_consonant('b')
#4 Define a function that accepts a string that is a word. The function should capitalize the first letter 
# he word if the word starts with a consonant.
def cap_consonant(n):
    word = n
    first_char=word[0]
    print(first_char)
    if is_consonant(first_char)== True:
        new_word=word[0].upper()+word[1:]
        print(new_word)
        
    
cap_consonant('hello')
#5Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and 
# the bill total, and return the amount to tip.
def calculate_tip():
    tip =input('Please enter the tip percent you would like to leave')
    print(tip)
    bill_total = input('Please enter your bill total')
    print(bill_total)

    tip_perc = (float(tip) * .001) * (float(bill_total))
    tip_amount = (float(tip_perc) / .1)
    tip_format = "{:.2f}".format(tip_amount)

    print(f"With a {tip}% tip for a total bill of ${bill_total} your tip amount will be: ${tip_format}")

#6 Define a function named apply_discount. It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.
#def appply_discount():
discount =input('Please enter the discount percentage')
print(discount)
original_price = input('Please enter the original price')
print(original_price)

discount_perc = (float(discount) * .001) * (float(original_price))
discount_amount = (float(discount_perc) / .1)
discount_format = "{:.2f}".format(discount_amount)
sale_price = (float(original_price)) - (float(discount_format))
sale_price_format = "{:.2f}".format(sale_price)

print(f""" {discount}% off the regular price of {original_price} is {discount_format}. The sale price will be ${sale_price_format}.""")
#7 Define a function named handle_commas. It should accept a string that is a number that contains 
# commas in it as input, and return a number as output.
#def handle_commas():
n = input('enter your number')   
number = n
no_commas =","
for comma in no_commas:
    number = number.replace(comma, "")
    print(int(number))
    print(type(number))
#8 Define a function named get_letter_grade. It should accept a number and return the letter
#  grade associated with that number (A-F).

#9 Define a function named remove_vowels that accepts a string and returns a string with all the vowels 
# removed.

#10 Define a function named normalize_name. It should accept a string and return a valid python i
# dentifier, that is:

#anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores
