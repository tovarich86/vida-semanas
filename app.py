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
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    .title {
        color: #000080;
        font-size: 2.5em;
        margin-bottom: 0.5rem;
    }
    .instruction {
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 2rem;
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
    }
    .years > li, .months > li, .weeks > li {
        margin: 4px;
        background-color: #f5f5f5;
        border: 1px solid #000080;
        text-align: center;
        padding: 10px;
        cursor: pointer;
    }
    .years > li {
        width: 24px;
        height: 24px;
    }
    .months > li {
        width: 20px;
        height: 20px;
        border-radius: 50%;
    }
    .weeks > li {
        width: 16px;
        height: 16px;
    }
</style>
"""

st.markdown(css_style, unsafe_allow_html=True)

# Título da página
st.markdown("<div class='title-box'><h1 class='title'>Your Life in Weeks</h1></div>", unsafe_allow_html=True)
st.markdown("<div class='instruction'>Visualize os anos, meses e semanas de sua vida.</div>", unsafe_allow_html=True)

# Selecionar data de nascimento
birth_date = st.date_input("Data de nascimento:", datetime.date(2000, 1, 1))

# Calcular idade e semanas vividas
today = datetime.date.today()
age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
weeks_lived = ((today - birth_date).days) // 7

# Constantes para visualização
max_years = 90
weeks_in_year = 52
months_in_year = 12

# Visualização dos anos
st.markdown("<h2>Ano de Vida</h2>", unsafe_allow_html=True)
years_html = "<ul class='years'>"
for year in range(1, max_years + 1):
    color = "#000080" if year <= age_years else "#d3d3d3"
    years_html += f"<li style='background-color: {color};'>{year}</li>"
years_html += "</ul>"
st.markdown(years_html, unsafe_allow_html=True)

# Visualização dos meses
st.markdown("<h2>Meses</h2>", unsafe_allow_html=True)
months_html = "<ul class='months'>"
for month in range(1, months_in_year * max_years + 1):
    year = (month - 1) // months_in_year + 1
    color = "#000080" if year <= age_years else "#d3d3d3"
    months_html += f"<li style='background-color: {color};'></li>"
months_html += "</ul>"
st.markdown(months_html, unsafe_allow_html=True)

# Visualização das semanas
st.markdown("<h2>Semanas</h2>", unsafe_allow_html=True)
weeks_html = "<ul class='weeks'>"
for week in range(1, weeks_in_year * max_years + 1):
    color = "#000080" if week <= weeks_lived else "#d3d3d3"
    weeks_html += f"<li style='background-color: {color};'></li>"
weeks_html += "</ul>"
st.markdown(weeks_html, unsafe_allow_html=True)

# Mostrar informações adicionais
st.write(f"Idade atual: {age_years} anos.")
st.write(f"Semanas vividas: {weeks_lived} semanas.")
