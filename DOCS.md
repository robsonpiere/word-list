# Documentação Técnica #

## Criação da aplicação ##

Para a criação da api foi escolhido o framerwork **Flask**, pois é o framework python que possuo  familiaridade.

A aplicação foi construida utilizado o padrão *appication factory.*

Para os tests foi utilizada o módulo  **unittests**

A api foi disponibilizada no azure e horoku, também é possível utilizar adicionar em um container 
conforme arquivo readme.

A especificação da api pode ser encontrada no endpoint */docs/* ainda foi utilizado swagger

## Resolução do problema ##
A principal parte da resolução do problema se encontra no módulo *words* e segue o fluxo de execução:

 1. O texto é limpo removendo-se os caracteres especiais e transformado em minúsculo para evitar duplicade
 2. São removidos as *stopwords* (brasileiras) para cada texto é transoformado em uma lista de palavras *(list)*, cada item que for uma 
 stopword é removido o texto volta a ser uma *string*
 3. Para geração das listas de palavras também são utilizadas listas de strings
 4. Após a geração das listas de palavras, também é gerardo as listas de ocorrência também utlizando list
 5. Cada item gerado é adiciondo a um dicionário que pode ser filtrado na chamda da API

Foram utlizados mais objetos do tipo list, porque apesar dos sets já resolverem o problema de duplicadade, 
alteravam a ordem das palavras.

A api recebe em seu endpoint via post um json contendo os textos e um filtro de resultado (opcional)
e também retorna um json com os resultados (que podem ser removidos pelo filtro):

- textos
    -   Os textos enviados já limpos e com stopwords removidas
- listaDePalavras
    - A lista de palavras gerada para todos os textos
- listaDeDuasPalavras
    - A lista de duas palavras gerada pra todos os textos
- vetorDePalavras
    -  Os vetores de ocorrência de palavras para cada texto
- vetorDeDuasPalavras
    -  Os vetores de ocorrência de palavras para cada texto


## Tecnlogias Utilizadas ##

|          Nome         	|                                   Descrição                                  	|
|:---------------------:	|:----------------------------------------------------------------------------:	|
|   Visual Studio Code  	| Editor de Texto utilizado para criação dos scripts de workflow               	|
| Py Charm Professional 	| IDE utilizada para desenvolvimento                                           	|
|   Docker for Windows  	| Utilizado para testar um container contendo a aplicação                      	|
|         WSL 2         	| Utilizado GIT e ssh + gpg para assinatura dos commits                        	|
|         Python        	| Python para windows versão 3.8                                               	|
|         GitHub        	| disponibilizar o fonte e executar workflows de teste e deploy (git hub actions)|
|        Codecov        	| Utilizado para subir a cobertura de testes do fonte                          	|
|         Azure         	| Utilizado para hospedar a aplicação (camada gratuita)                       	|
|         Heroku        	| Utilizado para hospedar a aplicação (camada gratuita)                       	|    
                                                      	
                                                      	
### Agradecimentos ###

Agradeço a empresa pela disponibilização do teste e teste e pela oportunidade.
A construção da aplicação me ajudou a testar novas tecnologias e adquirir novos conhecimentos.

Todo feedback será bem vindo. Sempre podemos melhorar :grimacing: :bug:

Obrigado!







