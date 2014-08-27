import random
import time
import datetime
print('Automatic Generation')
i = 0
while True:
    i += 1
    f = open('C:\\Users\\gseive\\Documents\\tests\\test' + str(i) + '.txt', 'w')
    f.write('Rank of file squared: ' + str(i ** 2) + ' | Random value between 1 and 5: ' + str(random.randint(0,5)) + '\n')
    t = time.strftime("%H:%M:%S")
    f.write("Current time is: " + str(t))
    f.close()
    if i % 10 == 0:
        print(str(i) + ' files generated.')
    time.sleep(random.randint(0,10))