# Varying arguments
def wish(*names, message):
    for name in names:
        print(f"{message}, {name}")


wish('Tom', "Jack", "Joe", message = 'Hello')
wish('Tom', "Jack", message = 'Hi')


