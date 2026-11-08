# 11 - Time Converter
SECONDS_PER_DAY = 86400     # 24 * 60 * 60
SECONDS_PER_HOUR = 3600     # 60 * 60
SECONDS_PER_MINUTE = 60

total_seconds = int(input())
days, rest = divmod(total_seconds, SECONDS_PER_DAY)  # rest = what is left over, less than 1 day
hours, rest = divmod(rest, SECONDS_PER_HOUR)
minutes, seconds = divmod(rest, SECONDS_PER_MINUTE)

print(f"{days}d {hours:02}:{minutes:02}:{seconds:02}")
