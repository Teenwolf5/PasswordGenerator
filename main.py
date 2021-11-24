print("генератор случайных паролей")
print("Введите количество символов")
a= int(input())
import random
length = a
passwd = list('1234567890abcdABCD!@#$%&*()?жзиклпшщя')
random.shuffle(passwd)
passwd = ''.join([random.choice(passwd) for x in range(length)])
print (passwd)  
