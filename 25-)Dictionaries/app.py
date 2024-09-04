'''
# Each key name is must be unique
# keys is Case sensitive
customer = {
    "name": "John Smith",
    "age": "30",
    "is_verified": True
}
# if ve use customer["birthdate"] , program doesnt work
# but we uses customer.get("birthdate") program return 'None' value and keep working
print(customer.get("birthdate", "Jan 1 1980"))
# for .get() function if first parameter doesnt match any key, second parameter returns
print(customer.get("name", "Jan 1 1980"))

customer["name"] = "Jack Smith"
#also uses add to dictinoary new key
customer["birthdate"] = "Sep 25 2002"
print(customer.get("name"))
print(customer.get("birthdate"))
'''

userNumbers = input("Phone: ")
i = 0
result = ""
digit_mapping = {
    "0": "zero ",
    "1": "one ",
    "2": "two ",
    "3": "three ",
    "4": "four ",
    "5": "five ",
    "6": "six ",
    "7": "seven ",
    "8": "eight ",
    "9": "nine "
}
# Version 1
while i < len(userNumbers):
    result += digit_mapping.get(f"{userNumbers[i]}", "- ")
    i += 1
print(result)
# Version 2, video based solution
output = ""
for ch in userNumbers:
    output += digit_mapping.get(ch, "!") + " "
print(output)