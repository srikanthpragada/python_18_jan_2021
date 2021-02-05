# Stack operations
data = []

while True:
    # Menu
    print("1. Push")
    print("2. Pop")
    print("3. Length")
    print("4. Exit")
    choice = int(input("Enter Choice [1-4]: "))
    if choice == 4:
        break

    if choice == 1:
        value = int(input("Enter value :"))
        data.append(value)  # Pushing
    elif choice == 2:
        print('Pop value = ', data.pop())
    else:
        print("Length = ", len(data))

print("Thank You!")