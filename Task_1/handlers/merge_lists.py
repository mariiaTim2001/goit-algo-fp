def merge_sorted_lists(first_list, second_list):
    if not first_list:
        return second_list
    if not second_list:
        return first_list

    if first_list.data <= second_list.data:
        result = first_list
        result.next = merge_sorted_lists(first_list.next, second_list)
    else:
        result = second_list
        result.next = merge_sorted_lists(first_list, second_list.next)
    return result
