def sortarray(arr,index):            #function to sort an array
    for i in range(index):           #loop in an array
        min=arr[i]
        for j in range(i+1,index):   #loop to check minimum number 
            if(arr[j]<min):
                temp=arr[j]           #swapping of numbers
                arr[j]=arr[i]
                arr[i]=temp
    for i in range(index):             #loop to print the number
        print(arr[i])

