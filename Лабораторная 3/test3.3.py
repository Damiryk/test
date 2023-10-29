
def count_letters(text):
    znaki = ' .,?!-;—:…\n'
    lower_text = main_str.lower()
    new_text = []
    new_text2 = []
    for item in lower_text:
        if item not in znaki and item not in new_text:
            new_text.append(item)
    for item in new_text:
        new_text2.append(lower_text.count(item))
    result = dict(zip(new_text, new_text2))

    return result

def calculate_frequency(result):
    total = sum(result.values())

    result_calculate = {}
    for key, char in result.items():
        result_calculate[key] = char / total

    return result_calculate

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letter_total = count_letters(main_str)
letter_calculate = calculate_frequency(letter_total)

for letter, value in letter_calculate.items():
    print(f"{letter}: {value:.2f}")

