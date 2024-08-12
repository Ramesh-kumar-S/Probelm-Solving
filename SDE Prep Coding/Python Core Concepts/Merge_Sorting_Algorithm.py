"""
    Merge Sorting Algorithm 
        -  Divide and Conquer Algorithm
        -  Split the Array in to Halves till the ponint it can't be halved  
"""

def mergeSort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        lefthalf = dataset[:mid]
        righthalf = dataset[mid:]
        
        #Halve the left & right halfs
        mergeSort(lefthalf)
        mergeSort(righthalf)
        
        i=0 #Left array index
        j=0 #Right array index
        k=0 #Meged array index
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[i]:
                dataset[k] = lefthalf[i]
                i+=1
            else:
                dataset[k] = righthalf[j]
                j+=1
            k+=1
        
        #Copy the left over left half of array to merged array
        while i < len(lefthalf):
            dataset[k] = lefthalf[i]
            i+=1
            k+=1

        #Copy the left over right half of array to merged array
        while j < len(righthalf):
            dataset[k] = righthalf[j]
            j+=1
            k+=1


alist = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
mergeSort(alist)
print(alist)