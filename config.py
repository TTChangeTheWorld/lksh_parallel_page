# -*- coding: utf-8 -*-

from classes import Day
__author__ = 'TTChangeTheWorld'


def get_config():
    config = {
        "parallel_name" : "C'",
        "month" : "Июнь",
        "year" : "2015",

        "usefull_links" : [
            ("Памятка по PEP8", ""),
            ("Python cheatsheet", ""),
            ("Еще что-то", ""),
            ("Еще что-то", ""),
        ],

        "additional_info" : [
            "Завтра олимпиада. Не забудьте найти себе команду."
        ],

        "dictionary_shown_tags" : [
            "день 1",
            "день 2",
            "день 3",
            "день 4"
        ]
    }

    config["days"] = reversed([
        Day("День 1: Вступление",
            [
                ("Условия", "https://ejudge.lksh.ru/archive/2014/08/Cpy/01/problems.pdf"),
                ("Вход", "https://ejudge.lksh.ru/cgi-bin/new-client?contest_id=21501&locale_id=1"),
                ("Таблица результатов", "https://ejudge.lksh.ru/ejudge/standings/021501.html"),
            ]),
        Day("День 2: Продолжение",
            [
                ("Условия", "https://ejudge.lksh.ru/archive/2014/08/Cpy/01/problems.pdf"),
                ("Вход", "https://ejudge.lksh.ru/cgi-bin/new-client?contest_id=21501&locale_id=1"),
                ("Таблица результатов", "https://ejudge.lksh.ru/ejudge/standings/021501.html"),
            ]),
        Day("День 3: Уже почти конец",
            [
                ("Условия", "https://ejudge.lksh.ru/archive/2014/08/Cpy/01/problems.pdf"),
                ("Вход", "https://ejudge.lksh.ru/cgi-bin/new-client?contest_id=21501&locale_id=1"),
                ("Таблица результатов", "https://ejudge.lksh.ru/ejudge/standings/021501.html"),
            ]),
        Day("День 4: Зачет",
            [
                ("Условия", "https://ejudge.lksh.ru/archive/2014/08/Cpy/01/problems.pdf"),
                ("Вход", "https://ejudge.lksh.ru/cgi-bin/new-client?contest_id=21501&locale_id=1"),
                ("Таблица результатов", "https://ejudge.lksh.ru/ejudge/standings/021501.html"),
                ("Еще что-то странное", "https://ejudge.lksh.ru/archive/2014/08/Cpy/01/Словарь.pdf")
            ])
    ])
    return config
