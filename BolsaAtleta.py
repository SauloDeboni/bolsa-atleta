import pandas as pd
import os

def SingleName(pathToFile):
  xlsx = pd.ExcelFile(pathToFile)
  tabela = pd.read_excel(xlsx)
  
  tabela_singleName = []

  for x in tabela.index:
      if "," in tabela['NOME COMPLETO'][x]:
          tabela_nome_duplo = []
          nome_duplo = tabela['NOME COMPLETO'][x]
          tabela_nome_duplo.append(nome_duplo)
        
          for doublename in tabela_nome_duplo:
              separador = doublename.split(', ')
              for singlename in separador:
                  novo_row = tabela.loc[x].tolist()
                  novo_row[2] = singlename
                  tabela_singleName.append(novo_row)
                  
      else:
        novo_row = tabela.loc[x].tolist()
        tabela_singleName.append(novo_row)
  
  single_dataFrame = pd.DataFrame(tabela_singleName, columns=['RACE', 'RAIA', 'NOME COMPLETO', 'CPF', 'PROVA', 'SUBCATEGORIA',
       'COLOCAÇÃO', 'CLUBE', 'ESTADO', 'FINAL', 'TEMPO', 'DATA'])
 
  filename = os.path.basename(pathToFile)
  single_dataFrame.to_excel("{}_SINGLENAME.xlsx" .format(os.path.splitext(filename)[0]))
  print("Seu arquivo foi gerado com o nome de {}_SINGLENAME.xlsx" .format(os.path.splitext(filename)[0]))

