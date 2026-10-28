from general import Parcer, log
 
 
def main():
    log("Запуск парсера")
    parcer = Parcer(
    'https://www.wildberries.by/catalog/0/search.aspx?search=%D0%B8%D0%B3%D1%80%D0%BE%D0%B2%D0%B0%D1%8F+%D0%B1%D0%B5%D1%81%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B4%D0%BD%D0%B0%D1%8F+%D0%BC%D1%8B%D1%88%D1%8C+logitech+superlight+2',
    'catalogCardLink--CgiYl'
    )
    try:
        parcer.accept_cookie()
        log("accept_cookie")
        parcer.scroll()
        log("scroll")
        items = parcer.getlinks()
        log(f"getlinks, найдено товаров: {len(items)}")
        parcer.parse_and_save(items)

    except Exception as e:
        print(e)
    finally:
        parcer.close()
        log("close")
 
 
if __name__ == '__main__':
    main()
