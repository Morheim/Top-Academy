MIN_COST = 1 #Константа минимальной стоимости учебного материала

def get_material_type():
    while True:
        mat_type = input("Введите тип учебного материала (книга/видео): ").strip().lower()
#для решения проблемы регистра и случайных пробелов при вводе использую .strip().lower()
        match mat_type:
            case "книга" | "видео":
                return mat_type
            case _:
                print("Некорректный выбор, попробуйте снова.")

def get_valid_cost():
    while True:
        try:
            cost = int(input("Введите стоимость материала: "))
            if cost >= MIN_COST:
                return cost
            print(f"Неверная стоимость (должна быть больше либо равна {MIN_COST})")
        except ValueError:
            print("Пожалуйста, введите целое число")

def get_material_category():
    while True:
        category = input("Введите категорию (математика/история): ").strip().lower()
        match category:
            case "математика" | "история":
                return category
            case _:
                print("Некорректный выбор, попробуйте снова.")

# Сохраняем результаты в переменные, чтобы не вызывать ввод повторно
material_type = get_material_type()
cost = get_valid_cost()
category = get_material_category()

# Вывод результата
print(f"""
Материал добавлен:
\tТип       - {material_type}
\tСтоимость - {cost}
\tКатегория - {category}""")

