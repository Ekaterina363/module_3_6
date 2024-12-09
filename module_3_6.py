def calculate_structure_sum(*args):
    summ = 0
    for elem in args:
        if isinstance(elem, str):
            summ+= len(elem)
        elif isinstance(elem, int):
            summ +=elem
        elif isinstance(elem, dict):
            summ += calculate_structure_sum(list(elem.keys()))
            summ += calculate_structure_sum(list(elem.values()))
        elif isinstance(elem, list):
            summ += calculate_structure_sum(*elem)
        elif isinstance(elem, tuple):
            summ += calculate_structure_sum(*elem)
        elif isinstance(elem, set):
            summ += calculate_structure_sum(list(elem))
    return summ
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
print(data_structure)
print(calculate_structure_sum(data_structure))