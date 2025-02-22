from datetime import datetime
current_time = datetime.now()

new_time = current_time.replace(microsecond=0)
print("Current time: ",current_time)
print("Current time without microseconds: ",new_time)