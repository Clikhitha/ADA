def localMinima(arr):
  positions = dict({0:arr[0],len(arr)-1:arr[len(arr)-1]})
  for i in range(1,len(arr)-1):
    if arr[i-1] > arr[i] and arr[i+1] > arr[i] :
      positions.update({i:arr[i]})
  return positions
arr=input('Enter array values\t').split()
for i  in range(len(arr)):
  arr[i]=int(arr[i])
min=localMinima(arr)
print(min.items())