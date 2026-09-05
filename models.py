# ============================================================================
# models.py — Define cómo se ve la tabla "usuarios" en la base de datos
# ============================================================================
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

# db es el objeto que usamos en todo el proyecto para hablar con la
# base de datos. Se conecta a la app de Flask en run.py.
db = SQLAlchemy()


class Alimentos_R(db.Model):
    __tablename__ = "Alimentos_Refrigerados"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alimento_especifico = db.Column(db.String(100), nullable=False)
    temperatura = db.Column(db.Double, nullable=False, unique=True)
    rango = db.Column(db.String(100), nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        """Convierte el objeto Usuario en un diccionario, para poder
        devolverlo como JSON en las respuestas de la API."""
        return {
            "id": self.id,
            "alimento_especifico": self.alimento_especifico,
            "temperatura": self.temperatura,
            "rango": self.rango,
            "fecha_creacion": self.fecha_creacion.isoformat() if self.fecha_creacion else None,
        }
