#change the phone numbers as per your need in lines 10,11,12 and 13


import phonenumbers


from phonenumbers import geocoder, carrier, timezone


phone_number1 = phonenumbers.parse("+12136574429")
phone_number2 = phonenumbers.parse("+916766543456")
phone_number3 = phonenumbers.parse("+862234567890")
phone_number4 = phonenumbers.parse("+919990157407")


#getting below info on above numbers
#Geoloc
#carrier originally owned a phone number
#timezone
print(phone_number1)
print(geocoder.description_for_number(phone_number1,'en'))
print(carrier.name_for_number(phone_number1, "en"))
print(timezone.time_zones_for_number(phone_number1))
print("-------------------------")

print(phone_number2)
print(geocoder.description_for_number(phone_number2,'en'))
print(carrier.name_for_number(phone_number2, "en"))
print(timezone.time_zones_for_number(phone_number2))
print("-------------------------")

print(phone_number3)
print(geocoder.description_for_number(phone_number3,'en'))
print(carrier.name_for_number(phone_number3, "en"))
print(timezone.time_zones_for_number(phone_number3))
print("-------------------------")

print(phone_number4)
print(geocoder.description_for_number(phone_number4,'en'))
print(carrier.name_for_number(phone_number4, "en"))
print(timezone.time_zones_for_number(phone_number4))
print("-------------------------")
