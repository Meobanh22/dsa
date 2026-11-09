from heapq import merge
import random

def insertSort(arr):
    for k in range(len(arr)):
        tmp= arr[k]
        pos= k
        while pos>0 and arr[pos-1]>tmp:
            arr[pos]=arr[pos-1]
            pos-=1
        arr[pos]=tmp

def swap(a,b):
    return b,a

def selectionSort(arr):
    for i in range(len(arr)):
        minIndex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minIndex]:
                minIndex=j
        if minIndex!=i:
            arr[i],arr[minIndex]=swap(arr[i],arr[minIndex])

def bubbleSort(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=swap(arr[j],arr[j+1])
                swapped=True
            if not swapped:
                break

def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i=j=k=0

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1

n = random.randint(0,100)
arr = [random.randint(-10000,100000) for _ in range(n)]
mergeSort(arr)
print(arr)   