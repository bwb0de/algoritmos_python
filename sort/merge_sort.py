def merge_sort(lista, init_idx=0, end_idx=None):
    if end_idx == None:
        end_idx = len(lista)

    if end_idx - init_idx > 1:
        mid = end_idx + init_idx // 2 
        merge_sort(lista, init_idx, mid)
        merge_sort(lista, mid, end_idx)
        merge(lista, init_idx, mid, end_idx)
    
def merge(lista, init_idx, mid, end_idx):
    left_list = lista[init_idx:mid]
    right_list = lista[mid:end_idx]
    i, j = 0, 0
    for k in range(init_idx, end_idx):
        if i >= len(left_list):
            lista[k] = right_list[j]
            j += 1
        elif j >= len(right_list):
            lista[k] = left_list[i]
            i += 1
        elif left_list[i] < right_list[j]:
            lista[k] = left_list[i]
            i += 1
        else:
            lista[k] = right_list[j]
            j += 1