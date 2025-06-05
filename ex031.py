print('Aumento de salario dos funcinario se o funcinario recber \n'
      'a mais R$1250.00 recébera um aumento de 10% para salario inferior ou superior \n'
      'recebera um aumento de 15%.')
print('Use o "." para saparar inves da virgula.')
salario = float(input("Escreva o quanto o funcinario recebe; "))
if salario > 1250.00:
    aumento = salario * 0.10
    salario_novo = salario + aumento
    print(f"O novo salario será este {salario_novo:.2f}")
else:
    aumento = salario * 0.15
    salario_novo = salario + aumento
    print(f"O novo salario será este {salario_novo:.2f}")