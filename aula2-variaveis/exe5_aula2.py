# Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado pelo usuário, assim como a quantidade de dias 
# pelos quais o carro foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

km = int(input('Quantos km foram percorridos com o carro alugado? '))
dias = int(input('Quantos dias foram percorridos com o carro foi alugado? '))
valor_diaria = 60
valor_km = 0.15

valor_final = valor_diaria * dias + valor_km * km
print(f'O valor total a ser pago pela quantidade de dias do carro alugado {dias} e pela quilometragem percorrida {km} é R$ {valor_final}')