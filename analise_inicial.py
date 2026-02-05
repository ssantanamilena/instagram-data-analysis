import pandas as pd
import matplotlib.pyplot as plt

# Importando base de dados
base = pd.read_excel("bd_instagram.xlsx")

# Visualizando minha base
print(base.head())

# Visualizando nome de todas as colunas
print(base.columns)

# Visualiando o tipo das colunas base
base.info()

# Visualizando quantidade de nulos nas colunas
print(base.isnull().sum())

# Visualizando quantidade de nulos na linhas
base[base.isnull().any(axis=1)]
base = base.fillna(0)

# Verificando qual da mais engajamento reels ou fotos?
print(base.groupby("Tipo")[["Curtidas", "Comentários"]].mean())

# Vericando o post mais curtido
print("Post com mais curtidas:")
post_mais_curtido = base.loc[base["Curtidas"].idxmax()]
print(post_mais_curtido)

# Verificando o post mais comentado
print("Post com mais comentários:")
post_mais_comentado = base.loc[base["Comentários"].idxmax()]
print(post_mais_comentado)

# Tag com mais engajamento
print(base.groupby("Tags")[["Curtidas", "Comentários"]].mean())

# Média de curtidas por tipo de post
curtidas_tipo = base.groupby("Tipo")["Curtidas"].mean()

# Gráfico
curtidas_tipo.plot(kind="bar")

# Título e nomes
plt.title("Média de Curtidas por Tipo de Post")
plt.xlabel("Tipo de Post")
plt.ylabel("Curtidas Médias")

# Mostrar gráfico
plt.show()

curtidas_tags = base.groupby("Tags")["Curtidas"].mean()

curtidas_tags.plot(kind="bar")
plt.title("Média de Curtidas por Tag")
plt.xlabel("Tag")
plt.ylabel("Curtidas Médias")
plt.show()

base["Data"] = pd.to_datetime(base["Data"])

curtidas_dia = base.groupby("Data")["Curtidas"].sum()

curtidas_dia.plot()
plt.title("Curtidas ao longo do tempo")
plt.xlabel("Data")
plt.ylabel("Curtidas")
plt.show()
