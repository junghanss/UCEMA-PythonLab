def linear_search(item,my_list):
    found = False
    i=0
    
    while i<len(my_list) and found == False:
        if my_list[i] == item:
            found=True
        else:
            i=i+1
    return found

lista_prueba = [1,5,9,15,25,346,932]
print(linear_search(65,lista_prueba))
print(linear_search(1,lista_prueba))
