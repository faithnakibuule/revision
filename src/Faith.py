phone_number = input("In put your phone number please: ")
print(phone_number.split())
formated_phone_number = f"({phone_number[:3]}){phone_number[3:6]}-{phone_number[7:]}"
print(formated_phone_number)

if len(phone_number)<=10:
    print("valid phone number")
else:
    print("invalid phone number")
    