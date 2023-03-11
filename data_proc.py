from typing import Union


def fraction_str(numerator: int, denominator: int) -> str:
    return f"{numerator}/{denominator}"


def complex_number_str(real: float, imag: float) -> str:
    # for i in range(len(str(real))):
    # if str(real)[i] is not in "0123456789.":
    # return
    if imag >= 0:
        return f"{real}+{abs(imag)}i"
    else:
        return f"{real}{abs(imag)}i"


def doubly_linked_list_node_str(node_value: Union[str, int, float]) -> str:
    return str(node_value)


def create_doubly_linked_list() -> list:
    return []


def doubly_linked_list_append(linked_list: list, node_value: Union[str, int, float]) -> None:
    node = (node_value, None, None)
    if len(linked_list) == 0:
        linked_list.append(node)
    else:
        node_prev = linked_list[-1]
        node_prev_index = len(linked_list) - 1
        linked_list.append(node)
        node_next = linked_list[-1]
        node_next_index = len(linked_list) - 1
        node_prev = list(node_prev)
        node_prev[1] = node_next_index
        node_next = list(node_next)
        node_next[2] = node_prev_index
        linked_list[node_prev_index] = tuple(node_prev)
        linked_list[node_next_index] = tuple(node_next)


def doubly_linked_list_to_string(linked_list: list) -> str:
    values = []
    node_index = 0
    while node_index is not None:
        node = linked_list[node_index]
        node_value = doubly_linked_list_node_str(node[0])
        values.append(node_value)
        node_index = node[2]
    return " -> ".join(values)