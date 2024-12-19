def arrival_times(schedule, delay):
    new = []

    for time in schedule:
        hh, mm = time.split(':')
        hh = int(hh)
        mm = int(mm)

        total_minutes = hh * 60 + mm + delay
        
        new_hh = (total_minutes // 60) % 24
        new_mm = total_minutes % 60

        new.append(f"{new_hh:02}:{new_mm:02}")

    return new