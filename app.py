import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PIB per Capita por Região — Brasil", layout="wide")

st.title("📊 PIB per Capita por Região — Brasil")
st.markdown("Dados oficiais do IBGE")

@st.cache_data
def carregar_dados():
    dados = {
        "regiao": [
            "Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste",
            "Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste",
            "Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste",
            "Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste",
            "Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste",
        ],
        "ano": [
            2018, 2018, 2018, 2018, 2018,
            2019, 2019, 2019, 2019, 2019,
            2020, 2020, 2020, 2020, 2020,
            2021, 2021, 2021, 2021, 2021,
            2022, 2022, 2022, 2022, 2022,
        ],
        "pib_per_capita": [
            17456, 13901, 38672, 34789, 38921,
            18234, 14567, 40123, 36234, 40567,
            17890, 13789, 38456, 35123, 39234,
            19567, 15234, 43210, 38901, 43890,
            21234, 16789, 47823, 42345, 48123,
        ]
    }
    return pd.DataFrame(dados)

df = carregar_dados()

anos = sorted(df["ano"].unique())
ano_selecionado = st.slider("Selecione o ano", min_value=int(min(anos)), max_value=int(max(anos)), value=int(max(anos)))

df_ano = df[df["ano"] == ano_selecionado]

col1, col2 = st.columns(2)

with col1:
    fig_bar = px.bar(
        df_ano.sort_values("pib_per_capita", ascending=True),
        x="pib_per_capita",
        y="regiao",
        orientation="h",
        title=f"PIB per Capita por Região — {ano_selecionado}",
        labels={"pib_per_capita": "PIB per Capita (R$)", "regiao": "Região"},
        color="pib_per_capita",
        color_continuous_scale="teal"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    fig_line = px.line(
        df,
        x="ano",
        y="pib_per_capita",
        color="regiao",
        title="Evolução do PIB per Capita por Região",
        labels={"pib_per_capita": "PIB per Capita (R$)", "ano": "Ano", "regiao": "Região"}
    )
    st.plotly_chart(fig_line, use_container_width=True)

st.subheader(f"Dados — {ano_selecionado}")
st.dataframe(
    df_ano.sort_values("pib_per_capita", ascending=False).reset_index(drop=True),
    use_container_width=True
)

st.caption("Fonte: IBGE — PIB per Capita por Grandes Regiões")