"""
the program consists of creating a list and 
iterating over it to add values ​​to a new list. 
we attach both lists in another list and show on the screen
"""
def attach_lists(first_value, second_value): 
    while len(first_value) == len(second_value): # 3==3
        all_lst=first_value+second_value
        print(all_lst)
        break
    
def lst():
    lst=[1,2,3]
    new_lst=[] # [0, 1, 2]
    for i in range(len(lst)): # [0, 1, 2]
        new_lst.append(i)  
    attach_lists(lst, new_lst)
lst()

