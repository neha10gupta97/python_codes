import time

def stopwatch(seconds):
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print "seconds passed: %02d" % (elapsed) 
        time.sleep(1)  

while True:
	x=input("enter duration for stopwatch:  ")
	stopwatch(x)
	print("want to run again? (Y/N)")
	ch=raw_input()
	if(ch=='Y' or ch=='y'):
		continue
	elif(ch=='N'or ch=='n'):
		break;
	else:
		print("enter either Y or N")
