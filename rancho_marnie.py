comprar, quantia = input().split()
comprar =  int(comprar)
quantia = int(quantia)
vender = quantia - comprar
if vender >= 2 and vender % 2 == 0:
	print("vendido")
else: 
     print("sinto muito")