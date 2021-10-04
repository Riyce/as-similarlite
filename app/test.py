import tasks
from time import sleep

print("add 3+5")
ret = tasks.add.delay(3,5)
print("Task ID:")
print(ret)
sleep(10)
s = 'SUCCESS'
status = 'PENDING'
while status != s:
    status = ret.status
    print(status)
    if status == s:
        print(ret.get())
