list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
index_sredniy = len(list_players) // 2
list_players1 = list_players[:index_sredniy]
list_players2 = list_players[index_sredniy:]
print(list_players1)
print(list_players2)
