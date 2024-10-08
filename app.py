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
        font-size: 2.5em;
        margin-bottom: 0.5rem;
        font-weight: bold;
    }
    .subtitle {
        color: #CB0509;
        font-size: 2.5em;
        margin-bottom: 1rem;
        font-weight: bold;
        display: inline;
    }
    .instruction {
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 1.5rem;
    }
    .chart-container {
        display: grid;
        grid-template-columns: auto 1fr;
        gap: 10px;
        margin-top: 20px;
        position: relative;
        width: fit-content;
        margin-left: auto;
        margin-right: auto;
    }
    .week-grid {
        display: grid;
        grid-template-columns: repeat(52, 14px);
        grid-auto-rows: 14px;
        gap: 3px;
    }
    .week-cell {
        width: 14px;
        height: 14px;
        border: 1px solid #000080;
        background-color: #fff;
    }
    .week-cell.lived {
        background-color: #000080;
    }
    .age-labels {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        height: calc(52 * 16px); /* Ajusta para altura total da grid */
        margin-top: 12px;
        font-size: 0.9em;
        color: #000080;
        font-weight: bold;
    }
    .week-labels {
        display: flex;
        justify-content: space-between;
        margin-top: 15px;
        width: calc(52 * 16px); /* Ajusta para largura total da grid */
        font-size: 0.9em;
        color: #000080;
        font-weight: bold;
    }
    .week-title {
        text-align: center;
        margin-top: 15px;
        font-size: 1.2em;
        color: #000080;
        font-weight: bold;
    }
    .year-title {
        text-align: center;
        margin-bottom: 10px;
        font-size: 1.2em;
        color: #000080;
        font-weight: bold;
        writing-mode: vertical-rl;
        transform: rotate(180deg);
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

# Título centralizado para "Semanas do Ano"
st.markdown("<div class='week-title'>Semanas do Ano</div>", unsafe_allow_html=True)

# Labels de semanas na parte superior
week_labels_html = "<div class='week-labels'>"
for i in range(1, semanas_por_ano + 1, 5):
    week_labels_html += f"<div>{i}</div>"
week_labels_html += "</div>"

# Adiciona o rótulo "Anos" ao lado esquerdo da grade
st.markdown("<div class='year-title'>Anos</div>", unsafe_allow_html=True)

# Labels de idade na lateral (escala de 5 em 5 anos)
age_labels_html = "<div class='age-labels'>"
for i in range(0, max_anos + 1, 5):
    age_labels_html += f"<div>{i}</div>"
age_labels_html += "</div>"

# Renderiza a grade de semanas
week_cells_html = "<div class='week-grid'>"
for semana in range(1, semanas_por_ano * max_anos + 1):
    cor = "lived" if semana <= semanas_vividas else ""
    week_cells_html += f"<div class='week-cell {cor}'></div>"
week_cells_html += "</div>"

# Junta todas as partes para a visualização final
st.markdown(week_labels_html, unsafe_allow_html=True)
st.markdown(f"""
<div class='chart-container'>
    {age_labels_html}
    {week_cells_html}
</div>
""", unsafe_allow_html=True)

# Referência ao site original
st.markdown(
    "<div class='reference'>Inspirado em <a href='https://www.bryanbraun.com/your-life/weeks.html' target='_blank'>Your Life in Weeks</a></div>",
    unsafe_allow_html=True
)
