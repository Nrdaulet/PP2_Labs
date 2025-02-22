from datetime import datetime

date = datetime(2025, 2, 22, 12, 0, 0)
date1 = datetime(2025, 2, 18, 10, 30, 0)

difference = (date - date1).total_seconds()

print("Difference in seconds: ", int(difference))