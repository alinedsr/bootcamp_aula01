# Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário 
# pelo nome e informando o valor do salário em comparação com o bônus recebido.

ADICIONAL_BONUS = int(1000)

nome_usuario = input("Olá! Qual é o seu nome? ")
print('-----------------------------------------')

salario_mensal = float(input("Qual é o valor do seu salário mensal? "))
print('-----------------------------------------')

bonus_recebido = float(input("Qual a porcentagem de bônus recebida? "))
print('-----------------------------------------')

calculo_bonus = ((salario_mensal + ADICIONAL_BONUS) * bonus_recebido)

print(f'{nome_usuario}, o valor do seu salário complementado pelo bônus será de {calculo_bonus:,.2f}.')