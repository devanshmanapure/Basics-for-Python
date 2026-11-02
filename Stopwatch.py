#Stopwatch
import time
input("Press Enter to START...")
start = time.time()
input("Press Enter to STOP...")
end = time.time()
total = round(end - start, 2)
print("Time Taken:", total, "seconds")