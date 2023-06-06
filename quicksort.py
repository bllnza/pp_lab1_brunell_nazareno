def quick_sort(lista_original:list,flag_orden:bool)->list:
    lista_de = []
    lista_iz = []
    if(len(lista_original)<=1):
        return lista_original
    else:
        pivot = lista_original[0]
        for elemento in lista_original[1:]:
            if(elemento > pivot and flag_orden) or (elemento < pivot and not flag_orden):
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)
    lista_iz = quick_sort(lista_iz,flag_orden)
    lista_iz.append(pivot) 
    lista_de = quick_sort(lista_de,flag_orden)
    lista_iz.extend(lista_de) 
    return lista_iz


