import time
from termcolor import colored

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
raw_input()                    # press Enter to begin
print('Stopwatch has Started')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1

try:
	while True:
		raw_input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime,1)
		print colored(totalTime,'red')
		lapNum += 1
		lastTime = time.time() # reset the last lap time
		
	
except KeyboardInterrupt:
       # Handle the Ctrl-C exception to keep its error message from displaying.
	#print (totalTime)	
	print('\nDone.')


