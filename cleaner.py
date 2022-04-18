from soup import Soup

class Cleaner:
    def __init__(self, soup):
        self.soup = soup
        self.questions = ["Quick Clean", "Add", "Replace", "Remove", "Access Whitelist"]
        self.whitelist = self.soup.get_whitelist()

    def get_questions(self):
        return self.questions
        
    def quick_clean(self):
        print("Quick clean will replace inaccessible and non-semantic tags and remove empty tags.")
        i = input("Are you sure you want to quick clean? [Y/N] ")
        if i in ["Y", "y", "yes", "Yes"]:
            self.soup.auto_replace()
            self.soup.remove_empty_tags()
        return

    def add(self):
        print("What do you want to add?")
        add = ["Header", "Language declaration", "Bibliography", "Citation"]
        i = int(print_options(add))
        if i == 1:
            self.soup.add_header()
        elif i == 2:
            self.soup.add_lang()
        elif i == 3:
            self.soup.add_bib()
        elif i == 4:
            self.soup.add_cite()
        return

    def replace():


        return

    def remove(self):
        print("What do you want to remove?")
        rm = ["Specific Tag", "Tag-Specific Attribute", "All attributes", "View/edit whitelist"]
        i = int(print_options(rm))
        if i == 1:
            tag = input("What tag do you want to remove? (NOTE: This will remove all instances of the tag) ")
            self.soup.remove_tag(tag)
        elif i == 2:
            attr = input("What attribute do you want to remove? ")
            tag = input("Which tag is the attribute associated with? ")
            self.soup.remove_attr(tag, attr)
        elif i == 3:
            print("WARNING: This will remove ALL attributes from all tags, unless they are in your whitelist.")
            print("Tags currently in your whitelist: ")
            print_whitelist()
            a = input("Would you like to proceed? [Y/N] ")
            if a in ["y", "Y", "yes", "Yes"]:
                self.soup.remove_all_attrs_except(self.whitelist)
            else:
                a = input("View/edit whitelist? [Y/N] ")
                if a in ["y", "Y", "yes", "Yes"]:
                    self.whitelist()
        return

    def update_whitelist(self):
        self.whitelist = self.soup.get_whitelist()

    def print_whitelist(self):
        if len(self.whitelist) == 0:
            print("Your whitelist is empty.")
        else:
            for i in self.whitelist:
                print("- ", i)

    def whitelist(self):
        wq = ["View", "Add", "Remove"]

        done = False
        while not done:
            i = int(print_options(wq))
            if i == 1:
                print("Your current whitelist: ")
                self.print_whitelist()
            elif i == 2:
                a = input("What tag do you want to add? ")
                self.soup.add_to_whitelist(a)
                self.update_whitelist()
            elif i == 3:
                a = input("What do you want to remove? ")
                self.soup.remove_from_whitelist(a)
                self.update_whitelist()
            else:
                return

    def done(self):
        self.soup.make_file()
