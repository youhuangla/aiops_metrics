import datetime

# Unix timestamp
timestamp = 1694966460

# Convert to datetime object
dt_object = datetime.datetime.fromtimestamp(timestamp)

# Format as a string
formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')

print(formatted_time)
