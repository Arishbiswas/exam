import threading
import time

def sleepAndPrint (n):
  time.sleep(n)
  print(n)

n = 10
number = []
for i in range(n):
  num = int(input(f"Enter the number {i+1}: "))
  if num == 0:
    break;
  number.append(num)
 

threads = []
for num in number:
  thread = threading.Thread(target = sleepAndPrint, args =(num,))
  threads.append(thread)
  thread.start()

for thread in threads:
  thread.join()


