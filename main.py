"""
Objetivo do projeto:

Uma empresa está oferecendo uma viagem ao vendedor que bater a meta do mês (R$ 55.000). Nosso programa irá entrar
nas planilhas (Excel) onde tem as informações de venda de cada vendedor, e ver se algum deles bateu a meta.
Se sim, nós iremos enviar um SMS com os dados do vendedor, senão, não iremos fazer nada.
"""
import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6abb78d30a8df50eccd8873aa4776b08"

# Your Auth Token from twilio.com/console
auth_token = "93abef8df7d73102918f105db629285f"

client = Client(account_sid, auth_token)

# -------------------------------------------------------------------------------------
# Passo a passo de solução:
# -------------------------------------------------------------------------------------

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
    if (tabela_vendas['Vendas'] > 55000).any():
        # Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'\nNo mês de {mes} alguém bateu a meta! foi o {vendedor} com um total de {vendas:,.2f} em vendas!\n')
        message = client.messages.create(
            to="+5511956876830",
            from_="+17578957945",
            body=f'No mês de {mes} alguém bateu a meta! foi o {vendedor} com um total de {vendas:,.2f} em vendas!')
        # print(message.sid + '\n')
    else:
        print(f'Nenhum vendedor encontrado no mês de {mes}.')
