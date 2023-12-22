# %%
import pandas as pd

# %%
df = pd.read_csv('https://raw.githubusercontent.com/camimq/fiap/master/alura/data%20viz/data-visualization_criando_graficos_com_biblioteca_python/base/imigrantes_canada.csv')
df

# %%
# método info
# dtype OBJECT = strings
df.info()

# %%
# tornar coluna país em index
# quando utilizamos o inplace = True, ele já transforma o dataset, não sendo necessário reatribuir a variável df para que a coluna País seja o index
df.set_index('País', inplace=True)

# %%
# cria variável que atribui o intervalo de anos, através de uma lista
# com a função map, iremos definir que os anos serão armazenados como strings (ou seja objetos), e não como números
anos = list(map(str, range(1980, 2014)))
anos

# %%
# cria uma variável que trás o intervalo dos anos, apenas para o Brasil, utilizando o método .lo() que vai fazer a busca por rótulo
brasil = df.loc['Brasil', anos]
brasil

# %%
# transformando variável Brasil em um DataFrame, através da criação de um dicionário
brasil_dict = {'ano' : brasil.index.tolist(), 'imigrantes' : brasil.values.tolist()}
dados_brasil = pd.DataFrame(brasil_dict)
dados_brasil

# %%
import matplotlib.pyplot as plt

# %%
# funão plot cria, automaticamente, um gráfico de linha
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])

# %% [markdown]
# - Variável do eixo Y (numero de imigrantes), é dependente porque ela muda de acordo com o ano.

# %%
# funão plot cria, automaticamente, um gráfico de linha
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
# melhorando a visualização do gráfio, alterando o intervalo de anos no eixo X, para que mostre de 5 em 5 anos
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])

# %%
# funão plot cria, automaticamente, um gráfico de linha
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
# melhorando a visualização do gráfio, alterando o intervalo de anos no eixo X, para que mostre de 5 em 5 anos
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
# ajustando o eixo y
plt.yticks([500, 1000, 1500, 2000, 2500, 3000])

# %%
# funão plot cria, automaticamente, um gráfico de linha
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
# melhorando a visualização do gráfio, alterando o intervalo de anos no eixo X, para que mostre de 5 em 5 anos
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
# função que deixa de mostrar as informações de armazenamento do matplotlib (o texto que aparece antes do gráfico - cheque no gráfico acima)
plt.show()

# %%
# modificar o tamnho do gráfico (primeiro valor altura, segundo valor largura), em polegadas
plt.figure(figsize = (8,4))
# funão plot cria, automaticamente, um gráfico de linha
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
# melhorando a visualização do gráfio, alterando o intervalo de anos no eixo X, para que mostre de 5 em 5 anos
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
# função que deixa de mostrar as informações de armazenamento do matplotlib (o texto que aparece antes do gráfico - cheque no gráfico acima)
plt.show()

# %%
# modificar o tamnho do gráfico (primeiro valor altura, segundo valor largura), em polegadas
plt.figure(figsize = (8,4))
# funão plot cria, automaticamente, um gráfico de linha
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
#adiciona o título do gráfico
plt.title('Imigração do Brasil para o Canadá')
# melhorando a visualização do gráfio, alterando o intervalo de anos no eixo X, para que mostre de 5 em 5 anos
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
# função que deixa de mostrar as informações de armazenamento do matplotlib (o texto que aparece antes do gráfico - cheque no gráfico acima)
plt.show()

# %%
# modificar o tamnho do gráfico (primeiro valor altura, segundo valor largura), em polegadas
plt.figure(figsize = (8,4))
# funão plot cria, automaticamente, um gráfico de linha
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
#adiciona o título do gráfico
plt.title('Imigração do Brasil para o Canadá')
# incluindo o rótulo do eixo x
plt.xlabel('Ano')
# incluindo rótulo para o eixo y
plt.ylabel('Imigrantes')
# melhorando a visualização do gráfio, alterando o intervalo de anos no eixo X, para que mostre de 5 em 5 anos
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
# função que deixa de mostrar as informações de armazenamento do matplotlib (o texto que aparece antes do gráfico - cheque no gráfico acima)
plt.show()

# %%
df

# %%
# cria variável argentina com quantidade de imigrantes por ano
argentina = df.loc['Argentina', anos]
argentina

# %%
# transforma variável Argentina Brasil em um DataFrame, através da criação de um dicionário
argentina_dict = {'ano' : argentina.index.tolist(), 'imigrantes' : argentina.values.tolist()}
dados_argentina = pd.DataFrame(argentina_dict)
dados_argentina

# %%
# modificar o tamnho do gráfico (primeiro valor altura, segundo valor largura), em polegadas
plt.figure(figsize = (8,4))
# funão plot cria, automaticamente, um gráfico de linha
# plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'], dados_argentina['ano'], dados_argentina['imigrantes'])
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'], label = 'Brasil')
plt.plot(dados_argentina['ano'], dados_argentina['imigrantes'], ls = '--', label = 'Argentina' )
#adiciona o título do gráfico
plt.title('Brasil x Argentina: Imigração para o Canadá')
# adicionando legenda
plt.legend()
# incluindo o rótulo do eixo x
plt.xlabel('Ano')
# incluindo rótulo para o eixo y
plt.ylabel('Imigrantes')
# melhorando a visualização do gráfio, alterando o intervalo de anos no eixo X, para que mostre de 5 em 5 anos
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
# função que deixa de mostrar as informações de armazenamento do matplotlib (o texto que aparece antes do gráfico - cheque no gráfico acima)
plt.show()

# %%
df_comparacao = df.loc[['Brasil', 'Argentina'], anos]

# %%
df_comparacao = df_comparacao.T
df_comparacao.head()

# %%
plt.plot(df_comparacao['Brasil'], label = 'Brasil')
plt.plot(df_comparacao['Argentina'], label = 'Argentina')
plt.title('Imigração do Brasil e Argentina para o Canadá')
plt.xlabel('Ano')
plt.ylabel('Número de imigrantes')
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
plt.legend()
plt.show()

# %%
# criando uma figura - para isso, usamos a função subplots()
# fig = cria uma espaço
# ax (abreviação de axes) = representa o eixo
fig, ax = plt.subplots(figsize = (8,4))
# dados_brasil['ano'] = eixo X / dados_brasil('imigrantes') = eixo y
ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
# adiciona título em figura
# a barra invertida, inclui uma segunda linha no título
ax.set_title('Imigração do Brasil para o Canadá\n1980 a 2013')
# adiciona rótulos em uma figura
ax.set_xlabel('Ano')
ax.set_ylabel('Número de Imigrantes')
# altera, na figura, a frequência dos anos para que seja exibido de 5 em 5 anos
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
plt.show()

# %%
# axs especifica que, dentro da figura, existirão mais de um gráfico
# a função subplots(), vai dizer quantos gráficos serão colocados na mesma figura
# essa função recebe dois argumentos:
# 1. Quantas linhas existirão no subplot + 2. Quantos subplots (gráficos) queremos inserir na linha
# como iremos comparar somente dois gráficos (um ao lado do outro, precisamos de uma linha)
fig, axs = plt.subplots(1, 2, figsize = (15,5))

# criando o primeiro subplot - gráfico de linha
# axs[0] - indica que é o primeiro gráfico (considere contagem de indexação)
axs[0].plot(dados_brasil['ano'], dados_brasil['imigrantes'])
axs[0].set_title('Imigração do Brasil para o Canadá\n1980 a 2013')
axs[0].set_xlabel('Ano')
axs[0].set_ylabel('Número de Imigrantes')
# para alterar frequência do gráfico para 5 em 5 anos
axs[0].xaxis.set_major_locator(plt.MultipleLocator(5))
# adiciona grid para facilitar leitura do gráfico
axs[0].grid()

#criando o segundo subplot - boxplot (mostra alguns dados estatísticos)
# quando estamos criando um boxplot, só é necessário passar nos argumentos, os dados numéricos
axs[1].boxplot(dados_brasil['imigrantes'])
axs[1].set_title('Boxplot da Imigração do Brasil para o Canadá\n1980 a 2013')
axs[1].set_xlabel('Brasil')
axs[1].set_ylabel('Número de Imigrantes')
# adiciona grid para facilitar leitura do gráfico
axs[1].grid()

plt.show()

# %%
# confirmando os números do boxplot
dados_brasil.describe()

# %%
fig, axs = plt.subplots(2, 2, figsize = (10,6))

# muda o espaçamento entre os gráficos
# hspace = espaçamento vertical
# wspace = espaçamento horizontal
fig.subplots_adjust(hspace = 0.5, wspace = 0.3)

axs[0,0].plot(df.loc['Brasil', anos])
axs[0,0].set_title('Brasil')

axs[0,1].plot(df.loc['Colômbia', anos])
axs[0,1].set_title('Colombia')

axs[1,0].plot(df.loc['Argentina', anos])
axs[1,0].set_title('Argentina')

axs[1,1].plot(df.loc['Peru', anos])
axs[1,1].set_title('Peru')

# for para ajustar a frequencia para 5 anos, em todos os gráficos
for ax in axs.flat:
  ax.xaxis.set_major_locator(plt.MultipleLocator(5))

for ax in axs.flat:
  ax.set_xlabel('Ano')
  ax.set_ylabel('Número de Imigrantes')

plt.show()

# %%
fig, ax = plt.subplots(figsize = (8,4))
# customização
# lw = espessura da linha do gráfico
# marker = marca os pontos dos dados na linha do tempo
#ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'], lw=3, marker='o')
ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'], lw=3)
# customização
# fontsize = tamanho da fonte para o título
# loc = alinhamento do título (esquerda, centro ou direita)
ax.set_title('Imigração do Brasil para o Canadá\n1980 a 2013', fontsize = 18, loc='left')
# customização
# fontsize = tamanho da fonte da label
ax.set_xlabel('Ano', fontsize=14)
ax.set_ylabel('Número de imigrantes', fontsize=14)
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
# customiazação do grid
plt.grid(linestyle='--')
plt.show()

# %%
print(plt.style.available)

# %% [markdown]
# ## Alterando as Cores #1

# %%
fig, ax = plt.subplots(figsize = (8,4))
# customização - cores
# color - cor da linha
ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'], lw=3, color = 'g')
ax.set_title('Imigração do Brasil para o Canadá\n1980 a 2013', fontsize = 18, loc='left')
ax.set_xlabel('Ano', fontsize=14)
ax.set_ylabel('Número de imigrantes', fontsize=14)
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# para salvar o gráfico
fig.savefig('imigracao_brasil_canada.png', transparent=False, dpi=300, bbox_inches='tight')
plt.show()

# %%
df.head()

# %%
# query para puxar somente os países que são parte da América do Sul
america_sul = df.query('Região == "América do Sul"')

# %%
america_sul

# %%
cores = ['royalblue', 'orange', 'forestgreen', 'orchid', 'purple', 'brown', 'slateblue', 'gray', 'olive', 'navy', 'teal', 'tomato']
# criando um gráfio de barra
fig, ax = plt.subplots(figsize = (12,5))
ax.bar(america_sul.index, america_sul['Total'], color = cores)
ax.set_title('Imigração da América do Sul para o Canadá\n1980 a 2013', loc = 'left', fontsize = 18)
ax.set_xlabel('')
ax.set_ylabel('Número de imigrantes', fontsize = 14)
ax.xaxis.set_tick_params(labelsize = 12)
ax.yaxis.set_tick_params(labelsize = 12)

plt.show()

# %%
cores = ['royalblue', 'orange', 'forestgreen', 'orchid', 'purple', 'brown', 'slateblue', 'gray', 'olive', 'navy', 'teal', 'tomato']
fig, ax = plt.subplots(figsize = (12,5))
# criando um grafico de barra invertida
ax.barh(america_sul.index, america_sul['Total'], color = cores)
ax.set_title('Imigração da América do Sul para o Canadá\n1980 a 2013', loc = 'left', fontsize = 18)
ax.set_xlabel('Número de imigrantes', fontsize = 14)
ax.set_ylabel('')
ax.xaxis.set_tick_params(labelsize = 12)
ax.yaxis.set_tick_params(labelsize = 12)

plt.show()

# %%
# criando um novo DataFrame para ordenar as informações nos gráficos, tornando-as mais simples de ler.
america_sul_sorted = america_sul.sort_values("Total", ascending=True)

# %%
cores = ['royalblue', 'orange', 'forestgreen', 'orchid', 'purple', 'brown', 'slateblue', 'gray', 'olive', 'navy', 'teal', 'tomato']
fig, ax = plt.subplots(figsize = (12,5))
ax.barh(america_sul_sorted.index, america_sul_sorted['Total'], color = cores)
ax.set_title('Imigração da América do Sul para o Canadá\n1980 a 2013', loc = 'left', fontsize = 18)
ax.set_xlabel('Número de imigrantes', fontsize = 14)
ax.set_ylabel('')
ax.xaxis.set_tick_params(labelsize = 12)
ax.yaxis.set_tick_params(labelsize = 12)

plt.show()

# %%
# cria um for para iterar em todos os países. se for o brasil, cor vai ser verde, caso contrário, cinza.
cores_for = []
for pais in america_sul_sorted.index:
  if pais == 'Brasil':
    cores_for.append('green')
  else:
    cores_for.append('silver')

fig, ax = plt.subplots(figsize = (12,5))
ax.barh(america_sul_sorted.index, america_sul_sorted['Total'], color=cores_for)
ax.set_title('América do Sul: Brasil foi o quarto país com mais imigrantes\n para o Canadá, no período de 1980 a 2013', loc = 'left', fontsize = 18)
ax.set_xlabel('Número de imigrantes', fontsize = 14)
ax.set_ylabel('')
ax.xaxis.set_tick_params(labelsize = 12)
ax.yaxis.set_tick_params(labelsize = 12)

# cria iteração para criar notações nos gráficos
for i, v in enumerate(america_sul_sorted['Total']):
  # indica onde o texto deve ser adicionado. o v, indica o local da barra
  # i é a posição y do texto
  ax.text(v + 20, i, str(v), color='black', fontsize=10, ha='left', va='center')

# tirando a as linhas de delimitação do frame (O 'quadrado' em que o gráfico está contido)
ax.set_frame_on(False)

# tira o eixo X para deixar o gráfico limpo
ax.get_xaxis().set_visible(False)

# tira os ticks perto dos gráficos
ax.tick_params(axis='both', which='both', length=0)

# salvando o gráfico
fig.savefig('imigracao_america_sul.png', transparent=False, dpi=300, bbox_inches='tight')
plt.show()

# %%
# salvando gráficos
print(fig.canvas.get_supported_filetypes())


# %%
import seaborn as sns

# %%
# a biblioteca Seaborn, tem alguns temas que podem ser utilizadas na estilização dos gráficos
# para este exemplo, utilizaremos a biblioteca padrão
sns.set_theme()

# %%
# TOP 10 dos países que imigram para o Canadá

# ordenar o DF pela quantidade de pessoas que imigraram, utilizando a coluna Totla, que traz o número total de imigrantes
top_10 = df.sort_values('Total', ascending=False).head(10)
top_10

# %%
# criando um gráfico de barras para mostrar a informação do DF acima
sns.barplot(data=top_10, x=top_10.index, y='Total')

# %%
sns.barplot(data=top_10, x='Total', y=top_10.index, orient='h')

# %% [markdown]
# ## Personalizando visualizações com Seaborn

# %%
ax = sns.barplot(data=top_10, y=top_10.index, x='Total', orient='h')

ax.set(title='Países com maior imigração para o Canadá\n1980 a 2013',
       xlabel='Número de imigrantes',
       ylabel='')

plt.show()

# %%
fig, ax = plt.subplots(figsize=(8,4))
ax = sns.barplot(data=top_10, y=top_10.index, x='Total', orient='h')

ax.set_title('Países com maior imigração para o Canada\n1980 a 2013', loc='left', fontsize=16)
ax.set_xlabel('Número de imigrantes', fontsize=14)
ax.set_ylabel('')

plt.show()

# %%
# Função que ajuda a entender melhor qual a paleta de cores mais adequada

def gerar_grafico_paleta(palette):
 fig, ax = plt.subplots(figsize=(8,4))
 ax = sns.barplot(data=top_10, y=top_10.index, x='Total', orient='h', palette=palette)
 ax.set_title('Países com maior imigração para o Canada\n1980 a 2013', loc='left', fontsize=14)
 ax.set_xlabel('Número de imigrantes', fontsize=14)
 ax.set_ylabel('')

 plt.show()

# %%
gerar_grafico_paleta('Blues')

# %%
gerar_grafico_paleta('Blues_r')

# %%
gerar_grafico_paleta('rocket')

# %%
gerar_grafico_paleta('coolwarm')

# %%
gerar_grafico_paleta('tab10')

# %%
sns.set_theme(style='dark')
gerar_grafico_paleta('tab10')

# %%
sns.set_theme(style='whitegrid')
gerar_grafico_paleta('tab10')

# %%
sns.set_theme(style='white')
gerar_grafico_paleta('tab10')

# %%
sns.set_theme(style='ticks')
gerar_grafico_paleta('tab10')

# %%
# retirando o gráfico de "dentro da caixinha"

fig, ax = plt.subplots(figsize=(8,4))
ax=sns.barplot(data=top_10, y=top_10.index, x='Total', orient='h', palette='tab10')

ax.set_title('Países com maior imigração para o Canadá\n1980 a 2013', loc='left', fontsize=18)
ax.set_xlabel('Número de imigrantes', fontsize=14)
ax.set_ylabel('')

# função que tira o "contorno" do gráfico
sns.despine()

plt.show()

# %% [markdown]
# ## Desafio: criando um gráfico de linhas com a biblioteca Seaborn

# %% [markdown]
# Voltando aos dados utilizados no projeto que nós estamos desenvolvendo neste curso, agora chegou o momento de utilizar todos os conhecimentos adquiridos sobre as bibliotecas Matplotlib e Seaborn.
# 
# Nesta etapa, seu desafio é criar uma figura contendo as tendências de imigração dos 4 maiores países da América latina: Brasil, Argentina, Peru e Colômbia. Através dessa criação você pode explorar diversas possibilidades e reconhecer de forma atrativa o seu processo de desenvolvimento.E não nos esqueçamos das orientações! Essa figura precisa ter uma linha para cada país, título, rótulos nos eixos, cores apropriadas, um tema da biblioteca Seaborn e legenda. Por isso, pense nas questões de acessibilidade, como tamanho das fontes e espessura das linhas. É importante escolher cores adequadas que não causem cansaço visual ou dificultem a leitura das informações. Além disso, o tamanho das fontes deve ser legível o suficiente para que as pessoas possam interpretar os dados com facilidade.
# 
# > Dica: para escolher a paleta de cores, você também pode consultar a documentação da biblioteca Matploltib. A Seaborn utiliza as colormaps do Matplotlib por padrão, além de oferecer suas próprias paletas de cores. Para aplicar uma paleta de cores a todas as linhas da figura você pode usar a função `sns.set_palette()` e passar a ela o nome da paleta escolhida.
# 
# Estamos empolgados para ver o resultado do seu trabalho e as histórias que você irá contar através deste gráfico. Mãos à obra e divirta-se!

# %% [markdown]
# ### Resolução

# %%
# define um tema para o gráfico
sns.set_theme()
# define paleta de cores
sns.set_palette('Dark2')

# cria uma figura com uma área de plotagem (eixo) com tamanho específico
fig, ax = plt.subplots(figsize=(10, 5))
# lineplot() - utilizada para plotar uma linha para cada país, com label identificando o país e espessura da linha em 3px
ax = sns.lineplot(df.loc['Brasil', anos], label='Brasil', lw=3)
ax = sns.lineplot(df.loc['Argentina', anos], label='Argentina', lw=3)
ax = sns.lineplot(df.loc['Peru', anos], label='Peru', lw=3)
ax = sns.lineplot(df.loc['Colômbia', anos], label='Colômbia', lw=3)

ax.set_title('Imigração dos maiores países da América do Sul\npara o Canadá de 1980 a 2013', loc='left', fontsize=20)
ax.set_xlabel('Ano', fontsize=14)
ax.set_ylabel('Número de imigrantes', fontsize=14)

ax.xaxis.set_major_locator(plt.MultipleLocator(5))

# adiciona uma legenda ao gráfico
# bbox_to_anchor é a propriedade que indica onde esta legenda deve ficar
# 1.18 para x, significa que a legenda deve ser colocada 18% para a direita da extremidade direita do gráfico
# 1.02 para Y, infica que a legenda deve ser colocada 2% acima do topo do gráfico
ax.legend(title='Países', loc='upper right', bbox_to_anchor=(1.18, 1.02))

plt.show()

# %% [markdown]
# # 5. Gráficos interativos com Plotly

# %% [markdown]
# ## Criando o primeiro gráfico interativo

# %%
import plotly.express as px

# %%
fig = px.line(dados_brasil, x='ano', y='imigrantes')
fig.update_layout(width=1000, height=500,
                  xaxis={'tickangle' : -45})
fig.show()

# %% [markdown]
# ## Personalizando interativos com Plotly

# %%
fig = px.line(dados_brasil, x='ano', y='imigrantes',
              title='Imigração do Brasil para o Canadá no período de 1980 a 2013')
fig.update_layout(width=1000, height=500,
                  xaxis={'tickangle' : -45},
                  font_family='Arial',
                  font_size=14,
                  font_color='grey',
                  title_font_color='black',
                  title_font_size=22,
                  xaxis_title='Ano',
                  yaxis_title='Número de imigrantes')
fig.show()

# %% [markdown]
# ## Alterando as cores com Plotly

# %%
fig = px.line(dados_brasil, x='ano', y='imigrantes',
              title='Imigração do Brasil para o Canadá no período de 1980 a 2013')
# altera cor e espessura da linha do gráfico
fig.update_traces(line_color='green', line_width=4)
fig.update_layout(width=1000, height=500,
                  xaxis={'tickangle' : -45},
                  font_family='Arial',
                  font_size=14,
                  font_color='grey',
                  title_font_color='black',
                  title_font_size=22,
                  xaxis_title='Ano',
                  yaxis_title='Número de imigrantes')
fig.show()

# %%
# criando um gráfico de linha com vários países
# para isso, será utilizado o dataframe df america_sul
america_sul.head()

# %% [markdown]
# Para criar o gráfico que mencionamos, precisamos somente das colunas com o nome dos países e os números de cada ano. Para isso, faremos o drop da coluna continente, região e total.
# 
# Além disso, precisaremos transpor a tabela para que, em cada coluna, tenhamos um país e, em cada linha, um  país. Do jeito que o DataFrame está hoje, está ao contrário.

# %%
# para especificar que estamos deletando uma coluna, a propriedade axis, vai ser igual a 1. Se fosse uma coluna, essa propriedade, seria igual a 0.
df_america_sul_clean=america_sul.drop(['Continente', 'Região', 'Total'], axis=1)

# cria dataframe df_america_sul_clean transposto
america_sul_final = df_america_sul_clean.T

# %%
america_sul_final.head(5)

# %%
# criando o gráfico para todos os países
fig = px.line(america_sul_final, x=america_sul_final.index, y=america_sul_final.columns, color='País',
              title = 'Imigração dos países da América do Sul para o Canadá de 1980 a 2013')
fig.update_layout(
  xaxis={'tickangle' : -45},
  xaxis_title='Ano',
  yaxis_title='Número de imigrantes'
)

fig.show()

# %%
# criando o gráfico para todos os países
fig = px.line(america_sul_final, x=america_sul_final.index, y=america_sul_final.columns, color='País',
              title = 'Imigração dos países da América do Sul para o Canadá de 1980 a 2013', markers=True)
fig.update_layout(
  xaxis={'tickangle' : -45},
  xaxis_title='Ano',
  yaxis_title='Número de imigrantes'
)

fig.show()

# %% [markdown]
# ## Salvando gráficos em HTML

# %%
fig.write_html('imigracao_america_sul.html')

# %% [markdown]
# ## Desafio: criando uma animação para comparar diferentes dados

# %% [markdown]
# Na atividade anterior foi possível compreender como criar uma animação com a biblioteca Plotly. Agora vem mais um desafio!
# 
# Lembra que nós criamos uma figura estática contendo os dados de imigração do Brasil e Argentina? Sua tarefa é criar um gráfico animado com o Plotly que mostre esses dados. O gráfico deve ter as seguintes características:
# 
# - Duas linhas: uma para o Brasil e outra para a Argentina.
# - Um botão "Play" para iniciar a animação, mostrando o aumento ou diminuição do número de imigrantes ao longo dos anos.
# - As configurações de animação devem fazer com que as duas linhas sejam exibidas e animadas ao mesmo tempo.
# 
# **Dicas:**
# 
# - Crie um DataFrame com os dados da Argentina e não se esqueça de deixar a coluna de anos no tipo int(inteiro).
# - Use o código fornecido para o Brasil como base e adapte-o para incluir os dados da Argentina.
# - Para configurar as animações você pode fazer um Loop for para percorrer o DataFrame dados_brasil e para cada iteração, criar uma nova lista contendo dois objetos do tipo go.Scatter, um para cada país. Em seguida, cada lista pode ser usada para criar um objeto go.Frame, que é adicionado à lista de frames. Por fim, a lista de frames pode ser atribuída ao objeto fig, que é a figura do gráfico a ser animado. Com isso, quando a animação for iniciada, o gráfico exibirá as duas linhas em movimento, uma para o Brasil e outra para a Argentina.

# %%
import plotly.graph_objs as go

dados_argentina['ano'] = dados_argentina['ano'].astype(int)
dados_brasil['ano'] = dados_brasil['ano'].astype(int)

import plotly.graph_objs as go

# # Criando uma figura
fig = go.Figure()

# Adicionando a linha com os dados do Brasil 
fig.add_trace(
    go.Scatter(x=[dados_brasil['ano'].iloc[0]], y=[dados_brasil['imigrantes'].iloc[0]], mode='lines', name='Imigrantes do Brasil', line=dict(width=4))
)

# Adicionando a linha com os dados da Argentina
fig.add_trace(
    go.Scatter(x=[dados_argentina['ano'].iloc[0]], y=[dados_argentina['imigrantes'].iloc[0]], mode='lines', name='Imigrantes da Argentina', line=dict(width=4))
)

# Definindo as configurações de layout
fig.update_layout(
    title=dict(
        text='<b>Imigração do Brasil e da Argentina para o Canadá no período de 1980 a 2013',
        x=0.1,

        font=dict(size=18)
    ),
    xaxis=dict(range=[1980, 2013], autorange=False, title='<b>Ano</b>'),
    yaxis=dict(range=[0, 3000], autorange=False, title='<b>Número de imigrantes</b>'),
    updatemenus=[dict(
        type='buttons',
        showactive=False,
        buttons=[dict(
            label='Play',
            method='animate',
            args=[None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}]
        )]
    )],
    width=1200, # largura da figura em pixels
    height=600 # altura da figura em pixels
)

# Definindo as configurações de animação
frames = []
for i in range(len(dados_brasil)):
    frame_data = [
        go.Scatter(x=dados_brasil['ano'].iloc[:i+1], y=dados_brasil['imigrantes'].iloc[:i+1]),
        go.Scatter(x=dados_argentina['ano'].iloc[:i+1], y=dados_argentina['imigrantes'].iloc[:i+1])
    ]
    frame = go.Frame(data=frame_data)
    frames.append(frame)
fig.frames = frames

# Mostrando a figura
fig.show()


# %% [markdown]
# Neste caso nós adicionamos duas linhas, uma para cada país com o `fig.add_trace()`. Para conseguir animar as duas linhas juntas, temos a criação de uma lista de frames que serão usados para a animação do gráfico. O loop for percorre o comprimento dos dados de imigração do Brasil (que deve ser o mesmo dos dados de imigração da Argentina). Para cada índice i no loop, cria-se um `frame_data` que contém dois objetos Scatter do Plotly: um para o Brasil e outro para a Argentina. Cada Scatter é definido pelos dados correspondentes de imigração para o país em questão até o índice i. Em seguida, é criado um objeto frame que contém o `frame_data` correspondente ao índice i. Finalmente, esse objeto frame é adicionado à lista de frames. O resultado é uma lista de frames que representam a evolução da imigração do Brasil e da Argentina para o Canadá ao longo do tempo, que serão usados para criar a animação do gráfico.

# %% [markdown]
# # Exercícios / Teste

# %% [markdown]
# ## Facilitando a interpretação de dados

# %% [markdown]
# Em um mundo movido pela busca constante por insights e resultados, Théo é um cientista de dados que está trabalhando em um projeto que envolve a análise e a previsão de vendas de um e-commerce. Imerso nesse projeto desafiador, ele concentra seus esforços para alcançar seus objetivos.
# 
# Nesse momento os dados que ele possui estão armazenados em um DataFrame chamado df, que foi obtido com o seguinte código:
# 
# ```
# import pandas as pd
# 
# 
# dados_vendas = {
#     'mes': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#     'vendas': [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000]
# }
# 
# df = pd.DataFrame(dados_vendas)
# ```
# 
# Com suas habilidades afiadas, Théo precisa criar um gráfico que mostre a evolução das vendas ao longo do tempo e adicione um título e rótulos aos eixos X e Y para facilitar a interpretação dos dados. Para isso, ele decide utilizar a biblioteca Matplotlib.
# 
# Qual é o código correto para criar a figura, adicionar um título e os rótulos dos eixos que você indicaria a ele?

# %%
dados_vendas = {
    'mes': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'vendas': [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000]
}

df_vendas = pd.DataFrame(dados_vendas)

# %%
fig, ax = plt.subplots(figsize = (10,4))
ax.plot(df_vendas['mes'], df_vendas['vendas'])
ax.set_title('Evolução das vendas\nÚltimos 12 Meses')
ax.set_xlabel('Mês')
ax.set_ylabel('Evolução das Vendas')
#ax.xaxis.set_major_locator(plt.MultipleLocator(5))
plt.show()

# %% [markdown]
# ## Desafio: visualizando dados de venda de diferentes lojas

# %% [markdown]
# Você trabalha como Analista de Dados em uma empresa de varejo e recebeu a tarefa de criar uma figura com subplots que apresente a variação no número de vendas em quatro diferentes lojas ao longo de um ano. A gerência da empresa precisa visualizar de forma clara as tendências de vendas em cada loja, para que possam tomar decisões estratégicas sobre os estoques e ações de marketing. Para isso, você deve criar quatro subplots dispostos em duas linhas e duas colunas, onde cada subplot representa uma loja diferente. Nesse desafio, cada subplot deve apresentar um gráfico de linhas que mostre a variação do número de vendas ao longo dos meses do ano.
# 
# Agora, chegou a hora de mostrar suas habilidades em análise de dados e visualização! Para criar o DataFrame com o número de vendas das lojas e criar a figura, utilize as informações abaixo:
# 
# ```
# lojas = ['A', 'B', 'C', 'D']
# 
# vendas_2022 = {'Jan': [100, 80, 150, 50],
#     'Fev': [120, 90, 170, 60],
#     'Mar': [150, 100, 200, 80],
#     'Abr': [180, 110, 230, 90],
#     'Mai': [220, 190, 350, 200],
#     'Jun': [230, 150, 280, 120],
#     'Jul': [250, 170, 300, 140],
#     'Ago': [260, 180, 310, 150],
#     'Set': [240, 160, 290, 130],
#     'Out': [220, 140, 270, 110],
#     'Nov': [400, 220, 350, 190],
#     'Dez': [300, 350, 400, 250]
# }
# ```
# 
# **Dica:** Para facilitar a criação dos subplots, você pode definir a coluna "Lojas" como índice do DataFrame e utilizar a propriedade loc da biblioteca Pandas para plotar cada uma das lojas.
# 
# >Não se esqueça de adicionar um título geral à figura, títulos aos subplots e rótulos aos eixos. Além disso, se atente ao tamanho da figura e ao espaçamento entre os subplots!

# %%
lojas = ['A', 'B', 'C', 'D']

vendas_2022 = {'Jan': [100, 80, 150, 50],
    'Fev': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'Mai': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Set': [240, 160, 290, 130],
    'Out': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dez': [300, 350, 400, 250]
}

# %%
import pandas as pd


# %%
df_vendas = pd.DataFrame(vendas_2022, index=lojas)

# %%
df_vendas

# %%
# cria a figura e os subplots
fig, axs = plt.subplots(2, 2, figsize = (14,8))

# ajusta os espaçamentos entre os subplots
plt.subplots_adjust(wspace =0.3, hspace=0.4)

# adiciona um título geral para os subplots
fig.suptitle('Vendas no período de janeiro a dezembro de 2022 nas lojas A, B, C e D')

# adiciona os gráficos em cada um dos subplots
axs[0,0].plot(df_vendas.loc['A'])
axs[0,0].set_title('Vendas na loja A')

axs[0,1].plot(df_vendas.loc['B'])
axs[0,1].set_title('Vendas na loja B')

axs[1,0].plot(df_vendas.loc['C'])
axs[1,0].set_title('Vendas na loja C')

axs[1,1].plot(df_vendas.loc['D'])
axs[1,1].set_title('Vendas na loja C')

# adiciona rótulos para os eixos X e Y
for ax in axs.flat:
  ax.set_xlabel('Mês')
  ax.set_ylabel('Número de vendas')

# exibe figura
plt.show()

# %% [markdown]
# ## Testando o estilização

# %%
IPython_default = plt.rcParams.copy()

# %%
with plt.style.context('fivethirtyeight'):
  fig, ax = plt.subplots(figsize=(8, 4))
  ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'], lw=3)
  ax.set_title('Imigração do Brasil para o Canadá\n1980 a 2013', fontsize=20, loc='left')
  ax.set_ylabel('Número de imigrantes', fontsize=14)
  ax.set_xlabel('Ano', fontsize=14)
  ax.yaxis.set_tick_params(labelsize=12)
  ax.xaxis.set_tick_params(labelsize=12)
  ax.xaxis.set_major_locator(plt.MultipleLocator(5))
  plt.show()

# %% [markdown]
# ## Desafio: customizando os subplots com dados de vendas de diferentes lojas

# %% [markdown]
# Mais uma etapa de desafio se inicia! Aproveite a oportunidade proposta e mergulhe nas possibilidades. Na aula anterior, você teve o desafio de criar uma figura com subplots que apresentam a variação no número de vendas em quatro diferentes lojas ao longo de um ano. Agora é o momento de elevar essa figura a um novo patamar! É a hora de personalizá-la! Nesta segunda parte do desafio, você deve explorar as opções de customização dos subplots para deixar a figura mais clara e atraente para a gerência da empresa.
# 
# Algumas ideias de customização que você pode explorar são:
# 
# - Alterar a posição dos títulos dos subplots para esquerda.
# - Aumentar o tamanho da fonte do título geral da figura para destacá-lo.
# - Aumentar o tamanho dos títulos e rótulos dos eixos dos subplots.
# - Deixar as linhas com a espessura maior.
# - Alterar a cor das linhas de cada loja para diferenciá-las ainda mais.
# - Fique à vontade para testar mais customizações!
# 
# E mais uma dica: você pode reduzir o tamanho do código utilizando o comando for i, ax in enumerate(axs.flat): que permite um loop iterando sobre todos os subplots da figura. Dentro desse loop você pode passar as funções plot, set_title, set_xlabel, set_ylabel e etc…
# 
# Lembrando que os dados são os seguintes:
# ```
# lojas = ['A', 'B', 'C', 'D']
# 
# vendas_2022 = {'Jan': [100, 80, 150, 50],
#     'Fev': [120, 90, 170, 60],
#     'Mar': [150, 100, 200, 80],
#     'Abr': [180, 110, 230, 90],
#     'Mai': [220, 190, 350, 200],
#     'Jun': [230, 150, 280, 120],
#     'Jul': [250, 170, 300, 140],
#     'Ago': [260, 180, 310, 150],
#     'Set': [240, 160, 290, 130],
#     'Out': [220, 140, 270, 110],
#     'Nov': [400, 220, 350, 190],
#     'Dez': [300, 350, 400, 250]
# }
# ```

# %% [markdown]
# ### Resolução
# 
# Este código cria uma figura com 4 subplots (2 linhas e 2 colunas), onde cada subplot representa as vendas de uma loja em cada mês do ano. O tamanho da figura é definido com o parâmetro figsize da função subplots(). Em seguida, o espaço entre os subplots é ajustado com a função subplots_adjust().
# 
# O título geral da figura é adicionado com a função suptitle(), onde é definido o texto e o tamanho da fonte com o parâmetro fontsize.
# 
# Uma lista de cores é criada com as cores que serão usadas para plotar as linhas em cada subplot. O comando enumerate(axs.flat) permite que o loop a seguir itere sobre todos os subplots da figura. Dentro do loop, o comando plot() é usado para plotar as vendas da loja correspondente ao subplot atual. A cor da linha é definida pelo índice do subplot na lista de cores. O título do subplot é definido com o nome da loja e o parâmetro loc='left' alinha o título à esquerda. Os rótulos dos eixos X e Y são definidos com as funções set_xlabel() e set_ylabel(), e as fontes são definidas pelo parâmetro fontsize. As ticks dos eixos são definidas com a função tick_params(). Por fim, um grid é adicionado aos subplots com a função grid().

# %% [markdown]
# ## Criando gráficos animados

# %%
import plotly.graph_objs as go

dados_brasil['ano'] = dados_brasil['ano'].astype(int)

# Criando uma figura
fig = go.Figure()

# Adicionando a linha do gráfico e definindo a espessura da linha
fig.add_trace(
    go.Scatter(x=[dados_brasil['ano'].iloc[0]], y=[dados_brasil['imigrantes'].iloc[0]], mode='lines', name='Imigrantes', line=dict(width=4))
)

# Definindo as configurações de layout
fig.update_layout(
    title=dict(
        text='<b>Imigração do Brasil para o Canadá no período de 1980 a 2013</b>',
        x=0.12,
        xanchor='left',
        font=dict(size=20)
    ),
    xaxis=dict(range=[1980, 2013], autorange=False, title='<b>Ano</b>'),
    yaxis=dict(range=[0, 3000], autorange=False, title='<b>Número de imigrantes</b>'),
    updatemenus=[dict(
        type='buttons',
        showactive=False,
        buttons=[dict(
            label='Play',
            method='animate',
            args=[None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}]
        )]
    )],
    width=1000,
    height=500
)

# Definir as configurações de animação
frames = [go.Frame(data=[go.Scatter(x=dados_brasil['ano'].iloc[:i+1], y=dados_brasil['imigrantes'].iloc[:i+1])]) for i in range(len(dados_brasil))]
fig.frames = frames

# Mostrando a figura
fig.show()