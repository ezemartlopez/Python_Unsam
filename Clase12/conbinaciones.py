def combinaciones(lista , n):
    if n==1:
        comb = lista
    else:
        comb_rec = combinaciones(lista,n-1)
        comb = [e+c for e in lista for c in comb_rec]
    return comb