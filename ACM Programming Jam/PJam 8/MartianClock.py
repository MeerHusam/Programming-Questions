def main():
    input_values = list(map(int, input().split()))

    while(len(input_values) < 6):
        input_values.insert(0, 0)
        
    # Unpack the values
    year, season, days, hours, minutes, seconds = input_values

    minutes += seconds // 60
    seconds %= 60
    
    hours += minutes // 60
    minutes %= 60
    
    days += hours // 24
    hours %= 24
    
    total_days = days
    
    year += total_days // 668
    remaining_days = total_days % 668
    
    if remaining_days <= 194:  
        season = 0
        days = remaining_days
    elif remaining_days <= 194 + 154:  
        season = 1
        days = remaining_days - 194
    elif remaining_days <= 194 + 154 + 142:  
        season = 2
        days = remaining_days - (194 + 154)
    else:  
        season = 3
        days = remaining_days - (194 + 154 + 142)
    
    print(year, season, days, hours, minutes, seconds)
    
    return

main()