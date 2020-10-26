# word-list

[![Testing and Deploy](https://github.com/robsonpiere/word-list/workflows/Testing%20and%20Deploy/badge.svg?branch=main)](https://github.com/robsonpiere/word-list/actions)
[![codecov](https://codecov.io/gh/robsonpiere/word-list/branch/main/graph/badge.svg?token=DT6HKTDBO4)](https://codecov.io/gh/robsonpiere/word-list)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Flask](https://img.shields.io/badge/flask-v1.1.2-green)](https://flask.palletsprojects.com/en/1.1.x/)

[![Heroku](https://img.shields.io/badge/-Heroku-430098?logo=heroku&color=430098&style=for-the-badge)](https://lista-de-palavras.herokuapp.com/docs)
[![Azure](https://img.shields.io/badge/-Azure-008AD7?logo=microsoft&color=008AD7&style=for-the-badge)](https://lista-de-palavras.azurewebsites.net/docs)

Links: 
 - [Documentação técnica](informacoes.pdf)

## Rodando o projeto ##

### Localmente ###


1 - Ativar seu ambiente virtual de preferência

2 - Instalar as dependências

```bash
pip install -r requirments txt
``` 

3 - Rodar o projeto

<details>
  <summary>Linux</summary>
  
```bash
export FLASK_APP=hello.py,
export MONGO_STRING_CONNECTION="mongodb://<dbuser>:<dbpassword>@<host>:<port>/lista-de-palavras"
flask run
``` 
</details>

<details>
  <summary>Windows</summary>
  
```powershell
PS C:\path\to\app> $env:FLASK_APP = "main.py"
PS C:\path\to\app> $env:MONGO_STRING_CONNECTION = "mongodb://<dbuser>:<dbpassword>@<host>:<port>/lista-de-palavras"
PS C:\path\to\app> flask run
``` 
</details>

### Em container ##
```docker
docker build -t word-list ./
docker run -d -p 80:80  -e MONGO_STRING_CONNECTION='mongodb://<dbuser>:<dbpassword>@<host>:<port>/lista-de-palavras' word-list
``` 
docker build -t word-list ./

## Descrição do problema ##

**Prova Prática**

**Vetor de Palavras**

Várias aplicações de processamento de linguagem natural necessitam que o texto seja formatado de forma estruturada, diferente da linguagem natural. Uma solução para isso é organizar as palavras do texto em um vetor que represente o documento em termos das palavras que ocorrem no mesmo.

Como exemplo, suponha dois documentos distintos contendo os textos abaixo:

**texto1.txt:**&quot;Falar é fácil. Mostre-me o código.&quot;

**texto2.txt:**&quot;É fácil escrever código. Difícil é escrever código que funcione.&quot;

Esses dois textos possuem a seguinte lista de palavras únicas (ignorando _case_ e pontuação):

_1. falar_

_2. é_

_3. fácil_

_4. mostre_

_5. me_

_6. o_

_7. código_

_8. escrever_

_9. difícil_

_10. que_

_11. funcione_

Ou seja, são 11 palavras distintas no **vocabulário** de dois textos com 17 palavras no total.

O vetor de palavras então calcula, para cada documento, a quantidade de vezes que cada palavra do vocabulário aparece. Para isso, podemos representar o vocabulário como um vetor de tamanho N (onde N é o tamanho do vocabulário), e cada texto terá o seu vetor com a quantidade de vezes que a palavra k do vocabulário aparece inserida na posição k do vetor. Como resultado, teremos:

texto1: [1,1,1,1,1,1,1,0,0,0,0]

texto2: [0,2,1,0,0,0,2,2,1,1,1]

Uma alternativa mais elaborada é fazer um vocabulário com 2 palavras (_2-gram_) na sequência:

_1. falar é_

_2. é fácil_

_3. fácil mostre_

_4. mostre me_

_5. me o_

_6. o código_

_7. fácil escrever_

_8. escrever código_

_9. código difícil_

_10. difícil é_

_11. é escrever_

_12. código que_

_13. que funcione_

Nesse caso, os vetores de palavras de cada documento do exemplo seriam de tamanho 13 e conteriam os seguintes valores:

texto1: [1,1,1,1,1,1,0,0,0,0,0,0,0]

texto2: [0,1,0,0,0,0,1,2,1,1,1,1,1]

**Problema**

Desenvolva uma API REST que permita a um usuário enviar textos de entrada, e que gere como resultado o vocabulário formado pelas palavras dos textos e o vetor de palavras para cada arquivo considerando dois cenários:

1. o vocabulário é composto de palavras isoladas.

2. o vocabulário é composto de grupos de duas palavras em sequência (_2-gram_).

Cabe ressaltar que uma palavra é considerada como uma sequência de letras e dígitos, começando com uma letra. Remova palavras que não agregam muito valor do vocabulário, chamadas _stop-words,_ como &quot;o&quot;, &quot;a&quot;, &quot;que&quot;, &quot;me&quot;, etc.

O vocabulário deve ser criado a partir das palavras de todos os N textos.

**Entrada**

O usuário poderá enviar textos via api REST

**Retorno**

Após o envio dos textos, o usuário poderá solicitar os seguintes resultados:

1. O vocabulário completo formado pelas palavras isoladas;

2. O vocabulário completo formado por grupos de 2 palavras em sequência (2-gram);

3. Os N vetores de palavras de todos os documentos, considerando o vocabulário formado pelas palavras isoladas;

4. Os N vetores de palavras de todos os documentos, considerando o vocabulário formado por grupos de 2 palavras em sequência (2-gram);

**Entregas:**

1. Entregar uma documentação técnica sobre as estruturas de dados escolhidas para resolver o problema e as ferramentas/tecnologias utilizadas para o desenvolvimento da API

2. O código fonte deve ser disponibilizado em um repositório público do GitHub (http://github.com ). Será levado em consideração a frequência dos commits e a separação temática entre eles.

(Opcional)

1. Salvar um histórico de utilização dos serviços em um banco de dados. Ou seja, toda requisição ao serviço deverá ser registrada em um banco de dados, com detalhes da mesma, para que possa ser consultada. Informe qual banco escolhido e envie junto um dump de estrutura e as configurações de conexão necessárias.

2. Faça testes unitários e/ou de integrações.

3. Desenvolver a API permitindo o usuário enviar N Arquivos de entrada.

4. Disponibilizar a API em um serviço Cloud da AWS ou do Google.

