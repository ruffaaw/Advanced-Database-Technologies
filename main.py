import time
# from datetime import datetime
import datetime
import calendar


date = b'2023-06-11'
date = date.decode("utf-8")
# print(int(date))

# current_time =time.time()
# print(current_time)
# t=datetime.datetime(2024,6,5,12,52).timestamp()
# print(t)
# epoch = 1717584720
# epoch_date_time = datetime.datetime.fromtimestamp( t )  
# print("Converted Datetime:", epoch_date_time )
date_object = datetime.datetime.strptime(date, '%Y-%m-%d').timestamp()
print(date_object)
# print(date_object.timestamp())
# print(datetime.datetime(date).timestamp())

# datetime_str = '09/19/22 13:55:26'

# datetime_object = datetime.datetime.strptime(date, '%Y-%m-%d')
# epoch_time=datetime.datetime(datetime_object).timestamp()

# print(type(datetime_object))
# print(datetime_object)  # printed in default format
# print(epoch_time)

