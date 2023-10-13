def merge_list(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise ValueError("Both inputs must be valid lists.")

    merged_list = []

    while list1 and list2:
        if list1[0] < list2[0]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))

    merged_list.extend(list1)
    merged_list.extend(list2)

    return merged_list

