import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Função para gerar dados de exemplo
def generate_data():
    data = {
        'Country': ['USA', 'Canada', 'Germany', 'UK', 'France'],
        'Population': [327, 38, 83, 67, 65],
        'GDP': [21.43, 1.84, 4.42, 2.62, 2.78]
    }
    return pd.DataFrame(data)

# Função para filtrar dados com base no país selecionado
def filter_data(df, country):
    return df[df['Country'] == country]

# Função para plotar gráfico
def plot_data(df):
    fig, ax = plt.subplots()
    ax.bar(df['Country'], df['GDP'])
    ax.set_xlabel('Country')
    ax.set_ylabel('GDP (Trillions USD)')
    ax.set_title('GDP by Country')
    st.pyplot(fig)

def main():
    st.title('GDP Analysis')
    
    # Gerar dados
    data = generate_data()
    
    # Filtro por país
    selected_country = st.selectbox('Select a country:', data['Country'])
    filtered_data = filter_data(data, selected_country)
    
    # Exibir dados filtrados
    st.write('Filtered Data:')
    st.write(filtered_data)
    
    # Plotar gráfico
    st.write('GDP Chart:')
    plot_data(filtered_data)

if __name__ == '__main__':
    main()
