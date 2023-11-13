define anton = Character('Антон', color="#0004ff")
define mother = Character('Мать', color="#c8ffc8")

label start:
    scene bg room shadow
    
    show anton:
        xalign 0.2 yalign 1.0 zoom 1.1

    anton "Привет, мам. Я вчера подумал, очень бы хотелось посетить концерт Дроы. Ну знаешь, в каждом утюге сейчас поет."

    anton "Она выступает в июле, билетов уже почти не осталось. Можешь помочь с деньгами на билет?"

    show anton:
        xalign 0.2 yalign 1.0 zoom 1.0
    with Dissolve(0.35)

    show mother:
        xalign 0.7 yalign 1.0 zoom 1.1
    with Dissolve(0.35)
    
    mother "Антон, мы уже обсуждали твои траты, и мы не можем себе позволить тратить деньги на всякую ерунду."

    mother "Слышал, Настин сын, Егор, помнишь кстати его? Он уже устроился на лето и работает менеджером зала в Точке вкуса."

    anton "цццц"

    mother "А Маша? Та вообще ипотеки выдает! Почему бы тебе не попробовать поработать как они?"

    mother "Ты должен быть более ответственным в управлении своим бюджетом."

    show anton:
        xalign 0.2 yalign 1.0 zoom 1.1
    with Dissolve(0.35)

    show mother:
        xalign 0.7 yalign 1.0 zoom 0.95
    with Dissolve(0.35)

    anton "Я знаю мааам, я стараюсь быть ответственным, но иногда же можно исключение сделать. Не каждый день можно пойти на концерт своей любимой исполнительницы."
    
    show anton:
        xalign 0.2 yalign 1.0 zoom 1.0
    with Dissolve(0.35)

    show mother:
        xalign 0.7 yalign 1.0 zoom 1.1
    with Dissolve(0.35)

    mother "Тоша, мы с отцом ценим твою работу, но мы хотим, чтобы ты научился управлять своими финансами."

    show anton:
        xalign 0.2 yalign 1.0 zoom 1.1
    with Dissolve(0.35)

    show mother:
        xalign 0.7 yalign 1.0 zoom 0.95
    with Dissolve(0.35)

    anton "Океей мам."

label computer:
    scene computer

    anton "Ыфыыыф"

    scene computer_with_fist
    with vpunch

    pause 1.0

    scene computer

    anton "И все-таки."

    anton "Нет, это бред. Рынок перенасыщен, кому я такой красивый нужен без опыта - хах - да никому!"

    anton "Мда, но с чего-то все же нужно начинать."

    scene computer_with_yandex_search

    anton "Так, Ок Яндекс, \"как вка-тить-ся в ай-ти\". Эээ. По-другому. \"какая професс-сия по-дой-дет но-вич-ку для вхо-да в ай-ти вопрос\"."

    scene computer_with_yandex_results

    anton "Угу, так учить языки зочется не особо, французского хватает, биг дата, юнит тесты агааа...."

    anton "Оп-па, тестик"