from datetime import datetime, timedelta


def calculate_alarm_time(current_time, alarm_time):
    current_time = datetime.strptime(current_time, "%H:%M:%S")
    alarm_time = datetime.strptime(alarm_time, "%H:%M:%S")

    if alarm_time <= current_time:
        # اگر زمان آلارم کمتر یا مساوی زمان فعلی باشد، به فردای همان روز اضافه کن
        alarm_time += timedelta(days=1)

    time_difference = alarm_time - current_time
    total_seconds = time_difference.total_seconds()

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


current_time = input()
alarm_time = input()

result = calculate_alarm_time(current_time, alarm_time)
print(result)