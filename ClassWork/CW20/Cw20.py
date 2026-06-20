from functools import reduce

def calculate_total(cart):
    item_totals = map(lambda x: x[0] * x[1], cart)
    return reduce(lambda x, y: x + y, item_totals, 0)

cart = [(10.99, 2), (5.49, 4), (3.99, 1)]
print(calculate_total(cart))


def combine_employee_data(names, positions, salaries):
    combined = zip(names, positions, salaries)
    return list(map(lambda x: f"{x[0]} - {x[1]}: {x[2]}", combined))

names = ["Анна", "Борис", "Виктория"]
positions = ["Менеджер", "Разработчик", "Аналитик"]
salaries = [80000, 120000, 90000]
print(combine_employee_data(names, positions, salaries))


multiplay = lambda a,b: a*b
print(multiplay(12,3))


arr = [1,2,5]
b = list(map(lambda x:x*2,arr))
print(b)


c = list(filter(lambda x: x%2==0, arr))
print(c)


from functools import reduce
arr = list(range(1, 5 + 1))
multiply = lambda a, b: a * b
print(reduce(multiply, arr)) # 120


arr1 = [1, 2, 3]
arr2 = ["a", "b", "c"]
d = list(zip(arr1, arr2)) # [(1, 'a'), (2, 'b'), (3, 'c')]
print(d)

