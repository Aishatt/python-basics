# linear search
def linear_search(list,search_for):
    start_at = 0
    result= False
#match value with each data element
    while start_at < len(list) and result is False :
        if list[start_at] == search_for :
            result= True
        else :
            start_at = start_at + 1
    print(result)        
    return result
    
lists= [4,2,32,23,56,12,5]
linear_search(lists,56)
linear_search(lists,6)       
