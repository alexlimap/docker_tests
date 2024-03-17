# import streamlit as st
# import pandas as pd
# import yfinance as yf
# import matplotlib.pyplot as plt

# def get_stock_data(tickers, start_date, end_date):
#     data = yf.download(tickers, start=start_date, end=end_date)
#     return data['Adj Close']

# def plot_stock_data(stock_data):
#     fig, ax = plt.subplots()
#     for column in stock_data.columns:
#         ax.plot(stock_data.index, stock_data[column], label=column)
#     ax.set_xlabel('Date')
#     ax.set_ylabel('Price')
#     ax.set_title('Stock Prices')
#     ax.legend()
#     st.pyplot(fig)

# def main():
#     st.title('Stock Analysis')
    
#     # Definir parâmetros de entrada
#     tickers = st.text_input('Enter stock tickers (comma-separated):', 'AAPL,GOOGL,MSFT,AMZN,FB').upper().split(',')
#     start_date = st.date_input('Start Date:', pd.to_datetime('2020-01-01'))
#     end_date = st.date_input('End Date:', pd.to_datetime('today'))
    
#     # Obter dados das ações
#     stock_data = get_stock_data(tickers, start_date, end_date)
    
#     if not stock_data.empty:
#         # Exibir dados
#         st.write('Stock Data:')
#         st.write(stock_data)
        
#         # Plotar gráfico
#         st.write('Stock Price Chart:')
#         plot_stock_data(stock_data)
#     else:
#         st.write('No data available for the selected stocks.')

# if __name__ == '__main__':
#     main()

import streamlit as st
import google.generativeai as genai

def generate_response(question):
    genai.configure(api_key= 'AIzaSyAayNX9dYVnBCFXMVFT7vRRA4YEB84w_pA')  # Substitua 'YOUR_API_KEY' pela sua chave de API
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

def main():
    st.title('Chatbot com IA_Generativa')
    
    # Caixa de entrada para o usuário digitar a pergunta
    question = st.text_input('Escreva sua pergunra:')
    
    if st.button('Perguntar'):
        # Gerar resposta
        if question:
            response = generate_response(question)
            # Exibir resposta
            st.write('Response:')
            st.write(response)
        else:
            st.write('Please enter a question.')

if __name__ == '__main__':
    main()
