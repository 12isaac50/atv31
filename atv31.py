def valor_imposto(valor):
    if valor <= 1000:
        imposto = valor * 0.1
    elif valor <= 2000: 
        imposto = valor * 0.13
    else:
        imposto = valor * 0.20
    return imposto

# Mudando os prompts para "digite o valor do número"
produto1 = float(input("Digite o valor do número 1: "))
produto2 = float(input("Digite o valor do número 2: "))
produto3 = float(input("Digite o valor do número 3: "))
produto4 = float(input("Digite o valor do número 4: "))

# Calculando o imposto de cada produto
imposto1 = valor_imposto(produto1)
imposto2 = valor_imposto(produto2)
imposto3 = valor_imposto(produto3)
imposto4 = valor_imposto(produto4)

# Calculando o valor total de cada produto com imposto
total_com_imposto1 = produto1 + imposto1
total_com_imposto2 = produto2 + imposto2
total_com_imposto3 = produto3 + imposto3
total_com_imposto4 = produto4 + imposto4

# Exibindo os resultados
print(f"""
O imposto do produto 1 é R${imposto1:.2f} e o valor total com imposto é R${total_com_imposto1:.2f}
O imposto do produto 2 é R${imposto2:.2f} e o valor total com imposto é R${total_com_imposto2:.2f}
O imposto do produto 3 é R${imposto3:.2f} e o valor total com imposto é R${total_com_imposto3:.2f}
O imposto do produto 4 é R${imposto4:.2f} e o valor total com imposto é R${total_com_imposto4:.2f}
""")
