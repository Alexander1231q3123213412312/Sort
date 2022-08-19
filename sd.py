n=int(input("Введите кол-во списка: "))
arr=[]
arr_1=[]
i_1,i_2=0,0
print("Вводите элементы списка: ")
for i in range(n):
    a=int(input())
    arr.append(a)
    if (a>0):
        arr_1.append(a)
        
b=abs(max(arr))
for i in range(n):
    if(abs(arr[i])==b):
        i_1=i
        break
    
c=abs(min(arr))
for i in range(n):
    if(abs(arr[i])==c):
        i_2=i
        break

for i in range(n-1):
    for j in range(n-i-1):
        if(arr[j]<arr[j+1]):
            a=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=a

print("Отсортированный список в порядке убывания (пузырьковый метод сортировки): ")
for i in range(n):
    print(arr[i],end=" ")
print()
print("Сумма положительных чисел: ",sum(arr_1))
print("Количество элементов между индексами: ",abs(i_1-i_2)-1)
