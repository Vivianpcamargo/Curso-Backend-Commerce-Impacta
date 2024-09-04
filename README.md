# :bookmark: Curso-Backend-Commerce-Impacta

:label: Tecnologia Principal: Python
<br> :bricks: Framework: Flask
<br> :luggage: Banco de Dados: SQLAlchemy
<br> :test_tube: Testes Unitários: Pytest
<br> :cloud: Nuvem: PythonAnywhere
<br> :page_facing_up: Padronização: pep8
<br> :book: Documentação: <a href=''> Postman

## :dart: Sobre

Curso com o objetivo de atuar no backend de um e-commerce fictício na disciplica Framework Full Stack da Faculdade Impacta.

## :building_construction: Instalação do projeto

- instalação do python na máquina:
```
sudo apt install python3-pip
```

- instalação de dependências necessárias:
```
pip3 install -r requirements.txt
pip3 install python-dotenv
```

## :bar_chart: Rodando

#### :test_tube: Local

- iniciar:
```
python3 run.py
```

#### :test_tube: Ambiente Virtual de Desenvolvimento

- iniciar:
```
python3 -m venv venv
```

- ativar:
```
source venv/bin/activate
```

- desativar:
```
deactivate
```

#### :test_tube: Pytest

- instalar pytest:
```
pip3 install pytest
```

- executar arquivo:
```
pytest <nome-arquivo>.py
```

## :door: Portas do Projeto

#### :label: Aplicação

http://localhost:5000/

* `GET /`
* `GET /timestamps`

`/carts`
* `GET /carts/`
* `GET /carts/:cart_code`
* `PUT /carts/:cart_code`

`/orders`
* `GET /orders/`
* `GET /orders/:order_id`
* `POST /orders/`

`/products`
* `GET /products`
