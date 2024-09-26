import streamlit as st
import datetime

# CSS personalizado para estilizar os elementos da página
css_style = """
<style>
    body {
        font-family: Helvetica, Arial, sans-serif;
    }
    .title-box {
        text-align: center;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .title {
        color: #000080;
        font-size: 2.2em;
        margin-bottom: 0.5rem;
        font-weight: bold;
    }
    .subtitle {
        color: #CB0509;
        font-size: 2.2em;
        margin-bottom: 1rem;
        font-weight: bold;
        display: inline;
    }
    .instruction {
        text-align: center;
        font-size: 1.1em;
        margin-bottom: 1.5rem;
    }
    .chart {
        display: flex;
        justify-content: center;
        margin-top: 2rem;
    }
    .years, .months, .weeks {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        list-style-type: none;
        padding: 0;
        margin: 0 auto;
        max-width: 90%;
    }
    .years > li, .months > li, .weeks > li {
        margin: 1px;
        background-color: #f5f5f5;
        border: 1px solid #000080;
        text-align: center;
        padding: 5px;
        cursor: pointer;
    }
    .years > li {
        width: 12px;
        height: 12px;
    }
    .months > li {
        width: 10px;
        height: 10px;
        border-radius: 50%;
    }
    .weeks > li {
        width: 8px;
        height: 8px;
    }
    .labels {
        font-size: 1em;
        color: #000080;
        font-weight: bold;
        text-align: center;
        margin-top: 1.5rem;
    }
    .reference {
        text-align: center;
        font-size: 0.9em;
        color: #555;
        margin-top: 2rem;
    }
    .reference a {
        color: #CB0509;
        text-decoration: none;
    }
</style>
"""

st.markdown(css_style, unsafe_allow_html=True)

# Título da página
st.markdown("<div class='title-box'><span class='title'>Sua Vida em </span><span class='subtitle'>Semanas</span></div>", unsafe_allow_html=True)
st.markdown("<div class='instruction'>Digite sua data de nascimento:</div>", unsafe_allow_html=True)

# Selecionar data de nascimento
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    dia = st.selectbox("Dia", list(range(1, 32)), index=0)
with col2:
    mes = st.selectbox("Mês", list(range(1, 13)), index=0)
with col3:
    ano = st.selectbox("Ano", list(range(1900, datetime.date.today().year + 1)), index=99)

data_nascimento = datetime.date(ano, mes, dia)

# Calcular idade e semanas vividas
hoje = datetime.date.today()
idade_anos = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
semanas_vividas = ((hoje - data_nascimento).days) // 7

# Constantes para visualização
max_anos = 90
semanas_por_ano = 52

# Visualização das semanas (por padrão)
st.markdown("<div class='labels'>Semana do Ano</div>", unsafe_allow_html=True)
semanas_html = "<ul class='weeks'>"
for semana in range(1, semanas_por_ano * max_anos + 1):
    cor = "#000080" if semana <= semanas_vividas else "#d3d3d3"
    semanas_html += f"<li style='background-color: {cor};'></li>"
semanas_html += "</ul>"
st.markdown(semanas_html, unsafe_allow_html=True)

st.markdown("<div class='labels'>Idade</div>", unsafe_allow_html=True)
st.write(f"Idade: {idade_anos} anos")
st.write(f"Semanas vividas: {semanas_vividas}")

# Referência ao site original
st.markdown(
    "<div class='reference'>Inspirado em <a href='https://www.bryanbraun.com/your-life/weeks.html' target='_blank'>Your Life in Weeks</a></div>",
    unsafe_allow_html=True
)
