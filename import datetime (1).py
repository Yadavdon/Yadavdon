import datetime

current_dt = datetime.datetime.now()
print("The Current Date and Time is:", current_dt)
import datetime
dt = datetime.datetime.now()
print("Today is", dt.strftime("%A"))
import datetime
dt = datetime.datetime.now()
print("Date:", dt.strftime("%x"))
import datetime

dt = datetime.datetime.now()

print("----The Current Date and Time----")
print(dt.strftime("%a"))
print(dt.strftime("%I"), ":", dt.strftime("%M"), " ", dt.strftime("%p"), sep="")
print(dt.strftime("%d"), dt.strftime("%b"), dt.strftime("%y"), sep="-")
import datetime
dt = datetime.datetime.now()
print("Time:", dt.strftime("%X"))