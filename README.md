# Módulo Bolsa Atleta
O módulo importa Panda e OS.

## SingleName
```
.SingleName(caminho do arquivo excel)
```

Esta função separa os resultados de barcos coletivos em linhas individuais no Excel. Deve ser indicado o caminho do arquivo atual como argumento. Um novo arquivo Excel é exportado.

O arquivo Excel deve conter as seguintes colunas: RACE, RAIA, NOME COMPLETO, PROVA, SUBCATEGORIA, COLOCAÇÃO, CLUBE, ESTADO, FINAL, TEMPO, DATA.

Os nomes dentro do campo NOME COMPLETO devem estar separados por vírgula.

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
