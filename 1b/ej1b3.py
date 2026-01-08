"""
Enunciado:
Desarrolla un servidor web básico utilizando la biblioteca http.server de Python.
El servidor debe responder a peticiones GET y proporcionar información sobre la hora del sistema.

`GET /time`: Devuelve la hora actual del sistema en formato JSON.

Esta es una introducción a los servidores HTTP en Python para entender cómo:
1. Crear una aplicación web básica sin usar frameworks
2. Responder a diferentes rutas en una petición HTTP
3. Manejar errores HTTP y devolver respuestas personalizadas
4. Devolver respuestas en formato JSON

Tu tarea es completar la implementación de la clase MyHTTPRequestHandler, enfocándote en el manejo
de errores para rutas no definidas.

Nota: La implementación para obtener y devolver la hora del sistema ya está proporcionada.
Tu objetivo es asegurar que cuando se acceda a una ruta no definida, se devuelva un mensaje de
error 404 personalizado en formato JSON.
"""

import json
import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Manejador de peticiones HTTP personalizado
    """

    def do_GET(self):
        """
        Método que se ejecuta cuando se recibe una petición GET.

        Rutas implementadas:
        - `/time`: Devuelve la hora actual del sistema en formato JSON

        Para otras rutas, debes devolver un código de estado 404 (Not Found) con un mensaje
        personalizado en formato JSON.
        """
        if self.path == "/time":
            # Esta parte ya está implementada: devuelve la hora del sistema en JSON
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            current_time = datetime.datetime.now()
            time_info = {
                "timestamp": current_time.timestamp(),
                "iso_format": current_time.isoformat(),
                "readable": current_time.strftime("%Y-%m-%d %H:%M:%S")
            }

            self.wfile.write(json.dumps(time_info).encode())
        else:
            # Implementa aquí el manejo de errores para rutas no definidas
            # Debes:
            # 1. Enviar un código de estado 404
            # 2. Establecer el tipo de contenido como "application/json"
            # 3. Devolver un mensaje de error personalizado en formato JSON
            #    que incluya al menos el código de error y un mensaje descriptivo
            #
            # FORMATO DE RESPUESTA DE ERROR:
            #
            # {
            #    "code": 404,
            #    "message": "Recurso [ruta] no encontrado"
            # }
            #
            # Donde [ruta] debe ser sustituido por la ruta solicitada (self.path)
            # Ejemplo: Si se solicita "/api/users", el mensaje sería "Recurso /api/users no encontrado"
            #
            # Nota: Para los nombres de campo también se aceptan variaciones como:
            # - Para el código: "code" o "status"
            # - Para el mensaje: "message", "descripcion" o "detail"
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            error_info = {
                "code": 404,
                "message": f"Recurso {self.path} no encontrado"
            }
            self.wfile.write(json.dumps(error_info).encode())



def create_server(host="localhost", port=8000):
    """
    Crea y configura el servidor HTTP
    """
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    return httpd

def run_server(server):
    """
    Inicia el servidor HTTP
    """
    print(f"Servidor iniciado en http://{server.server_name}:{server.server_port}")
    server.serve_forever()

if __name__ == '__main__':
    server = create_server()
    run_server(server)
