import phonenumbers
from phonenumbers import geocoder

while True:
    phone_number1 = phonenumbers.parse(input("Whats your number? "))

    print("\nYour phone numbers location:")
    print(geocoder.description_for_number(phone_number1, "pt"))

