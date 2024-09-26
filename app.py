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
    .chart-container {
        display: flex;
        justify-content: center;
        margin-top: 2rem;
        position: relative;
    }
    .years, .weeks {
        display: flex;
        flex-wrap: wrap;
        list-style-type: none;
        padding: 0;
        margin: 0 auto;
    }
    .weeks > li {
        margin: 1px;
        background-color: #f5f5f5;
        border: 1px solid #000080;
        width: 8px;
        height: 8px;
        cursor: pointer;
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
    .age-label, .week-label {
        position: absolute;
        font-weight: bold;
        color: #000080;
    }
    .age-label {
        left: -50px;
        top: 50%;
        transform: rotate(-90deg);
    }
    .week-label {
        top: -30px;
    }
    .arrow {
        font-size: 1.5em;
        font-weight: bold;
    }
    .age-arrow {
        left: -70px;
        top: 45%;
        transform: rotate(-90deg);
    }
    .week-arrow {
        top: -50px;
    }
</style>
"""

st.markdown(css_style, unsafe_allow_html=True)

# Título da página
st.markdown("<div class='title-box'><span class='title'>Sua Vida em </span><span class='subtitle'>Semanas</span></div>", unsafe_allow_html=True)
st.markdown("<div class='instruction'>Digite sua data de nascimento:</div>", unsafe_allow_html=True)

# Selecionar data de nascimento no formato dd/mm/aaaa
data_nascimento = st.date_input("Data de nascimento:", value=datetime.date(2000, 1, 1), format="DD/MM/YYYY")

# Calcular idade e semanas vividas
hoje = datetime.date.today()
idade_anos = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
semanas_vividas = ((hoje - data_nascimento).days) // 7

# Constantes para visualização
max_anos = 90
semanas_por_ano = 52

# Visualização das semanas
st.markdown("<div class='labels'>Semana do Ano</div>", unsafe_allow_html=True)

# Container para a visualização e as legendas
st.markdown("""
<div class='chart-container'>
    <!-- Label para a idade -->
    <div class='age-label'>
        Idade
    </div>
    <!-- Label para as semanas do ano -->
    <div class='week-label'>
        <span>Semana do Ano</span>
    </div>
    <!-- Seta para idade -->
    <div class='age-arrow arrow'>
        &#8595;
    </div>
    <!-- Seta para semana do ano -->
    <div class='week-arrow arrow'>
        &#8594;
    </div>
</div>
""", unsafe_allow_html=True)

# Renderizar a grade de semanas
semanas_html = "<ul class='weeks'>"
for semana in range(1, semanas_por_ano * max_anos + 1):
    cor = "#000080" if semana <= semanas_vividas else "#d3d3d3"
    semanas_html += f"<li style='background-color: {cor};'></li>"
semanas_html += "</ul>"
st.markdown(semanas_html, unsafe_allow_html=True)

# Adicionar números representando a idade (lado esquerdo) e as semanas do ano (acima)
idade_texto = "<div style='position: relative; display: flex; justify-content: center; margin-top: 10px;'>"
idade_texto += "<div style='position: absolute; left: -45px;'>"
for i in range(0, max_anos + 1, 5):
    idade_texto += f"<div style='height: 15px; font-weight: bold; color: #000080;'>{i}</div>"
idade_texto += "</div>"

semanas_texto = "<div style='position: absolute; top: -25px; width: 100%; display: flex; justify-content: space-around;'>"
for i in range(1, semanas_por_ano + 1, 5):
    semanas_texto += f"<div style='width: 20px; text-align: center; font-weight: bold; color: #000080;'>{i}</div>"
semanas_texto += "</div>"
idade_texto += semanas_texto
idade_texto += "</div>"

st.markdown(idade_texto, unsafe_allow_html=True)

st.markdown("<div class='labels'>Idade</div>", unsafe_allow_html=True)
st.write(f"Idade: {idade_anos} anos")
st.write(f"Semanas vividas: {semanas_vividas}")

# Referência ao site original
st.markdown(
    "<div class='reference'>Inspirado em <a href='https://www.bryanbraun.com/your-life/weeks.html' target='_blank'>Your Life in Weeks</a></div>",
    unsafe_allow_html=True
)
