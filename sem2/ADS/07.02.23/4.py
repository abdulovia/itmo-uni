from datetime import datetime
import time

datetime_object = datetime.strptime(input(), '%d.%m.%Y')

curtime_unix = int(time.time())
birthtime_unix = time.mktime(datetime_object.timetuple())

dif_days = (curtime_unix-birthtime_unix)//(24*60*60)
print(f'Число прожитых дней: {int(dif_days)}')
# 01.09.1939
# 30475

