import time

print("Calling sleep")
time.sleep(2)
print("Slept for 2 seconds")

#testing sleep in a while loop
n = 0
print("Begin while loop test")
while n < 5:
    time.sleep(1)
    print("Sleeping for 1 more seconds")
    print("n: ", n)
    n += 1
