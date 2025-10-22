import statistics #подключение библиотеки для медианы
first=third=bigger=0 #первое число, обозначение переменных
second=1 #второе число
fibon=[] #Фибоначчи
n=int(input('Введите число: ')) #ввод числа
for i in range(0, n): # цикл чисел Фибоначчи
    third=first+second
    fibon.append(first)
    first=second
    second=third
print('Изначальный список: ', fibon) 
for i in range(0, len(fibon)): #цикл от 0 до длины
    if i%2==0: #проверка на четность
        fibon[i]*=2 #умножение на два
    else: 
        fibon[i]**=2 #иначе - возводим в квадрат
print('Изменённый список:', fibon)
print('Минимальный элемент: ', min(fibon))
print('Максимальный элемент: ', max(fibon))
print('Количество элементов: ', len(fibon)) 
for i in range(0, len(fibon)): #цикл 
    if fibon[i]>(statistics.median(fibon)): #если больше мадианного
        bigger+=1 #прибавляем 1 к счетчику
print('Медиана списка: ', statistics.median(fibon)) 
print('Количество элементов, больше медианного: ', bigger)