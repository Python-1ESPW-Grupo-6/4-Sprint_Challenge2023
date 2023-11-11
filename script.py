#lista de bairros que tendem a alagar em época de chuva intesa (verão)
# https://imoveis.estadao.com.br/noticias/saiba-quais-sao-os-bairros-mais-suscetiveis-a-enchentes-e-alagamentos-em-sao-paulo/

# Fabrício Saavedra - 97631
# Guilherme Akio - 98582
# Guilherme Morais - 551981
# Matheus Motta - 550352
# Vinicius Buzato - 99125

import os
from datetime import datetime
import sys
import json

json_file_path = 'variables.json'  # Replace with the actual filename
with open(json_file_path, 'r') as json_file:
    dados = json.load(json_file)

# Extract chuva_hoje and bueiro_entupido values from the JSON data
chuva_hoje = dados['valores_chuva']['Mooca']  # Replace 'Mooca' with the desired key
bueiro_entupido = dados['outras_variaveis']['bueiro_entupido']

# Dicionário que associa bairros a meses de risco de alagamento
bairros_alagados = {
    'Mooca': 9,
    'Vila Prudente': 14,
    'Tatuape': 8,
    'Belenzinho': 15,
    'Bela Vista': 12,
    'Casa Verde': 7,
    'Vila Leopoldina': 13,
    'Cidade Jardim': 11,
    'Chacara Santo Antonio': 9,
    'Capao Redondo': 10
}

# Listas para armazenar histórico de pesquisa de bairros
bairro_pesquisados = []
bairro_pesquisados_alagados = []

# Listas para armazenar histórico de notificações de bairros e causas
notificacao_bairro = []
causa_risco = []

# Variavel com o arquivo
nome_arquivo = 'relatório.txt'

def traco():
    """
    Imprime uma linha de traço para formatação.
    """
    print('-' * 40)

def error():
    """
    Exibe uma mensagem de erro formatada.
    """
    traco()
    print('Opção inválida! Tente novamente!')
    traco()

def consultar_bairro(bairro_user):
    """
    Consulta informações sobre um bairro específico.
    
    Args:
        bairro_user (str): O nome do bairro a ser consultado.
    """
    if bairro_user in dados['valores_chuva']:
        chuva_hoje = dados['valores_chuva'][bairro_user]
    
    if bairro_user in bairros_alagados:
        if bairros_alagados[bairro_user] <= chuva_hoje:
            print('')
            traco()
            print(f'O bairro {bairro_user} VAI ALAGAR hoje devido a fortes chuvas. Tome cuidado e evite a região!')
            traco()
            print('')
            bairro_pesquisados_alagados.append(bairro_user)
        elif (bairros_alagados[bairro_user]*0.75) >= chuva_hoje and bueiro_entupido == True:
            print('')
            traco()
            print(f'O bairro {bairro_user} VAI ALAGAR hoje devido a fortes chuvas. Tome cuidado e evite a região!')
            traco()
            print('')
            bairro_pesquisados_alagados.append(bairro_user)
        else:
            print('')
            traco()
            print(f'O bairro {bairro_user} NÃO vai alagar hoje, fique tranquilo!')
            traco()
            print('')
            bairro_pesquisados.append(bairro_user)
    else:
        print('')
        print('Bairro não encontrado, verifique se contém abreviação ou erro ortográfico')
        print('')

def notificar_bairro(notificacao_area, causa):
    """
    Registra uma notificação sobre um bairro de risco.

    Args:
        notificacao_area (str): O nome do bairro a ser notificado.
        causa (str): Descrição da possível causa de risco no bairro.
    """
    notificacao_bairro.append(notificacao_area)
    causa_risco.append(causa)
    print('')
    print('Obrigado pela notificação, voltando para o menu de Notificações!')
    print('')

def consultar_bairros():
    """
    Função que permite ao usuário consultar bairros com maior risco de alagamento.

    Esta função exibe um menu interativo que permite ao usuário consultar bairros específicos para saber se eles vão alagar. O usuário pode selecionar um
    bairro para consultar e receber informações sobre o risco de alagamento naquele bairro durante
    o dia atual.
    """
    traco()
    print('Opção (1 - Consultar bairros com maior risco) escolhida!')
    traco()
    print('')
    while True:
        print('Consultar bairros')
        print('')
        print('1 - Consultar um bairro')
        print('2 - Voltar')
        print('')
        try:
            menu2 = int(input('Insira o número referente ao local que quer ir: '))
            print('')
            if menu2 == 1:
                print(f'Bairros cadastrados: {list(bairros_alagados.keys())}')
                print('')
                bairro_user = input('Digite o bairro que queira consultar: ').title()
                consultar_bairro(bairro_user)
            elif menu2 == 2:
                print('Ok, voltando para o menu!')
                print('')
                break
            else:
                error()
                print('')
        except ValueError:
            error()
            print('')

def notificar():
    """
    Função que permite ao usuário notificar um bairro de risco de alagamento.

    Esta função exibe um menu interativo que permite ao usuário notificar um bairro que ele considera
    estar em risco de alagamento. O usuário pode fornecer o nome do bairro e uma descrição da possível
    causa do alagamento.

    """
    traco()
    print('Opção (2 - Notificar algum bairro de risco) escolhida!')
    traco()
    print('')
    while True:
        print('Notificação')
        print('')
        print('1 - Mandar uma Notificação')
        print('2 - Voltar')
        print('')
        try:
            menu3 = int(input('Insira o número referente ao local que quer ir: '))
            print('')
            if menu3 == 1:
                notificacao_area = input('Notifique qual o bairro de risco: ')
                causa = input('Se souber qual poderia ser a causa de uma possível enchente, pode descrevê-la para nós? ')
                notificar_bairro(notificacao_area, causa)
            elif menu3 == 2:
                print('Ok, voltando para o menu!')
                print('')
                break
            else:
                error()
                print('')
        except ValueError:
            error()
            print('')

def conhecer_projeto():
    """
    Função que fornece informações sobre o projeto "Galo Weather".

    Esta função exibe informações detalhadas sobre o projeto "Galo Weather", incluindo sua motivação,
    funcionalidades e objetivos. O usuário pode ler sobre o projeto e, em seguida, escolher voltar ao menu
    principal.
    """
    traco()
    print('Opção (3 - Conheça mais sobre o projeto) escolhida!')
    traco()
    print('')
    print('Um pouco sobre a história do nosso projeto:')
    print('')
    print("Nosso projeto surgiu da preocupação com o crescente número de enchentes nas áreas urbanas e seus efeitos catastróficos sobre as pessoas. Sabemos que o Brasil é um país com muitas regiões vulneráveis, que sofrem com chuvas intensas que causam inundações, deslizamentos e perdas materiais e humanas. E esse problema não é exclusivo do nosso país, muitas outras cidades no mundo sofrem com essa mesma questão.\n")
    print("Por isso, criamos uma plataforma que utiliza dados em tempo real para prever alagamentos e identificar áreas de risco. Com um algoritmo de previsão de alagamento e um mapeamento das áreas de risco, nossa plataforma envia alertas em tempo real para a população e as autoridades responsáveis, permitindo medidas preventivas antes mesmo da ocorrência das enchentes.\n")
    print("Além disso, temos um hardware de monitoramento que utiliza dados de previsão de chuva e índice pluviométrico para verificar as condições dos bueiros em regiões pré-determinadas. As informações coletadas são armazenadas e repassadas aos órgãos responsáveis, permitindo uma atuação mais rápida e eficiente em caso de problemas.\n")
    print("Temos em mente que a chave para resolver problemas complexos como as enchentes urbanas está em colocar as pessoas em primeiro lugar. E é exatamente isso que nossa plataforma faz: utiliza tecnologia de ponta para proteger e salvar vidas, preservando o bem-estar da população e das comunidades afetadas pelas enchentes.\n")
    print('')
    while True:
        voltar_menu = input('Quando quiser voltar para o menu apenas digite "voltar": ').lower()
        print('')
        if voltar_menu == 'voltar':
            break
        else:
            print('Opção inválida! Tente novamente!')
            print('')

def sair():
    """
    Função que permite ao usuário sair do programa.

    Esta função exibe um menu que permite ao usuário confirmar se deseja sair do programa ou voltar ao menu
    principal. Se o usuário optar por sair, o programa será encerrado e um resumo das operações realizadas
    será exibido.
    """
    while True:
        sair_confirmacao = input('Tem certeza que quer sair? (sim/não) ').lower()
        print('')
        if sair_confirmacao == 'sim':
            traco()
            print('Obrigado pelo seu acesso!')
            traco()
            print('')
            # Histórico de uso da aplicação
            if not bairro_pesquisados and not notificacao_bairro:
                sys.exit()

            timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

            nova_atualização = f'Atualização em {timestamp}:\n'

            if os.path.exists(nome_arquivo):
                with open(nome_arquivo, 'a') as arquivo:
                    arquivo.write(nova_atualização)
                    
                    if bairro_pesquisados or bairro_pesquisados_alagados:
                        arquivo.write('Bairros pesquisados:\n\n')
                        if bairro_pesquisados:
                            for bairro in bairro_pesquisados:
                                arquivo.write(f'{bairro} não vai alagar!\n')
                        if bairro_pesquisados_alagados:
                            for bairro in bairro_pesquisados_alagados:
                                arquivo.write(f'{bairro} vai alagar!\n')
                    
                    if notificacao_bairro:
                        arquivo.write('\nNotificações adicionadas:\n\n')
                        for bairro, causa in zip(notificacao_bairro, causa_risco):
                            arquivo.write(f'Bairro: {bairro}\n')
                            arquivo.write(f'Causa: {causa}\n\n')
            else:
                with open(nome_arquivo, 'w') as arquivo:
                    arquivo.write(nova_atualização)

                    if bairro_pesquisados or bairro_pesquisados_alagados:
                        arquivo.write('Bairros pesquisados:\n\n')
                        if bairro_pesquisados:
                            for bairro in bairro_pesquisados:
                                arquivo.write(f'{bairro} não vai alagar!\n')
                        if bairro_pesquisados_alagados:
                            for bairro in bairro_pesquisados_alagados:
                                arquivo.write(f'{bairro} vai alagar!\n')
                    
                    if notificacao_bairro:
                        arquivo.write('\nNotificações adicionadas:\n\n')
                        for bairro, causa in zip(notificacao_bairro, causa_risco):
                            arquivo.write(f'Bairro: {bairro}\n')
                            arquivo.write(f'Causa: {causa}\n\n')
                    
            if bairro_pesquisados or bairro_pesquisados_alagados:
                traco()
                print(f'Bairros pesquisados: ')
                traco()
                if bairro_pesquisados:
                    for bairro in bairro_pesquisados:
                        print(f'{bairro} não vai alagar!')
                        print('')
                if bairro_pesquisados_alagados:
                    for bairro in bairro_pesquisados_alagados:
                        print(f'{bairro} vai alagar!')
                        print('')

            if notificacao_bairro:
                traco()
                print('Notificações adicionadas:')
                traco()
                for bairro, causa in zip(notificacao_bairro, causa_risco):
                    print(f'Bairro: {bairro}')
                    print(f'Causa: {causa}')
                    print('')
            sys.exit()
        elif sair_confirmacao == 'não':
            print('Ok, voltando para o menu!')
            print('')
            break
        else:
            error()
            print('')

while True:
    # Exibe um cabeçalho e menu para o usuário
    traco()
    print('Bem-vindo ao projeto "Galo Weather", sistema preventivo para alagamentos nas vias urbanas')
    traco()
    print('')
    print('1 - Consultar bairros com maior risco')
    print('2 - Notificar algum bairro de risco')
    print('3 - Conheça mais sobre o projeto')
    print('4 - Sair')
    print('')
    try:
        # Solicita uma escolha numérica do usuário
        menu = int(input('Insira o número referente à parte que quer acessar: '))
        print('')

        # Com base na escolha do usuário, chama as funções apropriadas
        if menu == 1:
            consultar_bairros()
        elif menu == 2:
            notificar()
        elif menu == 3:
            conhecer_projeto()
        elif menu == 4:
            sair()
        else:
            # Trata erros de escolha inválida
            error()
            print('')
    except ValueError:
        # Trata erros de entrada inválida (não numérica)
        print('')
        error()
        print('')