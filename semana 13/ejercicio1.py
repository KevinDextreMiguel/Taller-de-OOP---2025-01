import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#leer el archivo
df = pd.read_excel('periodos.xlsx')

df.head()

#Renombrar combre de las columnas
diccionario = {"año":"anio","contaminacion PM 2.5":"contaminacion_pm_2_5"}
df.rename(columns=diccionario, inplace=True)
df.head(2)

# cantidad de filas y columnas
# (24, 6) -> (cantidad filas, cantidad de columnas)
df.shape

# Cantidad de datos
df.size

# ver la información del dataset
df.info()

# ver nombre de las columnas
df.columns

# ver tipo de dato de las columnas
df.dtypes

df.head(2)

# uso de iloc: [fila,columna]
df.iloc[2:5,:]

# uso de iloc: [fila,nombre_columna]
df.loc[:3,['anio','contaminacion_pm_2_5']]

df.tail(2)

#Agreagr una fila
nuevo_dato = {"anio":2022,"mes":"abril","ciudad":"lima","casos":278,"temperatura":29.5,"contaminacion_pm_2_5":30}
tamanio = len(df)
df.loc[tamanio] = nuevo_dato

df.tail(2)

# Agrupar por columna
df["anio"].groupby(df["anio"]).count()

#matplotlib
#Gràfico de línea 
df_grouped = df.groupby("anio").sum().reset_index()

plt.plot(df_grouped["anio"],df_grouped["casos"],marker='o',color='red')

#Agregar tìtulos y etiquetas
plt.title("Casos de Contaminación PM 2.5 por año")
plt.xlabel("Año")
plt.ylabel("Contaminación PM 2.5")

#mostrar la gràfica
plt.show()


#Gràfico de barras
plt.bar(df["ciudad"],df["casos"],color='skyblue')
# plt.barh(df["ciudad"],df["casos"],color='skyblue') -> horizontal

#Agregar tìtulos y etiquetas
plt.title("Cantidad de casos por ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Cantidad de casos")

#mostrar la gràfica
plt.show()


#Histograma
plt.hist(df["casos"],color='green',bins=6)

#Agregar tìtulos y etiquetas
plt.title("Cantidad de casos")
plt.xlabel("Cantidad")
plt.ylabel("Frecuencia")

#mostrar la gràfica
plt.show()


#Gràfica de dispersión
plt.scatter(df["temperatura"],df["casos"],color='green')

#Agregar tìtulos y etiquetas
plt.title("Gràfico de dispersiòn temperatura vs casos")
plt.xlabel("temperatura")
plt.ylabel("casos")

#mostrar la gràfica
plt.show()


#Gràfico circular
contar_ciudad_contaminacion_pm = df.groupby("ciudad")["contaminacion_pm_2_5"].sum().reset_index()

plt.pie(contar_ciudad_contaminacion_pm["contaminacion_pm_2_5"],labels=contar_ciudad_contaminacion_pm["ciudad"],autopct='%1.1f%%')

#Agregar tìtulos y etiquetas
plt.title("Distribuciòn de contaminaciòn PM 2.5 por ciudad")
#mostrar la gràfica
plt.show()


#Seaborn
#Gràfico de barras
ax = sns.barplot(x="ciudad",y="casos",data=df,ci = None)

# Agragar valores a las barras
for p in ax.patches:
    ax.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')

#Agregar tìtulos y etiquetas
plt.title("Casos por ciudad")
plt.xlabel("Casos")
plt.ylabel("Ciudad")

#mostrar la gràfica
plt.show()


#Gràfico de barras apiladas
sns.barplot(x="anio",y="casos",hue="ciudad",data=df,ci = None)

#Agregar tìtulos y etiquetas
plt.title("Casos por año y ciudad")
plt.xlabel("Año")
plt.ylabel("Casos")

#mostrar la gràfica
plt.show()



#Gràfico de dispersión
sns.scatterplot(x="temperatura",y="casos",hue="ciudad",data=df)

#Agregar tìtulos y etiquetas
plt.title("Gràfico de dispersiòn temperatura vs casos")
plt.xlabel("temperatura")
plt.ylabel("casos")
plt.show()


#Gràfico de líneas
sns.lineplot(x="anio",y="casos",hue="ciudad",data=df,ci=None,marker='o')

#Agregar tìtulos y etiquetas
plt.title("Casos por año y ciudad")
plt.xlabel("Año")
plt.ylabel("Casos")

plt.show()

#
