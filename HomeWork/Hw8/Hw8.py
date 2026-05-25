def greatest_common_divisor(val1, val2):
    if val2 == 0:
        return val1
    else:
        print(f"val1 ({val1}) | ({val2}) val2\n")
        return greatest_common_divisor(val2, val1 % val2)

print(greatest_common_divisor(int(input(f"val1 = ")), int(input(f"val2 = "))))

