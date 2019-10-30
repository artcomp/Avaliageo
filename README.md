# Avaliageo


Um sistema para avaliar referências geográficas presentes em notícias a partir de um portal de notícias.


Este sistema foi desenvolvido como trabalho de conclusão de curso no curso de Engenharia de Computação na Universidade Federal de Ouro Preto.

## Objetivos

O objetivo do projeto sistema é gerar bases de dados geocodificadas a partir de informações geográficas presentes no corpo do texto da notícia. O sistema se divide em duas etapas: coleta de dados dos usuários e validação dos dados obtidos. Para a avaliação da confiabilidade dos dados fornecidos pelos usuários foi utilizado o coeficiente alfa de cronbach.

As bases obtidas durante a execução do projeto encontram-se na pasta `closedBases`.

### Desenvolvimento

  
As tecnologias utilizadas no projeto foram:
  * Servidor
    * Python 2.7
      * Flask
      * Jinga 2
    * Firebase
  
  * Cliente
    * HTML
    * CSS 3
      * Bootstrap
    * JavaScript

A implementação do sistema está dividida em três partes: 
  * web scrapping e geração do código web para as notícias (pŕé-processamento)
  * aplicação principal (sistema web)
  * validação (processamento dos dados dos usuários)
    
#### Execução

É esperado prévio conhecimento da estrutura dos projetos desenvolvidos com base no framework Flask para a compreensão da implementação.


Requisitos : 
 * Python 2.7
 * Pip
 * Virtualenv
 
Após a instalação dos requisitos acima, é necessário ativar o ambiente virtual do projeto. Para isso, entre do diretório do projeto e digite o seguinte comando:
 
 > source avaliageo/bin/activate
 
Agora, é necessário instalar as dependências do projeto:

  > pip install -r requirements.txt
 
Para a execução da primeira parte:
 > python generate_news_data.py
 
Para a segunda, digite : 
 > python flask_app.py
 
Para a terceira, digite : 
 > python files.py
 

 OBS: Para a utilização do Firebase foi necessário a utilização de dados pessoais(cartão de crédito) para manter a aplicação. Assim, será necessário criar uma conta no firebase para a aplicação em uma eventual reprodução deste projeto. A modificação será na no endereço da resectiva bucket do Firebase.

    
