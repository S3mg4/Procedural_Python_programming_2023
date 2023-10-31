def count_letters(string):
    lower_string = string.lower()
    list_of_letters = []
    for symbol in lower_string:
        if symbol.isalpha():
            list_of_letters.append(symbol)

    dictionary_of_letters = {}
    for index, value in enumerate(list_of_letters):
        sum_of_letter = 0
        for letter in range(len(list_of_letters)):
            if list_of_letters[letter] == value:
                sum_of_letter += 1
        dictionary_of_letters[value] = sum_of_letter

    return dictionary_of_letters

def calculate_frequency(dictionary):
    summary = sum(dictionary.values())

    dictionary_of_frequency = {}
    for value, count in enumerate(dictionary):
        dictionary_of_frequency[count] = dictionary.get(count) / summary

    return dictionary_of_frequency

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

dictionary_of_frequency = calculate_frequency(count_letters(main_str))
for letter, value in dictionary_of_frequency.items():
    print (f"{letter}: {value:.2f}")
