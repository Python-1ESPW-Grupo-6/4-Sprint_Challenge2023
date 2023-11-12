# EPSW

## Equipe

- Fabrício Saavedra - 97631
- Guilherme Akio - 98582
- Guilherme Morais - 551981
- Matheus Motta - 550352
- Vinicius Buzato - 99125

# Dados

O projeto "Galo Weather" utiliza um arquivo JSON, variables.json, para simular dados pré-existentes de índice pluviométrico em diferentes bairros. Esses dados simulados são essenciais para avaliar as condições climáticas, determinando a propensão de cada bairro a alagamentos. No código Python, esses valores são utilizados em conjunto com parâmetros específicos, como a condição de bueiros entupidos e as previsões de chuva para o dia atual, para analisar e prever o risco de alagamento em tempo real.

## Funções Principais

# Consultar Bairros com Maior Risco

A função permite consultar informações sobre bairros específicos para saber se estão propensos a alagamentos devido às chuvas. Mostra se o bairro vai alagar ou não, com base nos dados de chuva hoje, índice pluviométrico e condição de bueiros. Armazena histórico de bairros pesquisados e notificações de bairros de risco.

# Notificar Bairro de Risco

Permite aos usuários notificar um bairro considerado em risco de alagamento. Solicita o nome do bairro e uma descrição da possível causa do alagamento. Armazena histórico de notificações de bairros e suas causas.

# Conhecer Mais sobre o Projeto

Oferece informações detalhadas sobre o projeto "Galo Weather", incluindo sua motivação, funcionalidades e objetivos. Permite ao usuário voltar ao menu principal após a leitura das informações.

# Sair

Permite ao usuário sair do programa com a opção de visualizar um resumo das operações realizadas. Armazena um relatório em um arquivo relatório.txt que inclui bairros pesquisados, notificações e causas de risco.