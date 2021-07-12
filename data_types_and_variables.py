# 1. You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days,
#  they love it), and Hercules (1 day, you don't know yet if they're going to like it). 
#If price for a movie per day is 3 dollars, how much will you have to pay?

num_movies_rented = 3
num_days_rented = 9
rental_price = 3
p_p_d = (num_movies_rented * rental_price)
total_price = p_p_d * num_days_rented
total_price

#2. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350.
#  How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

Google = 400
Amazon = 380
Facebook = 350

pay = (Google * 6 + Amazon * 4 + Facebook*10)
pay

#3. A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

is_premium_member = True
more_than_2_items = False
offer_still_good = True
offer_can_be_applied = offer_still_good and (more_than_2_items or is_premium_member)

#4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

username = 'codeup'
password = 'notastrongpassword'

password_is_long_enough = len(password) >= 5
username_is_short_enough = len(username) <= 20
username_and_password_are_different = username != password # returns True if they're different
username_has_spaces = username != username.strip()
password_has_spaces = password != password.strip()

username_is_good = username_is_short_enough and username_and_password_are_different and not username_has_spaces
password_is_good = password_is_long_enough and username_and_password_are_different and not password_has_spaces

credentials_are_good = username_is_good and password_is_good

print(username, password)
print("Password is long enough?", password_is_long_enough)
print("Username is short enough?", username_is_short_enough)
print("Username and password are different", username_and_password_are_different)
print("Username has spaces", username_has_spaces)
print("Password has spaces", password_has_spaces)
print("Username is good?", username_is_good)
print("Password is good?", password_is_good)
print("------")
print("Credentials are good?", credentials_are_good)


# Print with commas doesn't need to worry about data types, and puts a space between values.
print(True, "Blue", 72)
