times = ('Fortaleza','Botafogo','Palmeiras','Flamengo',
        'Sao Paulo','Bahia','Cruzeiro','Vasco da Gama',
        'Atletico MG','Athletico PR','Internacional',
        'Criciuma','Juventude','Gremio','Bragantino','Fluminense',
        'Vitoria','Corinthians','Cuiaba','Atletico GO')
print('<'*20)
print(f'Lista de times do Brasileirão: {times}')
print('<'*20)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os 4 ultimos colocados são {times[-4:]}')
print(f'Os times em ordem alfabetica são {sorted(times)}')
print(f'O Vasco da Gama é o {times.index("Vasco da Gama")+1}ª colocado')
