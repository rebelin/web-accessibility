from web_class import Web

def main():
    # file = input("Enter (HTML) file name: ")
    file = "rba06-sb4converted.htm"

    x = Web(file)
    x.auto_replace()
    x.auto_span_style()
    x.remove_all_attrs_except(["href","li"])
    x.remove_tag("span")
    x.deep_clean()
    x.make_file()

main()
