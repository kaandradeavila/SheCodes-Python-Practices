# Import datetime
from datetime import datetime

# Display the current date and time (no formatting)
now = datetime.now()
print(now)

# Display the current date and time following this format: Date: Jan 12, 2032 Time: 14:03
formatted_now = now.strftime("Date: %b %d, %Y Time: %H:%M")
print(formatted_now)

# Convert this time stamp 1705590204 into a date and display only the time using this format: 2:30am
timestamp = 1705590204
timestamp_date = datetime.fromtimestamp(timestamp)
formatted_timestamp = timestamp_date.strftime("%-I:%M%p").lower()
print(formatted_timestamp)
