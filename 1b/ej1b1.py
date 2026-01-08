"""
Enunciado:
Introducción al manejo de errores HTTP con la biblioteca requests de Python.
La biblioteca requests permite realizar peticiones HTTP de forma sencilla, pero es
importante saber manejar los errores que puedan ocurrir.

En este ejercicio, aprenderás a:
1. Realizar una petición GET a un recurso inexistente
2. Capturar y manejar errores HTTP como 404 (Not Found)
3. Extraer información útil de las respuestas de error

Tu tarea es completar la función indicada para realizar una consulta a una URL inexistente
en api.ipify.org y manejar el error de forma adecuada.
"""

import requests

def get_nonexistent_resource():
    """
    Realiza una petición GET a un recurso inexistente en api.ipify.org y maneja el error.

    La función debe:
    1. Intentar realizar una petición a https://api.ipify.org/ip (recurso que no existe)
    2. Capturar el error HTTP 404
    3. Extraer información útil del error

    Returns:
        dict: Un diccionario con la siguiente información:
            - status_code: El código de estado HTTP (ej. 404)
            - error_message: El mensaje de error (si está disponible)
            - requested_url: La URL a la que se intentó acceder
    """
    url = "https://api.ipify.org/ip"  # URL incorrecta a propósito para generar un 404

    # Completa esta función para:
    # 1. Realizar la petición GET a la URL proporcionada
    # 2. Capturar la excepción o error HTTP (no interrumpir la ejecución)
    # 3. Extraer la información solicitada del error
    # 4. Devolver un diccionario con la información del error
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return {
                'status_code': response.status_code,
                'error_message': f"{response.status_code} Error: {response.reason}",
                'requested_url': url
            }
        response.raise_for_status()
        return {
            'status_code': response.status_code,
            'error_message': None,
            'requested_url': url
        }
    except requests.HTTPError as e:
        return {
            'status_code': 404,
            'error_message': str(e),
            'requested_url': url
        }
    except requests.RequestException as e:
        return {
            'status_code': getattr(e.response, 'status_code', None),
            'error_message': str(e),
            'requested_url': url
        }
    except Exception as e:
        return {
            'status_code': None,
            'error_message': str(e),
            'requested_url': url
        }


if __name__ == "__main__":
    # Ejemplo de uso de la función
    error_info = get_nonexistent_resource()
    if error_info:
        print(f"Error {error_info['status_code']} al acceder a {error_info['requested_url']}")
        print(f"Mensaje: {error_info.get('error_message', 'No disponible')}")
    else:
        print("No se pudo procesar la respuesta")
