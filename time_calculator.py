def add_time(start, duration, day = ''):
    # Destructuring variables
    duration_hours, duration_mins = duration.split(':')
    [[start_hours, start_mins], start_meridiem] = [ * map(lambda x: x.split(':') if x == start.split()[0] else x, start.split()) ]
    day = day.lower()

    # Creating contstants
    weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    meridiems = ['am', 'pm']
    hours_per_day = 24
    meridiem_change = 12
    mins_per_hour = 60
    
    # Days later function
    def how_many_days_later(days):
        if days == 1:
            return '(next day)'
        if days > 1:
            return f'({days} days later)'

    # Variable cleaning
    duration_hours = int(duration_hours)
    duration_mins = int(duration_mins)
    start_hours = int(start_hours)
    start_mins = int(start_mins)
    start_meridiem = start_meridiem.lower()
    days_later = 0
    end_hours = start_hours + duration_hours
    end_mins = start_mins + duration_mins

    # Conditionals for return cleaning
    if end_mins >= mins_per_hour:
        end_mins %= mins_per_hour
        end_hours += 1
    
    if end_hours >= hours_per_day:
        days_later += int(end_hours / hours_per_day)
        end_hours %= hours_per_day

    if end_hours > meridiem_change - 1:
        meridiem = meridiems[(meridiems.index(start_meridiem) + 1) % len(meridiems)]
        if end_hours > meridiem_change:
            end_hours %= meridiem_change
        if start_meridiem == 'pm' and meridiem == 'am':
            days_later += 1
    else:
        meridiem = start_meridiem
    
    s_days_later = how_many_days_later(days_later) if days_later > 0 else ''

    if day:
        day = weekdays[(weekdays.index(day) + days_later) % len(weekdays)]
        day = f'{day[0].upper() + day[1:]}'
        if days_later > 0:
            day += f' {s_days_later}'


    end_mins = str(end_mins).rjust(2,'0')
    meridiem = meridiem.upper()

    new_time = f'{end_hours}:{end_mins} {meridiem}'

    if day:
        new_time += f', {day}'
    elif days_later:
        new_time += f' {s_days_later}'
    
    return new_time