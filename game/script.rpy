﻿label start:
    scene bg room shadow
    
    show anton:
        xalign 0.2 yalign 1.0 zoom 1.1

    anton "Привет, мам. Я вчера подумал, очень бы хотелось посетить концерт Дроы. Ну знаешь, в каждом утюге сейчас поет."

    anton "Она выступает в июле, билетов уже почти не осталось. Можешь помочь с деньгами на билет?"

    show anton:
        xalign 0.2 yalign 1.0 zoom 1.0
    with Dissolve(0.35)

    show mother:
        xalign 0.8 yalign 1.0 zoom 1.1
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
        xalign 0.8 yalign 1.0 zoom 1.0
    with Dissolve(0.35)

    anton "Я знаю мааам, я стараюсь быть ответственным, но иногда же можно исключение сделать. Не каждый день можно пойти на концерт своей любимой исполнительницы."
    
    show anton:
        xalign 0.2 yalign 1.0 zoom 1.0
    with Dissolve(0.35)

    show mother:
        xalign 0.8 yalign 1.0 zoom 1.1
    with Dissolve(0.35)

    mother "Тоша, мы с отцом ценим твою работу, но мы хотим, чтобы ты научился управлять своими финансами."

    show anton:
        xalign 0.2 yalign 1.0 zoom 1.1
    with Dissolve(0.35)

    show mother:
        xalign 0.8 yalign 1.0 zoom 1.0
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

    jump educationTest

label messenger:
    scene messenger

    show anton:
        xalign 0.1 yalign 1.0
    
    show timoha:
        xalign 0.95 yalign 1.0

    timoha "та ну, угараешь? почему фрилансер - веб разработчик?"

    anton "А кто еще остается? Сам посуди - Геймдев - играть я кншн люблю, но отмел т.к. очень нишево, да и каких то вспомогательных талантов типа рисую, сочиняю сценарии, хорошо знаю физику и математику нет."

    timoha "Хаха а поч не QA?"

    anton "Кто?"

    timoha "тестировщик, деревня"

    anton "Ааааа, не, там в вакансиях Java, SQL, Sap и прочую муть требуют"

    timoha "ну ты тиииип, так выучи, лол"

    anton "Ага, времени то у меня вагон и маленькая тележка. Кстати про большое. БигДата звучит эпично, но вышмат меня убьет до первых бенефитов."

    timoha "хренефитов, давай 1С трайнешь? на заводике попашешь заодно)))"

    anton "Да заязывай, лучше статеек на тему подкинь, с чего мне начать это тернистый путь."

    timoha "как с чего? фрилансер? так составляй резюме! а, и раз все-таки веб, то почитай про конструкторы сайтов, скину статейки с хабра."

label kitchen:
    scene kitchen

    show anton:
        xalign 0.1 yalign 1.0 zoom 0.9

    show father:
        xalign 0.95 yalign 1.0 zoom 0.9

    show mother:
        xalign 0.7 yalign 1.0 zoom 0.9

    anton "Привет, родители. Я подумал, и может быть, я найду способ заработать деньги самостоятельно. Возможно, попробую веб-разработку."

    mother "Здорово, Антон! Это отличная идея. А что конкретно ты собираешься делать?"

    anton "Начну с верстки лендингов на всяких конструкторах. Это так разработка сайтов называется. Я думаю, это будет хорошим стартом."

    anton "Вчера весь день шерстил инет, вот думаю Tilda/WordPress/Turbo от яндекса их много, что начать осваивать?"

    mother "Я тут не советчик, Тош, попробуй посмотреть что популярнее."

    anton "Уже, мам...."

    father "Невольно вспоминается анекдот"

    father "Жена посылает программиста в магазин:
            - Дорогой, купи, пожалуйста, палку колбасы, и если будут яйца, то купи десяток."

    father "Через полчаса программист возвращается с десятью палками колбасы."

    father "Жена:
            - Что это?! Зачем ты купил столько колбасы?
            Программист:
            - Ну так яйца-то были..."

    anton "Кхм кх кх ну типа"

    jump messengerWithEducation