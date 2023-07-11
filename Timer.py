import time

seconds = input ("Enter time in seconds: ")

while True:
    try:
        seconds = int(seconds)
        break
    except:
        seconds = input ("Please enter a number: ")
        
while seconds > 0:
    print (seconds)
    seconds -= 1
    time.sleep (1)
    
print ("Time up!")