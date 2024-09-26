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
        margin: 2px;
        background-color: #f5f5f5;
        border: 1px solid #000080;
        text-align: center;
        padding: 5px;
        cursor: pointer;
    }
    .years > li {
        width: 16px;
        height: 16px;
    }
    .months > li {
        width: 14px;
        height: 14px;
        border-radius: 50%;
    }
    .weeks > li {
        width: 12px;
        height: 12px;
    }
    .labels {
        font-size: 1.2em;
        color: #000080;
        font-weight: bold;
    }
</style>
"""

st.markdown(css_style, unsafe_allow_html=True)

# Título da página
st.markdown("<div class='title-box'><span class='title'>Your Life in </span><span class='subtitle'>Weeks</span></div>", unsafe_allow_html=True)
st.markdown("<div class='instruction'>Enter your Date of Birth</div>", unsafe_allow_html=True)

# Selecionar data de nascimento
col1, col2, col3 = st.columns(3)

with col1:
    day = st.selectbox("Day", list(range(1, 32)), index=0)
with col2:
    month = st.selectbox("Month", list(range(1, 13)), index=0)
with col3:
    year = st.selectbox("Year", list(range(1900, datetime.date.today().year + 1)), index=99)

birth_date = datetime.date(year, month, day)

# Calcular idade e semanas vividas
today = datetime.date.today()
age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
weeks_lived = ((today - birth_date).days) // 7

# Constantes para visualização
max_years = 90
weeks_in_year = 52

# Visualização das semanas (por padrão)
st.markdown("<div class='labels'>Week of the Year</div>", unsafe_allow_html=True)
weeks_html = "<ul class='weeks'>"
for week in range(1, weeks_in_year * max_years + 1):
    color = "#000080" if week <= weeks_lived else "#d3d3d3"
    weeks_html += f"<li style='background-color: {color};'></li>"
weeks_html += "</ul>"
st.markdown(weeks_html, unsafe_allow_html=True)

st.markdown("<div class='labels'>Age</div>", unsafe_allow_html=True)
st.write(f"Age: {age_years} years old")
st.write(f"Weeks lived: {weeks_lived}")
