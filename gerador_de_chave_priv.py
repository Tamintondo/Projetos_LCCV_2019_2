def gerador_chave_priv(totiente,e):
    d=0
    while(mod(d*e,totiente)!=1):
        d=d+1
    return d