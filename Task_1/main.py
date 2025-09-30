from linked_list import LinkedList
from handlers.reverse import reverse
from handlers.sort import merge_sort
from handlers.merge_lists import merge_sorted_lists

def create_sample_list():
    linked_list = LinkedList()
    for x in [5, 3, 8, 1, 2]:
        linked_list.append(x)
    return linked_list

def main():
    print("Menu:")
    print("1. Reverse a linked list")
    print("2. Sort a linked list using merge sort")
    print("3. Merge two sorted linked lists")

    choice = int(input("Enter your choice (1-3): "))

    match choice:
        case 1:
            linked_list = create_sample_list()
            print("Default list:")
            linked_list.print_list()
            linked_list.head = reverse(linked_list.head)
            print("Reversed list:")
            linked_list.print_list()

        case 2:
            linked_list = create_sample_list()
            print("Default list:")
            linked_list.print_list()
            linked_list.head = merge_sort(linked_list.head)
            print("Sorted list:")
            linked_list.print_list()

        case 3:
            first_list = LinkedList()
            second_list = LinkedList()
            for x in [1, 3, 5]:
                first_list.append(x)
            for x in [2, 4, 6]:
                second_list.append(x)
            print("List 1:")
            first_list.print_list()
            print("List 2:")
            second_list.print_list()
            merged_head = merge_sorted_lists(first_list.head, second_list.head)

            merged = LinkedList()
            merged.head = merged_head
            print("Merged sorted list:")
            merged.print_list()

        case _:
            print("Invalid choice. Please select a valid option!")

if __name__ == "__main__":
    main()
