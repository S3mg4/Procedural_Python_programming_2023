# TODO Напишите функцию для поиска индекса товара
def find_index_item(item_list, name):
    for index in range(len(item_list)):
        if name == items_list[index]:
            break
        else:
            index = None

    return index

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index_item(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
