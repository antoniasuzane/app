# CRUD usando Python e framework Flask

Nosso objetivo é projetar uma API RESTful de back-end, desenvolvida com Python e Flask, para um único recurso -biblioteca

  • A própria API deve seguir os princípios de design RESTful, usando os verbos HTTP básicos: GET, POST, PUT e DELETE.
  
  •Também configuraremos um aplicativo front-end com o Vue que consome a API de back-end:


# Instalação
To use this template, your computer needs:

  * Vue.js
  * npm
  * Axios - Para conectar o aplicativo Vuedo lado do cliente ao aplicativo Flask de back-end, podemos usar abibliotecaaxiospara enviar solicitações AJAX
  * Python 3.7.1
  * Flask 1.0.2
  * Flask-WTF
  * Passlib
  * MySQL - XAMPP Server
  * mysql-connector-python-8.0.13 (https://dev.mysql.com/downloads/connector/python/)

# Running the app
python app.py

CRUD usando Python e framework Flask
O que é framework Flask?
Segundo a documentação, o Flask é um micro-framework e baseado na biblioteca WSGI Werkzeug e na biblioteca de Jinja2. Flask tem a flexibilidade da linguagem de programação Python e provê um modelo simples para desenvolvimento web. Uma vez importando no Python, Flask pode ser usado para economizar tempo construindo aplicações web.

O primeiro passo a se fazer é instalar o pip que é o gerenciador de pacotes do python.


pip install Flask

Depois é necessário ativar o virtualenv, para isso acesse o diretório cd /crud e depois digite source bin/active.

Agora, acesse o diretório pelo comando cd /projeto.

Por fim, digite o comando em seu terminal:


python app.py

Pronto! A aplicação Flask já está rodando. Abra seu navegador e digite localhost:5000.
