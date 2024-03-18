import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title('Análise de CSV com Streamlit')
    
    # Upload do arquivo CSV
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
    if uploaded_file is not None:
        # Ler o arquivo CSV
        df = pd.read_csv(uploaded_file)
        
        # Mostrar a tabela de dados
        st.write("Tabela de Dados:")
        st.write(df)

        # Gerar gráficos
        if st.button('Gerar Gráficos'):
            st.write("Gráficos:")
            # Gráfico 1
            st.write("Gráfico de Linha:")
            plt.figure(figsize=(10,4))
            plt.plot(df.iloc[:,0], df.iloc[:,1])
            st.pyplot(plt)

            # Gráfico 2
            st.write("Gráfico de Barras:")
            plt.figure(figsize=(10,4))
            plt.bar(df.iloc[:,0], df.iloc[:,1])
            st.pyplot(plt)

if __name__ == "__main__":
    main()
