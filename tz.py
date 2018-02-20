import datetime

now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

timeMin = datetime(year=now.year, month=now.month, day=now.day, tzinfo=cest) + timedelta(days=1)
timeMin = timeMin.isoformat()
timeMax = datetime(year=now.year, month=now.month, day=now.day, tzinfo=cest) + timedelta(days=3)
timeMax = timeMax.isoformat()

print(timeMin)
print(timeMax)
print(now)
