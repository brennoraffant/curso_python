print("***********************************")
print("*           MEDIA FINAL           *")
print("***********************************")


nome_do_aluno = ""
nota_do_bimestre_1 = 0.0
nota_do_bimestre_2 = 0.0
nota_do_bimestre_3 = 0.0
nota_do_bimestre_4 = 0.0
media_final = 0.0

# ENTRADA DOS DADOS
nome_do_aluno = input ("informe o nome do aluno? ")
nota_do_bimestre_1 = float(input ("informe a nota do aluno: "))
nota_do_bimestre_2 = float(input ("informe a nota do aluno: "))
nota_do_bimestre_3 = float(input ("informe a nota do aluno: "))
nota_do_bimestre_4 = float(input ("informe a nota do aluno: "))

# CALCULAR A NOTA FINAL?
media_final = (nota_do_bimestre_1 + nota_do_bimestre_2 + nota_do_bimestre_3 + nota_do_bimestre_4) / 4

# EXIBIR O RESULTADO
print("------------------------------------------")
print(nome_do_aluno + ", a sua nota final e " + str(media_final))
print("------------------------------------------")
