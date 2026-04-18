MIN_DAYS = 1
MAX_DAYS = 7

MIN_TIME = 0
MAX_MINUTES = 59
MAX_HOURS = 23


school_days = 0


def input_school_days():
    print("0. Выход")

    while True:
        user_input = input(f"Введите количество учебных дней (от {MIN_DAYS} до {MAX_DAYS}): ").strip()     

        if not user_input:
            print("Ввод не должен быть пустым.")
            continue
        if user_input == "0":
            return 0
        else:
            if user_input.isdigit():
                days = int(user_input)
                if MIN_DAYS <= days <= MAX_DAYS:
                    return days
                else:
                    print(f"Неверный ввод. Число должно быть (от {MIN_DAYS} до {MAX_DAYS}):")
            else:
                print(f"Ошибка: нужно ввести целое число (от {MIN_DAYS} до {MAX_DAYS}):")


def input_time(t_min_time, t_max_time):
    label = "часы" if t_max_time == MAX_HOURS else "минуты"
    prompt = f"Введите {label} ({t_min_time}-{t_max_time}): "

    while True:
        user_input_time = input(prompt).strip()
        
        if user_input_time.isdigit():
            value = int(user_input_time)
            if t_min_time <= value <= t_max_time:
                return value
                
        print("Ошибка: введите целое число в указанном диапазоне.")


def dz3_2(school_days = input_school_days()):
    if school_days == 0:
        print("На этой неделе не учились")
        print("Программа завершена.")
        return

    total_hours = 0
    total_minutes = 0

    for i in range(school_days):
        print(f"\n--- День {i + 1} ---")
        h = input_time(MIN_TIME, MAX_HOURS)
        m = input_time(MIN_TIME, MAX_MINUTES)
        
        total_hours += h
        total_minutes += m

    total_hours += total_minutes // 60
    total_minutes %= 60
    
    print(f"\n\n\tОбщее время учёбы за неделю: {total_hours:02d}:{total_minutes:02d}")


dz3_2()
