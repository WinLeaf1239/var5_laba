from general import Parcer


def main():
    parcer = Parcer(
    'https://www.wildberries.by/catalog/0/search.aspx?page=1&sort=popular&search=%D0%BC%D1%8B%D1%88%D1%8C+%D0%B1%D0%B5%D1%81%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B4%D0%BD%D0%B0%D1%8F+logitech+g+pro+x+superlight&meta_charcs=true',
    'catalogCardLink--CgiYl'
    )

    parcer.getlinks()

if __name__ == '__main__':
    main()