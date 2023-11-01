def find_common_participants(groupA, groupB, comma=','):
    groupA_ = groupA.split(comma)
    groupB_ = groupB.split(comma)

    new_group = set(groupA_).intersection(set(groupB_))

    return sorted(new_group)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
comma = '|'

new_group = find_common_participants(participants_first_group, participants_second_group, comma)
print(new_group)
