dados = pd.read_csv('gasolina.csv')
dados.head()

plt.figure(figsize = (16, 9))
dados.plot('dia', 'venda', grid= True, title= 'preço da gasolinha')

plt.show()