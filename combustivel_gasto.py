modelo_do_carro = ""
autonomia_do_carro = 0
distancia_da_viagem = 0
preço_do_combustivel = 0.0
quantidade_de_combustivel_usado = 0.0
valor_gasto = 0.0

print("***************************************")
print("*       CONSUMO DE COMBUSTIBVEL       *")
print("***************************************")

modelo_do_carro = input("informe o modelo do carro? ")
autonomia_do_carro = int(input("informe a autonomia do carro? "))
distancia_da_viagem = int(input("infome a distancia percorrida? "))
preço_do_combustivel = float(input("valor do combustivel? " ))

quantidade_de_combustivel_usado = distancia_da_viagem / autonomia_do_carro
valor_gasto = quantidade_de_combustivel_usado * preço_do_combustivel

print("******************************************")
print("*           R E S U L T A D O            *")
print("******************************************")
print("modelo do carro" + modelo)
print("autonomia_do_carro: " + str(autonomia_do_carro) +"Km/1")
print("distancia percorrida: " + str(distancia_da_viajem) + "Km")
print("valor do combustivel: R$ " + str(preço_do_combustivel))
print()
print("******************************************")
print("quantidade de combustivel utilizadao: " + str(quantidade_de_combustivel_usado + "1"))
print("total gasto com a viagem: R$" + str(valor_gasto))
print("******************************************")
