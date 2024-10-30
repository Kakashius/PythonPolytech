# TODO Напишите функцию find_common_participants
def find_common_participants(a, b, c=","):
    result = []
    for i in a.split(c):
        if i in b.split(c):
            result.append(i)
    result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, "|")
