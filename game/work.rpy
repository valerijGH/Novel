label messengerWithCustomer:
    scene messenger

    show anton:
        xalign 0.1 yalign 1.0

    show customer:
        xalign 0.95 yalign 1.0
    
    customer "Слушай, Антон, мы можем обойтись без гаранта, прямо между нами. Ты же понимаешь, комиссия сайта - это лишние расходы."

    anton "Ну, хорошо, давай так. Надеюсь, это не будет проблемой."

    "Осталось 18 дней до концерта"

    scene messenger with fade

    show anton:
        xalign 0.1 yalign 1.0

    show customer:
        xalign 0.95 yalign 1.0

    customer "Привет, как идут дела, может есть вопросы?"

    anton "Все штатно, примерно треть уже сделал, вопрос только по дизайну."

    customer "Оу, отправишь посмотреть, внесем правки, посоветуем?"

    anton "Да, конечно"

    "*отправляет файл*"

    "Осталось 16 дней до концерта"

    scene messenger with fade

    show anton:
        xalign 0.1 yalign 1.0

    anton "Добрый день, доделал проект, отправляю"

    customer "..."

    pause 1.0

    anton "Вы тут?"

    customer "..."

    pause 1.0

    "Осталось 15 дней до концерта"

    jump messengerAboutDeception