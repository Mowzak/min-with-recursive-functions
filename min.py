def operator_min(lst,coun,arg):
    if len(lst)==coun:
        return arg

    if lst[coun]<arg:
        saver = lst[coun]

    elif lst[coun]==arg:
        saver = lst[coun]
    elif lst[coun]>arg:
        saver = arg
    
    return operator_min(lst,coun+1,saver)
 
def min(a):
    return operator_min(a,1,a[0])


lst = [45,78,10,8041,840,54,6,90]
print(min(lst))
