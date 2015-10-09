''' This program prints numbers  n<100 , it prints 'fizz' if n%3 is zero , 'buzz' if divided by 5 and
'fizzbuzz' if divided by 3 and 5 '''
''' Braces are used in print command to make the program run both in Python 2.7 & Python 3'''
n = 100
for n in range ( 1, n):
    if n % 3 == 0:
       if n % 5 == 0:
          print ('fuzz buzz') 
       else:
          print ('fuzz')
    elif n % 5 == 0:
           print ('buzz')
    else:
           print( n)
