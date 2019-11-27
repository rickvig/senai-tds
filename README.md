# Técnico em Desenvolvimento de Sistemas

## Programa
Objetivo Geral: Propiciar desenvolvimento de capacidades técnicas e de gestão requeridas para
desenvolvimento de sistemas por meio de linguagem de programação, de acordo padrão de qualidade,
robustez, integridade e segurança.

### Conhecimentos:

Metodologia de desenvolvimento de sistemas
- Tipos
- Características
- Ferramentas
- Aplicabilidade

Técnicas de definição de prazos
- Ferramentas de tarefas

Linguagem de programação
- Tipos
- Ferramentas Boas práticas
- Bibliotecas e API's
- Frameworks
- Multiplaformas
- Integração de sistemas

Padrões de projetos (DesignPatterns)

Gerência de configuração
- Ferramentas
- Controle de versão
- Rastreabilidade
- Documentação

Princípios da comunicação profissional e postura

Comportamento e Trabalho em Equipe
- Situações de conflito;
- Normas de convivência;
- Fatores de satisfação.

Organização do trabalho
- Estruturas hierárquicas;
- Sistemas administrativos;
- Controle de atividades.

Planejamento Estratégico: conceitos

Visão Sistêmica
- Conceito;
- Microcosmo e macrocosmo;
- Pensamento sistêmico.


### Capacidades Técnicas:

2.1 .1 Seguindo metodologia de desenvolvimento
- Reconhecer requisitos de qualidade, integridade, usabilidade e segurança da informação
- Definir tecnologias de acordo com os requisitos não funcionais

2.1 .2 Adotando técnicas e métodos de desenvolvimento (boas práticas, padrões de desenvolvimento, depuração, documentação de sistemas, versionamento, repositório, rastreabilidade ...)
- Reconhecer tipos de linguagem de acordo com as multiplaformas 
- Selecionar linguagem programação de acordo com os requisitos
- Integrar sistemas multiplaformas por meio da linguagem de programação
- Aplicar linguagem de programação por meio de API ́s, bibliotecas, frameworks na construção de rotinas de software

2.1 .3 Utilizando linguagens de programação
- Identificar metodologia de desenvolvimento de sistemas 
- Aplicar metodologia de desenvolvimento de acordo com o escopo do projeto 
- Selecionar ferramentas de gerênciamento na aplicação da metodologia
- Definir cronograma de atividades, de acordo com a metodologia


## Aula 1 - POO - Porgamação Orientada a Objetos com Python
- Linguagem Python - fundamentos
- Abstração de dados
- Classes, objetos e métodos
- Herança e Polimorfismo


## Aula 2 - SCM com Git e finalizando OO
- Repositório Git
- Finalizar exemplo de herança e aplicar exercício de contaBancaria


## Aula 3 - Desenvolvimento Web (fundamentos web, HTML, CSS, JS - ) e conceitos MVC e MTV
- Repositório Git
- Finalizar exemplo de herança e aplicar exercício de contaBancaria
- Overview - Tipos de sistemas 
    - Dasktop
        - Cada linguagem possui sua ferramentas
        - Swing, JavaFX - Java
        - Delphi
        - C#
        - Python
        - Electron - JS, 
    - Web 
        - PHP - Facebook / Wordpress
        - Infinitos frameworks de todas as linguagens
        - Sistemas mais usado nos ultimos 10 anos 
    - Mobile 
        - Android
        - IOS
        - Hibridos
            - Xamarim
            - Webapps 
                - Phonegep
                - Progressivewebapp - PWA
                - Native
                - varios frameworks    
    - Embebed
        - C, Assemble, Python, C++
    - Games, 
    - IA?,
        - Sistemas de Recomendação, Machine Learning (processamentos de imagens, redes neurais), Automação, Robótica, - - - Sistemas cognitivos (IBM)

- Sistemas Web
    - Fundamentos da Web
    - Desenvolvimento Web


## Aula 4 - Desenvolvimento Web (fundamentos web, HTML, CSS, JS - ) Parte II 
- Finalizar fundamentos web
- exercicio surpresa
    

## Aula 5 - Conceitos MVC e MTV Introdução ao Danjo Framework (Web Framework)
- Corrigir exercicio
- Criar repositporios para equipes
- Conceitos MVC e MTV
- Django
    - Wiki
    - fullstack framework
    - site oficial
    - https://www.shuup.com/django/25-of-the-most-popular-python-and-django-websites/

- python-venv

        $ python -m venv meuApp
        $ source meuApp/bin/activate
        $ pip install django

- Pluguin VSCode
    - Pytho DonJayanmanne
    - Django Template/Snipptes bibhasdn

- Start Django project
        
        $ django-admin startproject meuApp

- Entendendo e rodando primeiro projeto Django
    - Arvore de arquivos

            $ python manager.py migrate
            $ python manage.py runserver
            $ python manage.py createsuperuser

- Django Admin
    - Usuários
    - Grupos
    - login/logout

Django req/res cycle img


## Aula 6 - Finalizar exemplo Django - inicializar projeto petshop

### Django Admin
- app CRUD's core

### Apps
- *SQLite*
    
        $ python manage.py startapp <sua-app>

- add app em INSTALLED_APPS (settings.py)
    
        $ python manage.py runserver

- Criar model
        
        $ python manage.py makemigrations
        $ python manage.py migrate

- Personalizando Django
    - fields
    - list_display
    - list_filter
    - search_fields

### Projeto PETSHOP
- Criar um repo no git hub para cada equipe
- Start no projeto
- Criação dos CRUD de admin
- Criação das classes e seus relacionamentes de models (DER)


# Aula 7 - Continuação Projeto petshop

### PETSHOP
- Trabalhando com versionamento
- Criação das classes e seus relacionamentes de models (DER)


# Aula 8

### PETSHOP
- Trabalhando com versionamento
- Criação das classes e seus relacionamentes de models (DER) - em equipe


# Aula 9

### PETSHOP
- Trabalhando com versionamento
- Criação das classes e seus relacionamentos de models (DER) - DEFINITIVO PARTE I
- Exercício de desenvolvimento dos modelos e suas regras


# Aula 10

### PETSHOP
- Trabalhando com versionamento
- Criação das classes e seus relacionamentes de models (DER) - DEFINITIVO PARTE II
- Correção do exercício de desenvolvimento dos modelos e suas regras no formato Code Review


# Aula 11

### PETSHOP
- Trabalhando com versionamento - adicionando novo remote no repositório de do projeto apontando para o repo base
- Classes e seus relacionamentes ManyToOne com ForiengnKey e _set - DEFINITIVO PARTE III
- Apresentação de teste de software com TDD (Test Driven Development)


# Aula 12
- Apresentação do teste de software com TDD - https://twitter.com/unclebobmartin/status/1189574793579941889

### PETSHOP
- Trabalhando com versionamento - atualizando o repositório
- Criação das classes e seus relacionamentes de models (DER) - DEFINITIVO PARTE IV 
    - financeiro-estoque


# Aula 13

### PETSHOP
- Trabalhando com versionamento - atualizando o repositório
- Criação das classes e seus relacionamentes de models (DER) - DEFINITIVO PARTE IV 
    - finalizar financeiro-estoque


# Aula 14

### PETSHOP
- Trabalhando com versionamento - atualizando o repositório
- Criação das classes e seus relacionamentes de models (DER) - DEFINITIVO PARTE IV 
    - finalizar financeiro-estoque

### App Code
- Brincado com nosso model
        
        $ python manage.py shell


# Aula 15
- Revisão de Programação
    - Programação estruturada


# Aula 16
- Revisão de Programação
    - Programação estruturada


# Aula 17
- Revisão de Programação
    - Programação OO


# Aula 18

### PETSHOP
- Trabalhando com versionamento - atualizando o repositório (repositório refatorado)
- Criação das classes e seus relacionamentes de models (DER) - DEFINITIVO PARTE IV 
    - Implementando ultima regra de negócio de movimentação de estoque para execução de ordem de serviço via TDD


# Aula 19
- Introdução a urls, views e templates (MTV - Django)

### Django req/res cycle img

![django-life-cycle](https://i.stack.imgur.com/rLfSC.jpg)


### PETSHOP
#### Url Partterns, Views
- url.py e views.py
- functions based view X class based views
- https://docs.djangoproject.com/en/2.2/topics/http/urls/

#### Templates
- 1° TEMPLATES em settings (templates)
- 2° criar pasta na raiz com nossos templates (index.hmtl)
- 3° criar função na view.py com retorno 'render' para o arquivo de templete (index.hmtl)


# Aula 20

### PETSHOP
- Loops for no Jinja - Exemplo da lista de animais
- Arquivos estáticos da template (CSS, JS, Vendor, etc..)
- Herança de templates com blocks - incluir template modelo do Bootstap
- Consulta no models para apresentar na view


- Template aplicada no projeto:
https://startbootstrap.com/previews/sb-admin-2/



# Equipes:

## Time 1 - Frente de caixa (Cadasros)
- Yuri
- Gustavo
- Ricardo
- Luan
## Time 2 - Banho e tosa
- Henrique
- Lucas
- Victor
- Carlos
## Time 3 - Financeiro e estoqe
- Andriw
- Diego
- Rodrigo
