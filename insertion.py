def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>0 and key<arr[j]:
          arr[j+1]=arr[j]
          j-=1
          arr[j+1]=key
arr=list()
n=int(input("enter number of elements"))
for i in range(0,n):
    print("enter element",i+1,":",end='')
    ele=int(input())
    arr.append(ele)
insertionsort(arr)
print("sorted array is:",arr)
