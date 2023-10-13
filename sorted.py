def reverse_sort_dictionary(input_dict):

    sorted_items = sorted(input_dict.items(), key=lambda item: item[0], reverse=True)

    result = [(name, data[0]) for name, data in sorted_items]

    return result

if __name__ == '__main__':
    input_dict = {'Tom': (5464512, 24), 'Sara': (5446987, 32), 'Mary': (1557896, 20)}
    result = reverse_sort_dictionary(input_dict)

