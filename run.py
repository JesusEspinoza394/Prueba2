# ============================================================================
# run.py — Punto de entrada: aquí se arma la aplicación y se arranca
# ============================================================================
from flask import Flask, jsonify

from config import Config
from models import db
from routes import (
    usuarios_bp,
    alimentos_bp,
    alimentos_verduras_bp,
    alimentos_congelados_bp,
)

# 1. Crear la aplicación Flask
app = Flask(__name__)

# 2. Cargarle la configuración (conexión a Neon, etc.)
app.config.from_object(Config)

# 3. Conectar SQLAlchemy (models.py) con esta app
db.init_app(app)

# 4. Registrar las rutas de usuarios (routes.py) en la app
app.register_blueprint(usuarios_bp)

# 5. Registrar las rutas de alimentos refrigerados (routes.py) en la app
app.register_blueprint(alimentos_bp)

# 6. Registrar las rutas de alimentos verduras (antes: alimentos_pr)
app.register_blueprint(alimentos_verduras_bp)

# 7. Registrar las rutas de alimentos congelados (antes: alimentos_pc)
app.register_blueprint(alimentos_congelados_bp)

# 8. Crear las tablas en la base de datos si no existen todavía
with app.app_context():
    db.create_all()


@app.route("/", methods=["GET"])
def inicio():
    """Ruta raíz: muestra qué endpoints existen."""
    return jsonify({
        "mensaje": "API CRUD de Usuarios y Alimentos (Flask + PostgreSQL/Neon)",
        "endpoints": {
            "USUARIOS": {
                "GET /usuarios": "Lista todos los usuarios",
                "GET /usuarios/<id>": "Obtiene un usuario por su id",
                "POST /usuarios": "Crea un nuevo usuario",
                "PUT /usuarios/<id>": "Actualiza un usuario existente",
                "DELETE /usuarios/<id>": "Elimina un usuario",
            },
            "ALIMENTOS_REFRIGERADOS": {
                "GET /alimentos": "Lista todos los alimentos refrigerados",
                "GET /alimentos/<id>": "Obtiene un alimento por su id",
                "POST /alimentos": "Crea un nuevo alimento",
                "PUT /alimentos/<id>": "Actualiza un alimento existente",
                "DELETE /alimentos/<id>": "Elimina un alimento",
            },
            "ALIMENTOS_VERDURAS": {
                "GET /alimentos_verduras": "Lista todos los alimentos verduras",
                "GET /alimentos_verduras/<id>": "Obtiene un alimento por su id",
                "POST /alimentos_verduras": "Crea un nuevo alimento",
                "PUT /alimentos_verduras/<id>": "Actualiza un alimento existente",
                "DELETE /alimentos_verduras/<id>": "Elimina un alimento",
            },
            "ALIMENTOS_CONGELADOS": {
                "GET /alimentos_congelados": "Lista todos los alimentos congelados",
                "GET /alimentos_congelados/<id>": "Obtiene un alimento por su id",
                "POST /alimentos_congelados": "Crea un nuevo alimento",
                "PUT /alimentos_congelados/<id>": "Actualiza un alimento existente",
                "DELETE /alimentos_congelados/<id>": "Elimina un alimento",
            },
        },
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
