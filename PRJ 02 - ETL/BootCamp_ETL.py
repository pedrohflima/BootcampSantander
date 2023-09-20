import pandas as pd
import numpy as np

db_clients_xls = pd.read_excel('db_clientes.xlsx')

print(db_clients_xls)

print(type(db_clients_xls))

user_ids: list = db_clients_xls['ID'].tolist()
fx_etaria = db_clients_xls['FAIXA_ETARIA'].tolist()
renda = db_clients_xls['RENDA'].tolist()
patrimonio = db_clients_xls['PATRIMONIO'].tolist()
dividas = db_clients_xls['DIVIDAS'].tolist()

print(user_ids)
print(fx_etaria)
print(renda)
print(patrimonio)
print(dividas)

i = -1
user_score = []
for users in user_ids:
    score = 0
    i = i + 1
    client = user_ids[i]
    age = fx_etaria[i]
    income = renda[i]
    wealth = patrimonio[i]
    debts = dividas[i]
    if wealth == 0:
        alav = 1.1
    else:
        alav = (int(debts)/int(wealth))

    # Bloco if da idade
    if 18 <= age < 25:
        score += 0
    elif 26 <= age < 30:
        score += 1
    elif 30 <= age < 45:
        score += 2
    elif 46 <= age < 60:
        score += 3
    elif age >= 60:
        score += 1

    # Bloco if de renda
    if income <= 1500:
        score += 0
    elif 1501 < income <= 2250:
        score += 1
    elif 2251 < income <= 3600:
        score += 2
    elif 3601 < income <= 6000:
        score += 3
    elif income > 6001:
        score += 4

    # Bloco if de alavancagem (razão div/patrimonio)
    if alav > 1:
        score += -1
    elif 0.7 <= alav < 1:
        score += 0
    elif 0.5 <= alav < 0.7:
        score += 1
    elif 0.3 <= alav < 0.5:
        score += 2
    elif alav < 0.3:
        score += 3

    user_score.append(score)

# print(user_ids)
# print(user_score)

j = -1
for users in user_ids:
    j = j + 1
    client = user_ids[j]
    score = user_score[j]
    # print(client)
    # print(score)

    if score <= 2:
        print(f"Oferecer ao cliente {client}: Conta corrente básica e Cartão de Débito")
    elif 3 <= score <= 5:
        print(f"Oferecer ao cliente {client}: Conta corrente básica com limite cheque especial inicial e Cartão Crédito internacional")
    elif 6 <= score <= 8:
        print(f"Oferecer ao cliente {client}: Conta corrente intermediária com limite de cheque especial e período curto de isenção de taxas, Cartão Crédito exclusivo nível 1, serviços de investimentos gerais")
    elif 9 <= score <= 10:
        print(f"Oferecer ao cliente {client}: Conta corrente avançada com limite de cheque especial e período amplo de isenção de taxas, Cartão Crédito exclusivo nível 2, serviços de investimentos com acessor dedicado")