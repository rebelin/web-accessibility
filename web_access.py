from soup import Soup

def main():
    file = "../tests/rba06-sb4converted.htm"

    x = Soup(file)
    print(x.find_specials())

    # x.auto_replace()
    # x.auto_span_style()
    # x.remove_all_attrs_except(["href","li"])
    # x.remove_tag("span")
    # x.deep_clean()
    # x.make_file()

main()
# only keep classes that are made with css
