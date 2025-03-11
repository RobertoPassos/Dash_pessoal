import streamlit as st
import pandas as pd

st.set_page_config(page_title="Monitoramento de Preços", layout="wide")
st.title("📊 Monitoramento de Preço - Hubii")

# Criando as abas no Streamlit
tab1, tab2 = st.tabs(["📌 Arquitetura de Preço Referência", "📊 Beleza em Casa iFood"])

# Tab 1: Arquitetura de Preço Referência**
with tab1:
    st.subheader("📌 Arquitetura de Preço - Referência da Indústria")
    
    col1, col2 = st.columns([0.25, 0.75])
    
    with col1:
        opcao_busca = st.radio("🔍 Buscar por:", ["EAN", "Marca", "Nome do Produto"], horizontal=True)
        desconto_sugerido = st.number_input("🔻 Desconto Sugerido (%)", min_value=0.0, max_value=100.0, value=10.0, step=0.5)

# tab2: Beleza em Casa iFood**
with tab2:
    st.subheader("📊 Beleza em Casa iFood - Monitoramento de Preços")
    st.write("### 📄 Comparação de Preços")
    st.write("O Price Index calculado na tabela acima é o comparativo do valor praticano no ifood com a tabela de referência fornecida pelo Boticário.")
