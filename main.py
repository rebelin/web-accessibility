def print_options(self, options):
    for i in range(len(options)):
        print(i + 1, options[i])
    print("Press ENTER at any time when done.")
    return valid_choice(len(options), input("Please enter an option number: "))

def valid_choice(length, num):
    if num == "":
        return
    try:
        int(num)
    except TypeError:
        num = valid_choice(length, input("Please enter the number associated with your desired action: "))
    else:
        if int(num) > length or int(num) <= 0:
            num = valid_choice(length, input("This is an invalid choice, please enter a number within range: "))
    finally:
        return num

def main():
    file = input("Enter (HTML) file name: ")
    x = Soup(file)
    clean = Cleaner(x)

    done = False
    while not done:
        print("What would you like to do?")
        i = int(print_options(questions))
        if i == 1:
            clean.quick_clean()
        elif i == 2:
            clean.add()
        elif i == 3:
            clean.replace()
        elif i == 4:
            clean.remove()
        elif i == 5:
            clean.whitelist()
        else:
            done = True
    print("A new file has been made with your changes. ")

main()
