import pandas as pd
import os

def SingleName(path, separador):
    tabela = pd.read_excel(path)
  
    tabela_singleName = []

    for x in tabela.index:
        if separador in tabela['NOME'][x]:
            tabela_nome_duplo = []
            nome_duplo = tabela['NOME'][x]
            tabela_nome_duplo.append(nome_duplo)
        
            for doublename in tabela_nome_duplo:
                separacao = doublename.split(separador)
                for singlename in separacao:
                    novo_row = tabela.loc[x].tolist()
                    novo_row[2] = singlename
                    tabela_singleName.append(novo_row)
                  
        else:
            novo_row = tabela.loc[x].tolist()
            tabela_singleName.append(novo_row)
  
    single_dataFrame = pd.DataFrame(tabela_singleName, columns=['RACE', 'RAIA', 'NOME', 'PROVA', 'SEXO', 'SUBCATEGORIA',
                                                                'COLOCACAO', 'CLUBE', 'ESTADO', 'FINAL', 'TEMPO', 'DATA'])
 
    filename = os.path.basename(path)
    single_dataFrame.to_excel("{}_SINGLENAME.xlsx" .format(os.path.splitext(filename)[0]))
    print("Seu arquivo foi gerado com o nome de {}_SINGLENAME.xlsx" .format(os.path.splitext(filename)[0]))