# Desafio Técnico - GeoCorridas: Encontre o motorsita ideal

Voce foi contratado para desenvolver parte de um sitema de corridas semelhante ao Uber, com foco em performance e geolocalização. seu desafio será criar uma aplicação web em django capaz de :

---

## objetivo do desafio

desenvolver uma aplicação que permita ao cliente solicitar uma corrida e retorne o motorista mais bem avaliado dentro de um raio de 200 metros do motorista mais próximo disponivel até 10 km de distancia do cliente.

---

## Tecnologia obrigatórias

- Django + GeoDjango
- PostgreSQL com extensão PostGIS
- Docker e Docker Compose

---

## Funcionalidades esperadas

1. Modelagem do banco de dados com a tabela `Motorista` contendo:

- `nome` (CharField)
- `localizacao`(PointField com SRID 4326)
- `avaliacao`(FloatField de 0.0 a 5.0)

2. Endpoint POST em `/solicitar-corrida/` que:

- Recebe um JSON com latitude e longitude de cliente.
- Retorna o motorista mais bem avaliado dentre os que:
    - Estão em até 10km do ponto informado
    - Esxtão em até 200 metros do motorista mais próximo.

3. Docker Compose com dois serviços:

- `web`
- `db`

---

## O que será avaliado

- clareza e organização do código
- Uso correto de GeoDjango e operações especiais
- boas práticas com Docker
- Lógica para filtragem e seleção do motorista ideal
