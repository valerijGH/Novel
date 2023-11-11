# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define anton = Character('Антон', color="#0004ff")
define droa = Character('Дроа', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.


# Игра начинается здесь:
label start:
    scene bg room

    show anton

    anton "Так долго спал, но хочется ещё"

    anton "Сколько время?"

    hide anton

    scene computer
    with vpunch

    anton "Не может быть, я проспал"


label concert:

    scene bg concert

    show anton

    anton "Вроде успел"

    anton "Всю жизнь мечтал попасть попасть на этот концерт"

    show anton:
        xalign 0.1
    with dissolve

    show droa:
        xalign 0.8 yalign 1.0
    with dissolve

    droa "Привет"

    return
