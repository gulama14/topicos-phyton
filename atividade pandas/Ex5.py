import pandas as pd

dfInicial = pd.read_csv("usuarios.txt",delim_whitespace = True)

nomes = df0['Usuários']
nomeslist = [df0.iloc[0]['Usuários'],df0.iloc[1]['Usuários'],df0.iloc[2]['Usuários'],df0.iloc[3]['Usuários'],df0.iloc[4]['Usuários'],df0.iloc[5]['Usuários']]
espaço = df0['Espaço_Utilizado']
espaçototal = converterEspaço(espaço).sum()
espaçomedio = espaçototal/6

def converterEspaço(espaço):
    espaço=espaço/1024
    espaço=espaço/1024
    return espaço
  
def calcularPorcentagemDeUso(espaçototal):
    poruso = (converterEspaço(espaço) / espaçototal) * 100
    return poruso
  
df0.head()

dfFinal = pd.DataFrame(nomeslst, columns = ['Nomes'])
dfFinal['Espaço Utilizado'] = converterEspaço(espaço)
dfFinal['% do uso'] = calcularPorcentagemDeUso(espaçototal)

print(dfFinal)
print('Espaço total ocupado = ', f'{espaçototal:,.2f}','Mb')
print('Espaço Medio ocupado = ', f'{espaçomedio:,.2f}','Mb')

dfFinal.to_csv('relatorio.txt', index=None, sep=' ', mode='a')