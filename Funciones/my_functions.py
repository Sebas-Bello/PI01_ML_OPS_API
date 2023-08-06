import pandas as pd
import numpy as np
import ast

data = pd.read_csv('Dataset/Data_Clean_steam_games.csv', index_col=0)


# API 1
 
def genero(Año: str):
    try:
        año_str = str(Año)  # Convertir a cadena
        if not año_str.isdigit():
            raise ValueError(f"El año '{año_str}' no es un valor numérico válido.")
        
        año_num = int(Año)
        
        # Filtrar el DataFrame para obtener solo las filas del año ingresado
        df_filtrado = data[data['year_release'] == año_num]

        # Contar los registros por género
        genres_counts = {}

        for genres_list in df_filtrado['genres']:
            if isinstance(genres_list, str):  # Verificar si es una cadena antes de dividir
                genres = genres_list.split(', ')
                for genre in genres:
                    if genre in genres_counts:
                        genres_counts[genre] += 1
                    else:
                        genres_counts[genre] = 1

        # Ordenar y tomar los 5 géneros con más registros
        top_5_generos = dict(sorted(genres_counts.items(), key=lambda item: item[1], reverse=True)[:5])
        
        if not top_5_generos:
            return f"No hay géneros disponibles para el año {Año}"

        return {año_num: top_5_generos}
    except ValueError as e:
        opciones_disponibles = '\n'.join(map(str, sorted(data['year_release'].unique())))
        return  print(f"Error: {e}\nEl año '{Año}' no es válido. Años disponibles:\n{opciones_disponibles}")
    
    
#API 2

def juegos(Año: str):
    try:
        año_str = str(Año)  # Convertir a cadena
        if not año_str.isdigit():
            raise ValueError(f"El año '{año_str}' no es un valor numérico válido.")
        
        año_num = int(Año)
        
        # Filtrar el DataFrame para obtener solo las filas del año ingresado
        df_filtrado = data[data['year_release'] == año_num]
        
        # Crear un diccionario para almacenar el nombre del juego y el año
        juegos_por_año = {}
        
        # Iterar sobre las filas filtradas y agregar el nombre del juego y el año al diccionario
        for index, row in df_filtrado.iterrows():
            juego = row['app_name']
            juegos_por_año[juego] = año_num
        
        if not juegos_por_año:
            return f"No hay juegos para el año {Año}"
        
        return juegos_por_año
    except ValueError as e:
        opciones_disponibles = '\n'.join(map(str, sorted(data['year_release'].unique())))
        return print(f"Error: {e}\nEl año '{Año}' no es válido. Años disponibles:\n{opciones_disponibles}")
    

#API 3
   
def specs(Año: str):
    try:
        año_str = str(Año)  # Convertir a cadena
        if not año_str.isdigit():
            raise ValueError(f"El año '{año_str}' no es un valor numérico válido.")
        
        año_num = int(Año)
        
        # Filtrar el DataFrame para obtener solo las filas del año ingresado
        df_filtrado = data[data['year_release'] == año_num]

        # Contar los registros por género
        genres_counts = {}

        for genres_list in df_filtrado['specs']:
            genres = genres_list.split(', ')
            for genre in genres:
                if genre in genres_counts:
                    genres_counts[genre] += 1
                else:
                    genres_counts[genre] = 1

        # Ordenar y tomar los 5 géneros con más registros
        top_5_generos = dict(sorted(genres_counts.items(), key=lambda item: item[1], reverse=True)[:5])
        
        if not top_5_generos:
            return f"No hay géneros disponibles para el año {Año}"

        return {año_num: top_5_generos}
    except ValueError as e:
        opciones_disponibles = '\n'.join(map(str, sorted(data['year_release'].unique())))
        return  print(f"Error: {e}\nEl año '{Año}' no es válido. Años disponibles:\n{opciones_disponibles}")
    

#API 4

def earlyacces(Año: str):
    try:
        año_str = str(Año)  # Convertir a cadena
        if not año_str.isdigit():
            raise ValueError(f"El año '{año_str}' no es un valor numérico válido.")
        
        año_num = int(Año)
        
        # Filtrar el DataFrame para obtener solo las filas del año ingresado y que tengan early access True
        df_filtrado = data[(data['year_release'] == año_num) & (data['early_access'] == True)]
        
        # Contar la cantidad de juegos con early access True
        cantidad_early_access = df_filtrado.shape[0]
        
        if not cantidad_early_access:
            return {año_num: 0}
        
        return {año_num: cantidad_early_access}
    except ValueError as e:
        opciones_disponibles = '\n'.join(map(str, sorted(data['year_release'].unique())))
        return print(f"Error: {e}\nEl año '{Año}' no es válido. Años disponibles:\n{opciones_disponibles}")
    
    
#API 5

def sentiment(Año: str):
    try:
        año_str = str(Año)  # Convertir a cadena
        if not año_str.isdigit():
            raise ValueError(f"El año '{año_str}' no es un valor numérico válido.")
        
        año_num = int(Año)
        
        # Filtrar el DataFrame para obtener solo las filas del año ingresado
        df_filtrado = data[data['year_release'] == año_num]
        
        # Contar la cantidad de registros para cada categoría de sentimiento
        conteo_sentimientos = df_filtrado['sentiment'].value_counts()
        
        # Convertir el diccionario de conteo_sentimientos en un diccionario
        diccionario_sentimientos = conteo_sentimientos.to_dict()
        
        if not diccionario_sentimientos:
            return f"No hay especificaciones disponibles para el año {Año}"
        
        return {año_num: diccionario_sentimientos}
    except ValueError as e:
        opciones_disponibles = '\n'.join(map(str, sorted(data['year_release'].unique())))
        return print(f"Error: {e}\nEl año '{Año}' no es válido. Años disponibles:\n{opciones_disponibles}")
    

#API 6

def metascore(Año: str):
    try:
        año_str = str(Año)  # Convertir a cadena
        if not año_str.isdigit():
            raise ValueError(f"El año '{año_str}' no es un valor numérico válido.")
        
        año_num = int(Año)
        
        # Filtrar el DataFrame para obtener solo las filas del año ingresado
        df_filtrado = data[data['year_release'] == año_num]
        
        # Ordenar los juegos según el puntaje Metascore en orden descendente
        top_juegos_metascore = df_filtrado.sort_values(by='metascore', ascending=False).head(5)
        
        # Convertir el DataFrame en un diccionario con el título del juego como clave y el Metascore como valor
        resultado = top_juegos_metascore.set_index('app_name')['metascore'].to_dict()
        
        if not resultado:
            return f"No hay especificaciones disponibles para el año {Año}"
        
        return {año_num: resultado}
    except ValueError as e:
        opciones_disponibles = '\n'.join(map(str, sorted(data['year_release'].unique())))
        return print(f"Error: {e}\nEl año '{Año}' no es válido. Años disponibles:\n{opciones_disponibles}")
    
#asasas