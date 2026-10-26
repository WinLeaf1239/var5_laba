from general import Parcer


def main():
    parcer = Parcer(
    'https://www.wildberries.by/catalog/0/search.aspx?search=%D0%B8%D0%B3%D1%80%D0%BE%D0%B2%D0%B0%D1%8F+%D0%B1%D0%B5%D1%81%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B4%D0%BD%D0%B0%D1%8F+%D0%BC%D1%8B%D1%88%D1%8C+logitech+superlight+2',
    'catalogCardLink--CgiYl'
    )
    try:
        parcer.accept_cookie()
        parcer.scroll()
        parcer.getlinks()
    finally:
        parcer.close()
                                                                           
if __name__ == '__main__':
    main()

#mo-button_view_fillLight mo-button_colors_neutral