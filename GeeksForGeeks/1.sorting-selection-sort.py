class Solution: 
    def select(self, arr, i):
        min = i
        for i in range(i+1,len(arr)):
            if arr[i] < arr[min]:
                min = i
        return min

    
    def selectionSort(self, arr,n):
        for i in range(n):
            min = self.select(arr,i)
            arr[min],arr[i] = arr[i],arr[min]
    
        return arr
        