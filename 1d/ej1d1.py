"""
Enunciado:
Este ejercicio introduce el uso de bibliotecas especializadas para acceder a APIs de forma
sencilla y estructurada. En concreto, utilizaremos la biblioteca pybikes que proporciona
wrappers para múltiples sistemas de bicicletas compartidas en todo el mundo.

En lugar de construir nuestro propio cliente HTTP y procesar manualmente los datos JSON,
aprenderemos a utilizar herramientas existentes que hacen este trabajo por nosotros.

Tareas:
1. Explorar los sistemas de bicicletas disponibles
2. Obtener información sobre el sistema de Barcelona (Bicing)
3. Analizar los datos de las estaciones

Esta práctica ilustra cómo las bibliotecas especializadas simplifican el acceso a APIs
y permiten concentrarse en el análisis de datos en lugar de en los detalles técnicos
de la comunicación con la API.
"""

import pybikes
import pandas as pd
import time
from typing import List, Dict, Any, Optional
import matplotlib.pyplot as plt
import sys


def listar_sistemas_disponibles() -> List[str]:
    """
    Obtiene una lista de todos los sistemas de bicicletas disponibles en pybikes.

    Returns:
        List[str]: Lista de identificadores de sistemas disponibles
    """
    # Implementa aquí la lógica para obtener y devolver la lista
    # de sistemas disponibles en pybikes
     try:
        # Get all data names (with .json):
        all_data: List[str] = pybikes.get_all_data()

        # Strip of the .json part:
        all_data = [name.replace(".json", "") for name in all_data]

        return sorted(all_data)

    except AttributeError:
        return []


def buscar_sistema_por_ciudad(ciudad: str) -> List[str]:
    """
    Busca sistemas de bicicletas que contengan el nombre de la ciudad especificada.

    Args:
        ciudad (str): Nombre de la ciudad a buscar

    Returns:
        List[str]: Lista de sistemas que coinciden con la búsqueda
    """
    # Implementa aquí la lógica para buscar y devolver sistemas
    # que coincidan con la ciudad especificada
    sistemas = []
    for system_tag in listar_sistemas_disponibles():
        try:
            # Get all the metadata for the system:
            # print(system_tag)
            system_data = pybikes.get(system_tag)
            city = system_data.meta.get("city")

            # Check if the city is the same as the one searched:
            if ciudad.lower() in city.lower():
                sistemas.append(system_tag)

        except Exception as e:
            # print(e)
            continue
    return sistemas


def obtener_info_sistema(tag: str) -> Dict[str, Any]:
    """
    Obtiene la información del sistema especificado.

    Args:
        tag (str): Identificador del sistema (por ejemplo, 'bicing')

    Returns:
        Dict[str, Any]: Metadatos del sistema o None si no existe
    """
    # Implementa aquí la lógica para obtener y devolver
    # los metadatos del sistema especificado
    try:
        system = pybikes.get(tag)
        return {
            'name': system.meta.get('name', ''),
            'city': system.meta.get('city', ''),
            'country': system.meta.get('country', ''),
            'system': system.meta.get('system', '')
        }
    except:
        return None


def obtener_estaciones(tag: str) -> Optional[List]:
    """
    Obtiene la lista de estaciones del sistema especificado.

    Args:
        tag (str): Identificador del sistema (por ejemplo, 'bicing')

    Returns:
        Optional[List]: Lista de objetos estación o None si hay error
    """
    # Implementa aquí la lógica para obtener y devolver
    # la lista de estaciones del sistema especificado
    try:
        bike_system = pybikes.get(tag)
        bike_system.update()
        return bike_system.stations
    except Exception:
        return None


def crear_dataframe_estaciones(estaciones: List) -> pd.DataFrame:
    """
    Convierte la lista de estaciones en un DataFrame de pandas.

    Args:
        estaciones (List): Lista de objetos estación

    Returns:
        pd.DataFrame: DataFrame con la información de las estaciones
    """
    # Implementa aquí la lógica para convertir la lista de estaciones
    # en un DataFrame de pandas con al menos las columnas:
    # nombre, latitud, longitud, bicicletas disponibles, espacios libres
    if not estaciones:
        return pd.DataFrame()

    data = []
    for station in estaciones:
        data.append({
            'name': station.name,
            'latitude': station.latitude,
            'longitude': station.longitude,
            'bikes': station.bikes,
            'free': station.free
        })
    return pd.DataFrame(data)


def visualizar_estaciones(df: pd.DataFrame) -> None:
    """
    Genera una visualización simple de la disponibilidad de bicicletas.

    Args:
        df (pd.DataFrame): DataFrame con la información de las estaciones
    """
    # Implementa aquí la lógica para crear un gráfico de barras que muestre
    # las 10 estaciones con más bicicletas disponibles
    


if __name__ == "__main__":
    # Listar sistemas disponibles
    print("\nSistemas de bicicletas disponibles:")
    sistemas = listar_sistemas_disponibles()
    print(f"Total: {len(sistemas)} sistemas")
    print(f"Algunos ejemplos: {sistemas[:5]}")

    # Buscar sistemas en Barcelona
    print("\nBuscando sistemas en Barcelona:")
    sistemas_barcelona = buscar_sistema_por_ciudad("Barcelona")
    print(f"Encontrados: {len(sistemas_barcelona)}")
    for sistema in sistemas_barcelona:
        print(f"- {sistema}")

    # Si se encuentra el sistema de Barcelona (Bicing), obtener información
    if "bicing" in sistemas:
        print("\nInformación del sistema Bicing de Barcelona:")
        info = obtener_info_sistema("bicing")
        for key, value in info.items():
            print(f"{key}: {value}")

        # Obtener estaciones
        print("\nObteniendo estaciones...")
        estaciones = obtener_estaciones("bicing")
        if estaciones:
            print(f"Obtenidas {len(estaciones)} estaciones")

            # Convertir a DataFrame
            print("\nConvirtiendo a DataFrame...")
            df = crear_dataframe_estaciones(estaciones)
            print(df.head())

            # Estadísticas básicas
            print("\nEstadísticas de bicicletas disponibles:")
            print(df['bikes'].describe())

            # Visualización
            print("\nVisualizando estaciones con más bicicletas disponibles...")
            visualizar_estaciones(df)
        else:
            print("No se pudieron obtener las estaciones.")
    else:
        print("El sistema 'bicing' no está disponible en pybikes.")

