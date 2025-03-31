from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Data de nascimento: '))
dados['cart'] = int(input('Carteira de Trabalho [0 não tem]: '))
dados['idade'] = datetime.now().year - nasc
if dados['cart']!= 0:
    dados['contratação'] = int(input('Ano da contratação: '))
    dados['salario'] = float(input('Valor do salario: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('><'*25)
for k, v in dados.items():
    print(f'{k} = {v}')
print('<>'*25)
print(dados)
