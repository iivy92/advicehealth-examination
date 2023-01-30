
# Advicehealth examanation

Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It’s a small town, so the mayor had a bright idea to limit the number of cars a person may possess. One
person may have up to 3 vehicles. The vehicle, registered to a person, may have one color, ‘yellow’, ‘blue’ or ‘gray’. And one of three models, ‘hatch’, ‘sedan’ or ‘convertible’. Carford car shop want a system where they can add car owners and cars. Car owners may not have cars yet, they need to be marked as a sale opportunity. Cars cannot exist in the system without owners.


## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/iivy92/advicehealth-examination
```

Entre no diretório do projeto

```bash
  cd advicehealth-examination
```

Se estiver usando macOS, execute o comando no terminal

```bash
  export DOCKER_DEFAULT_PLATFORM=linux/amd64
```

Use o Docker para subir os containers

```bash
  docker-compose up --build 
```

## Documentação da API

#### Cadastrar possivel dono de veiculo 

```http
  POST /v1/person/create
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `name` | `string` | **Obrigatório**. Nome do usuário |
| `document_number` | `string` | **Obrigatório**. Numero CPF do usuário |

#### Cadastrar veiculo 

```http
  POST /v1/vehicle/create
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `license_plate` | `string` | **Obrigatório**. Placa do veículo |
| `color` | `string` | **Obrigatório**. Cor do veículo |
| `model` | `string` | **Obrigatório**. Modelo do veículo |
| `owner_id` | `integer` | **Obrigatório**. ID do proprietario do veículo |

## Rodando os testes

Para rodar os testes, basta ativar a sua virtualenv e rodar o seguinte comando

```bash
  python3 -m pytest 
```
