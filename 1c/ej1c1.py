"""
Enunciado:
Desarrolla un cliente HTTP básico utilizando la biblioteca requests de Python.
El cliente debe realizar peticiones a la API pública del sistema de bicicletas compartidas de Barcelona
que sigue el estándar General Bikeshare Feed Specification (GBFS).

Tareas:
1. Realizar una petición GET a la API de GBFS para obtener la lista de feeds disponibles
2. Procesar la respuesta JSON para extraer información relevante sobre los endpoints
3. Manejar posibles errores en las peticiones

Esta es una introducción a las peticiones HTTP en Python utilizando la biblioteca requests
para entender cómo interactuar con APIs web.

Tu tarea es completar la implementación de las funciones indicadas.
"""

import requests

def get_gbfs_feeds():
    """
    Realiza una petición GET a la API de GBFS de Barcelona para obtener
    la lista de feeds (endpoints) disponibles.

    Returns:
        dict: Datos de la respuesta si se obtiene correctamente
        None: Si ocurre un error en la petición
    """
    # La URL base de la API de GBFS de Barcelona
    base_url = "https://barcelona-sp.publicbikesystem.net/customer/gbfs/v2/gbfs.json"

    # Debes completar la función:
    # 1. Realizar una petición GET a la URL
    # 2. Verificar que la respuesta sea correcta (código 200)
    # 3. Devolver los datos en formato JSON
    # 4. Manejar posibles errores (conexión, formato, etc.)
    try:
        # Realizar petición GET a la URL
        response = requests.get(base_url)

        # Comprobar si la petición fue exitosa (código 200)
        if response.status_code == 200:
            # Devolver los datos en formato JSON
            return response.json()
        else:
            # Si el código de estado no es 200, imprimir un mensaje de error
            print(f"Error: La petición no fue exitosa. Código de estado: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Capturar cualquier error que pueda ocurrir durante la petición
        print(f"Error al realizar la petición: {e}")
        return None


def extract_feeds_info(feeds_data):
    """
    Extrae la información de los feeds disponibles a partir de los datos recibidos.

    Args:
        feeds_data (dict): Datos de los feeds obtenidos de la API

    Returns:
        list: Lista de diccionarios con los campos 'name' y 'url' de cada feed
        None: Si los datos de entrada son None o no tienen el formato esperado
    """
    # Debes completar la función:
    # 1. Verificar que feeds_data no es None
    # 2. Extraer la lista de feeds para el idioma inglés (en)
    # 3. Crear y devolver una lista con la información relevante de cada feed
    # 4. Manejar posibles errores en la estructura de los datos
    if feeds_data is None:
        return None

    try:
        # Extraer la lista de feeds para el idioma inglés (en)
        feeds = feeds_data["data"]["en"]["feeds"]

        # Crear una lista con la información relevante de cada feed
        feeds_info = []
        for feed in feeds:
            feeds_info.append({
                "name": feed["name"],
                "url": feed["url"]
            })

        return feeds_info
    except (KeyError, TypeError) as e:
        # Manejar el caso en que los datos no tienen la estructura esperada
        print(f"Error al extraer la información de los feeds: {e}")
        return None

def print_feeds_summary(feeds_info):
    """
    Imprime un resumen formateado de los feeds disponibles.

    Args:
        feeds_info (list): Lista de feeds con los campos 'name' y 'url'
    """
    if feeds_info is None:
        print("Error: No feeds information available")
        return

    # Imprimir título y cantidad de feeds
    print("=" * 50)
    print("Barcelona Bike-Sharing System - GBFS Feeds")
    print("=" * 50)
    print(f"Available Feeds: {len(feeds_info)}")
    print("-" * 50)

    # Imprimir información de cada feed
    for feed in feeds_info:
        print(f"Name: {feed['name']}")
        print(f"URL: {feed['url']}")
        print("-" * 50)


if __name__ == '__main__':
    # Obtener los datos de los feeds disponibles
    feeds_data = get_gbfs_feeds()

    # Extraer la información relevante
    feeds_info = extract_feeds_info(feeds_data)

    # Imprimir el resumen
    print_feeds_summary(feeds_info)
