import multiprocessing



def check_divisor(number,res_queue):
  count=0
  for i in range(1, number+1):
    if number%i==0:
      count+=1
  res_queue.put((number, count))


n = int(input("Enter length of list: "))
numbers = []
for i in range(n):
  num = int(input(f"enter the number {i+1}: "))
  numbers.append(num)
print(numbers)

res_queue = multiprocessing.Queue()

processes = []
for num in numbers:
  process = multiprocessing.Process(target = check_divisor, args = (num,res_queue))
  processes.append(process)
  process.start()

for process in processes:
  process.join()

maxDivisor=0
numMaxDivisor= None

while not res_queue.empty():
  number,count = res_queue.get()
  if count > maxDivisor:
    maxDivisor = count
    numMaxDivisor = number

print(f"the number with max divisor is: {numMaxDivisor}")
