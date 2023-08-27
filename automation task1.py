#1. Finding the maximum number in a array.

print("1. Finding the maximum number in a array.")
arr=[2,44,34,55,3,1,90,7]
print("\narr = ",arr)
mx=arr[0]
a=len(arr)-1
for i in range(a):
    if arr[i+1]>arr[i]  :
        mx=arr[i+1]
print("Maximum number in array = ",mx)
print("Maximum number in array by max() = ",max(arr))

    

#2. Find prime number in an array.

print("\n\n\n2. Find prime number in an array.")
arr1=[11,2,4,7,40,55,80,97]
print("\narr1 = ",arr1)
b=len(arr1)
print("Prime Numbers:")
for i in range(b):
    n=arr1[i]
    flag=0
    for j in range(2,n):
        if n%j==0:
            flag=1
            break
    if flag==0:
        print(n)
        


#3. Implement a sorting algorithm that you find easy.

print("\n\n\n3. Implement a sorting algorithm that you find easy.")
print("\nBubble sort")
arr2=[1,34,22,66,8,23,99,19]
print("arr2 = ",arr2)
c=len(arr2)
for i in range(c-1):
    for j in range(0,c-i-1):
        if arr2[j]>arr2[j+1]:
            arr2[j],arr2[j+1]=arr2[j+1],arr2[j]
print("Sorted Array arr2 = ",arr2)
        
            
    
