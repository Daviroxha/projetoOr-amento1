import streamlit as st
import datetime
import math
import os

def data_Valida(ano, mes, dia):
    try:
        datetime.datetime(ano, mes, dia)
        return True
    except ValueError:
        return False

def data_no_alcance(ano, mes, dia, start_data, fim_data):
    data_check = datetime.datetime(ano, mes, dia)
    return start_data <= data_check <= fim_data

st.set_page_config(
    page_title="Orçamento Para festas",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="expanded",)

# Título e descrição
st.title("Lets Fest")
st.write("Faça o orçamento para sua festa")

# Obter a data do usuário
st.header('Selecione a data da Festa')
data_selecionada = st.date_input('')

ano, mes, dia = data_selecionada.year, data_selecionada.month, data_selecionada.day

## Verificar validade
#if data_Valida(ano, mes, dia):
#    st.write("A data é Válida")
#else:
#    st.write("A data é inválida.")
#
## Intervalo de datas
#data_inicio = datetime.datetime(2023, 10, 1)
#data_fim = datetime.datetime(2023, 10, 31)
#
## Verificar se está dentro do intervalo
#if data_no_alcance(ano, mes, dia, data_inicio, data_fim):
#    st.write("A data está dentro do intervalo.")
#else:
#    st.write("A data está fora do intervalo.")

valor_reserva_data = 100
valor_por_crianca = 48

st.header('Escolha a Quantidade de Crianças')
numero_crianca = st.slider("",6, 100)

calculo_festa = valor_por_crianca*numero_crianca

tempo_festa = st.radio(
    "Escolha o tempo que deseja para a festa",
    ["1 hora", "2 horas", "3 horas", "4 Horas"])

#verificador de tempo
if tempo_festa == "1 hora":
    calculo_festa = calculo_festa * 1.5
elif tempo_festa == "2 horas":
    calculo_festa = calculo_festa * 2
elif tempo_festa == "3 horas":
    calculo_festa = calculo_festa * 2.5
else:
    calculo_festa = calculo_festa * 3

st.header("**Atrações**")

atra1, atra2 = st.columns(2)

with atra1:
    atracao0 = st.checkbox("Games")
    atracao1 = st.checkbox("Slime")
    atracao2 = st.checkbox("Roupinha de Boneca")
    atracao3 = st.checkbox("Origami")

with atra2:
    atracao4 = st.checkbox("Pintura")
    atracao5 = st.checkbox("Just Dance")
    atracao6 = st.checkbox("Miçangas")

soma_atracao = atracao0 + atracao1 + atracao2 +atracao3 + atracao4 + atracao5 + atracao6
calculo_festa = calculo_festa + (soma_atracao * 25)


st.header("**Alimentação**")
alimentacao0 = st.checkbox("Pizza e Bebida")
alimentacao1 = st.checkbox("Hamburguer e Bebida")

if alimentacao0 == True:
    calculo_festa = calculo_festa + 90
elif alimentacao1 == True:
    calculo_festa = calculo_festa + 150
elif alimentacao0 == True and alimentacao1 == True:
    calculo_festa = calculo_festa + 150 + 90

botao_orcamento = st.button("Confirmar", type='primary')

if botao_orcamento == True:
    st.balloons()
    st.header('O valor final é: {} R$'.format(calculo_festa))