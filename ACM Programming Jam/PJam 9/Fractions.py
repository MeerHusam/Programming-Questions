def fraction_to_decimal(num, den):
    if den == 0:
        return "Undefined"
    
    sign = "-" if (num / den) < 0 else ""
    
    num, den = abs(num), abs(den)
    
    integral = str(num // den)
    num %= den
    
    if num == 0:
        return sign + integral
    
    decimal_part = []
    rem_positions = {}
    
    repeating = False
    while num != 0:

        if num in rem_positions:
            repeating = True
            break
        rem_positions[num] = len(decimal_part)
        
        num *= 10
        decimal_part.append(str(num // den))
        num %= den
    
    if repeating:
        repeat_start = rem_positions[num]
        decimal_str = "".join(decimal_part[:repeat_start]) + "[" + "".join(decimal_part[repeat_start:]) + "]"
    else:
        decimal_str = "".join(decimal_part)
    
    return sign + integral + "." + decimal_str

num, den = map(int, input().split())

outputs = fraction_to_decimal(num, den)
print(outputs)