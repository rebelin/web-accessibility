from soup import Soup

def print_options(questions):
    print("What would you like to do?")
    for i in range(len(questions)):
        print(i + 1, questions[i])
    return input("Please enter an option number: ")

def auto_clean():
    return

def add():
    print("What do you want to add?")
    add = ["Bibliography", "Citation", "Header"]
    print_options(add)

    return

def replace():

    return

def remove():
    print("What do you want to remove?")
    rm = ["Tag", "Attribute", "Edit whitelist"]
    print_options(rm)

    return

def whitelist(x):
    wq = ["View", "Add", "Remove", "Done"]

    done = False
    while not done:
        i = print_options(wq)
        if i == 1:
            print("Your current whitelist:")
            x.print_whitelist()
        elif i == 2:
            a = input("What tag do you want to add?")
            x.add_to_whitelist(a)
        elif i == 3:
            a = input("What do you want to remove?")
            x.remove_from_whitelist(a)
        else:
            done = True

def main():
    file = input("Enter (HTML) file name: ")
    x = Soup(file)
    questions = ["Auto-Clean", "Add", "Replace", "Remove", "Access whitelist", "Done"]

    done = False
    while not done:
        i = print_options(questions)

        if i == 1:
            auto_clean(x)
        elif i == 2:
            add(x)
        elif i == 3:
            replace(x)
        elif i == 4:
            remove(x)
        elif i == 5:
            whitelist(x)
        else:
            done = True
