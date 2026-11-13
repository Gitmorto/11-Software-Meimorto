#setting counter and num to 0
counter = 0
num = 0
num = int(input('Number for a time table '))
#The limit asks how many times the time tables wants
limit = int(input('how  any time tables do u want '))
#using a while loop
while limit == 0:
    limit = int(input('Please put how many times u want '))
while counter != limit:
    counter += 1
    print (f'{num} * {counter} = {num * counter}')
 
