# 26,27 and 28 part is merged this file
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

# Arguments and parameters not the same thing, paramters is define a methods, in this case parameter is "name", but argument is recieveing the data like "Selcuk"
print("Start")
greet_user("Selcuk", "DINC")
# 28 Positional argument order is matter
greet_user(last_name="DINC", first_name="Selcuk") # this is a positional argument example
# Also if we use positional argument after keyword argument pytohn allows to use
greet_user("Selcuk", last_name="DINC")
# calc_cost(total=50, shipping=5, discount=0.1) # this is a keyword argument example
# Keyword arguments accurate code readability
print("Finish")