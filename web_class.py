from bs4 import BeautifulSoup
import unicodedata

class Web:
    def __init__(self, file_name, whitelist = []):
        self.file = file_name
        self.index = file_name.rfind(".htm")
        self.new_file = self.file[:self.index] + "_remediated" + self.file[self.index:]
        self.whitelist = whitelist
        try:
            with open(file_name, "r", encoding = "utf-8") as f:
                txt = f.read()
                self.soup = BeautifulSoup(txt, "html.parser")
        except:
            print("Invalid file, please enter an htm(l) file")
        # self.tags = self.soup.find_all(True)

    def auto_replace(self):
        """
        This function replaces tags with accessible versions of those tags
        The replace_list.txt file follows this format:
            First column (index 0) = inaccessible tag
            Second column (index 1) = accessible tag
        """
        with open("replace_list.txt", "r") as f:
            for line in f.readlines():
                split = line.split()
                new_tag = self.soup.new_tag(split[1])
                for tag in self.soup.find_all(split[0]):
                    s = tag.replace_with(new_tag)
                    new_tag.string = s.string
                    self.whitelist.append(new_tag.name)

    def auto_span_style(self, tag = "span", attr = "style"):
        for t in self.soup.find_all(tag):
            if t.has_attr(attr):
                if "bold" in t[attr]:
                    tag = "strong"
                if "italic" in t[attr]:
                    tag = "em"
                new_tag = self.soup.new_tag(tag)
                s = t.replace_with(new_tag)
                new_tag.string = s.get_text()
                self.whitelist.append(new_tag.name)

    def remove_tag(self, tag):
        for t in self.soup.select(tag):
            t.unwrap()

    def replaceTag(self, old, tag):
        self.soup.old.replace_with(tag)

    def remove_specific_attr(self, tag, attr):
        for t in self.soup(tag):
            del t[attr]

    def remove_all_attrs_except(self, lst):
        self.whitelist.append(lst)
        tag_list = self.soup.findAll(lambda tag: len(tag.attrs) > 0)
        for t in tag_list:
            if t.name not in self.whitelist:
                keys = list(t.attrs.keys())
                while len(t.attrs) > 0:
                    del t[keys[0]]
                    keys = keys[1:]

    def deep_clean(self):
        tag_list = self.soup.findAll(lambda tag: not tag.contents and not tag.name == 'br' )
        for t in tag_list:
            t.decompose()


    # # remove all attributes
    # def _remove_all_attrs(soup):
    #     for tag in soup.find_all(True):
    #         tag.attrs = {}
    #     return soup
    #
    # # remove all attributes except some tags
    # def _remove_all_attrs_except(soup):
    #     whitelist = ['a','img']
    #     for tag in soup.find_all(True):
    #         if tag.name not in whitelist:
    #             tag.attrs = {}
    #     return soup
    #
    # # remove all attributes except some tags(only saving ['href','src'] attr)
    # def _remove_all_attrs_except_saving(soup):
    #     whitelist = ['a','img']
    #     for tag in soup.find_all(True):
    #         if tag.name not in whitelist:
    #             tag.attrs = {}
    #         else:
    #             attrs = dict(tag.attrs)
    #             for attr in attrs:
    #                 if attr not in ['src','href']:
    #                     del tag.attrs[attr]
    #     return soup
    def make_file(self):
        with open(self.new_file, "w") as f:
            f.write(str(self.soup))
