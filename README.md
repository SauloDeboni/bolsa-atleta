# Módulo Bolsa Atleta
O módulo importa Panda e OS.

## SingleName
```
.SingleName(caminho do arquivo excel, separador)
```

Esta função separa os resultados de barcos coletivos em linhas individuais no Excel. Deve ser indicado o caminho do arquivo atual como argumento e o caracterse separador (string). Um novo arquivo Excel é exportado.

O arquivo Excel deve conter as seguintes colunas: RACE, RAIA, NOME, PROVA, SUBCATEGORIA, COLOCAcaO, CLUBE, ESTADO, FINAL, TEMPO, DATA.

**Arquivo Original**
| RACE | RAIA | NOME COMPLETO | PROVA |... |
| :---: | :---: | --- | --- | --- |
| 21 | 2 | Paulo Soares, João Silva, Marcos Medeiros, Carlos Eduardo | Four Skiff | ... |

**Arquivo Exportado**
| RACE | RAIA | NOME COMPLETO | PROVA |... |
| :---: | :---: | --- | --- | --- |
| 21 | 2 | Paulo Soares | Four Skiff |... |
| 21 | 2 | João Silva | Four Skiff |... |
| 21 | 2 | Marcos Medeiros | Four Skiff |... |
| 21 | 2 | Carlos Eduardo | Four Skiff |... |

## EnviarPContas
```
.EnviarPContas(caminho do arquivo excel)
```

Esta função utiliza a API do Sendgrid para enviar as Declarações de Prestação de Contas solicitadas pelos atletas. Ela toma como argumento o caminho de um arquivo Excel com a lista das solicitações (originado a partir do fomulário do Google Drive). A função busca as declarações no servidor local da CBR (pasta Marketing) e envia aos atletas.

As Declarações precisam estar salvad em PDF na pasta do servidor *Documentos> ... > Bolsa Atleta > Prestação de Contas*
