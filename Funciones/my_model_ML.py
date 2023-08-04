import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV


model_data = pd.read_csv('Dataset/Data_ML.csv', index_col=0)




X = model_data.drop(['price', 'genres'], axis=1)
y = model_data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


best_bagging_model = BaggingRegressor(
    base_estimator=DecisionTreeRegressor(max_depth=15),  
    n_estimators=50,  
    max_samples=0.9,  
    max_features=0.7,  
    random_state=42
)


best_bagging_model.fit(X_train, y_train)
y_pred = best_bagging_model.predict(X_test)



def predict_price_and_rmse(genres, earlyaccess):
    try:
        # Convertir True o False a 1 o 0 para earlyaccess
        earlyaccess_int = int(earlyaccess)

        # Filtrar el DataFrame model_data según los géneros
        filtered_data = model_data[(model_data['genres'].str.contains(genres, case=False)) & (model_data['early_access'] == earlyaccess_int)]

        if filtered_data.empty:
            genres_list_of_lists = [genre.split(', ') for genre in model_data['genres']]
            genres_flat_list = [genre for sublist in genres_list_of_lists for genre in sublist]
            unique_genres = '\n'.join(set(genres_flat_list))
            
            available_earlyaccess = [False, True]
            raise ValueError(f"No se encontraron datos para el género especificado '{genres}' y el estado de acceso anticipado '{earlyaccess}'.\nGéneros disponibles:\n{unique_genres}\nEstados de acceso anticipado disponibles: {available_earlyaccess}")

        # Eliminar las columnas "genres" y "price" de filtered_data y almacenar en input_data
        input_data = filtered_data.drop(['genres', 'price'], axis=1)

        # Realizar la predicción del precio
        predicted_prices = best_bagging_model.predict(input_data)

        # Calcular el precio promedio para el género
        average_predicted_price = predicted_prices.mean()

        # Obtener los datos de prueba correspondientes a los géneros filtrados
        X_filtered = filtered_data.drop(['price', 'genres'], axis=1)
        y_filtered = filtered_data['price']

        # Realizar predicciones en los datos de prueba filtrados
        y_pred_filtered = best_bagging_model.predict(X_filtered)

        # Calcular el RMSE en los datos de prueba filtrados
        rmse_filtered = np.sqrt(mean_squared_error(y_filtered, y_pred_filtered, squared=False))

        # Crear un diccionario con los resultados
        results = {
            f"Precio previsto para el genero '{genres}'": f"{average_predicted_price:.2f}",
            f"RMSE para el genero '{genres}'": f"{rmse_filtered:.2f}"
        }
        
        return results
    except ValueError as e:
        return print("Error:", e)



predict_price_and_rmse("action", True)