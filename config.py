# -*- coding: utf-8 -*-

from classes import Day
__author__ = 'TTChangeTheWorld'
def get_config():
    result = dict()
    result["parallel_name"] = "C'"
    result["month"] = "Июнь"
    result["year"] = "2015"
    result["usefull_links"] = [
        ("Памятка по PEP8", ""),
        ("Python cheatsheet", ""),
        ("Еще что-то", ""),
        ("Еще что-то", ""),
    ]
    result["additional_info"] = [
        "Завтра олимпиада. Не забудьте найти себе команду."
    ]
    result["days"] = reversed([
        Day("День 1: Вступление",
            [
                ("Условия", "https://ejudge.lksh.ru/archive/2014/08/Cpy/01/problems.pdf"),
                ("Вход", "https://ejudge.lksh.ru/cgi-bin/new-client?contest_id=21501&locale_id=1"),
                ("Таблица результатов", "https://ejudge.lksh.ru/ejudge/standings/021501.html"),
                ("Словарь", "https://ejudge.lksh.ru/archive/2014/08/Cpy/01/Словарь.pdf")
            ]),
        Day("День 2: Продолжение",
            [
                ("Условия", "https://ejudge.lksh.ru/archive/2014/08/Cpy/01/problems.pdf"),
                ("Вход", "https://ejudge.lksh.ru/cgi-bin/new-client?contest_id=21501&locale_id=1"),
                ("Таблица результатов", "https://ejudge.lksh.ru/ejudge/standings/021501.html"),
                ("Словарь", "https://ejudge.lksh.ru/archive/2014/08/Cpy/01/Словарь.pdf")
            ]),
        Day("День 3: Уже почти конец",
            [
                ("Условия", "https://ejudge.lksh.ru/archive/2014/08/Cpy/01/problems.pdf"),
                ("Вход", "https://ejudge.lksh.ru/cgi-bin/new-client?contest_id=21501&locale_id=1"),
                ("Таблица результатов", "https://ejudge.lksh.ru/ejudge/standings/021501.html"),
                ("Словарь", "https://ejudge.lksh.ru/archive/2014/08/Cpy/01/Словарь.pdf")
            ]),
        Day("День 4: Зачет",
            [
                ("Условия", "https://ejudge.lksh.ru/archive/2014/08/Cpy/01/problems.pdf"),
                ("Вход", "https://ejudge.lksh.ru/cgi-bin/new-client?contest_id=21501&locale_id=1"),
                ("Таблица результатов", "https://ejudge.lksh.ru/ejudge/standings/021501.html"),
                ("Словарь", "https://ejudge.lksh.ru/archive/2014/08/Cpy/01/Словарь.pdf"),
                ("Еще что-то странное", "https://ejudge.lksh.ru/archive/2014/08/Cpy/01/Словарь.pdf")
            ])
    ])
    return result
