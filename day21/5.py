def search_replace(L, num):
    replaced = False
    
    
    for i in range(len(L)):
        if L[i] == num:
            L[i] = 0
            replaced = True
    
   
    if replaced:
        print("List after replacement:")
        print(L)
    else:
        print("The number", num, "does not exist in the list.")

      
L = [10, 20, 30, 10, 40] 

num_to_search = 10
search_replace(L, num_to_search)
