def slice_less(my_list, lesser): 
    my_list = [item for item in sorted(my_list, reverse=True) if item  > lesser]
    return my_list
        
        
