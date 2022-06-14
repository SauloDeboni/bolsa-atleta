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
.EnviarPContas(ano das solicitações, data do arquivo)
```
Esta função utiliza a API do Sendgrid para enviar as Declarações de Prestação de Contas solicitadas pelos atletas. Ela toma dois argumentos: ano do arquivo das solicitações e data do arquivo Excel com a lista das solicitações (originado a partir do fomulário do Google Drive). A função busca as declarações no servidor local da CBR (pasta Marketing) e envia aos atletas.

**Argumentos**<br>
- Ano da Solicitação: formato *aaaa*. Exemplo: 2022<br>
- Data do Arquivo: formato *aaaa-mm-dd*. Exemplo: 2022-06-08

**API SendGrid**<br>
Para o módulo funcionar, é necessário setar a API do SendGrid nas variáveis do sistema.<br>
- set SENDGRID_API_KEY = *código da API*

**Observações:**
- As Declarações precisam estar salvas em PDF na pasta do servidor:<br>*Documentos> ... > Bolsa Atleta > Prestação de Contas*
- A função retorna a lista dos e-mails enviados.

**Exemplo:**
```
EnviarPContas(2022, 2022-06-08)

Enviado para emailteste1@gmail.com
Enviado para emailteste2@gmail.com
Enviado para emailteste3@gmail.com
```
