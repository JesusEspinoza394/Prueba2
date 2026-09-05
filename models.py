# ============================================================================
# models.py — Define cómo se ven las tablas en la base de datos
# ============================================================================
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

# db es el objeto que usamos en todo el proyecto para hablar con la
# base de datos. Se conecta a la app de Flask en run.py.
db = SQLAlchemy()


class Usuario(db.Model):
    """Tabla de usuarios."""
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    edad = db.Column(db.Integer, nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        """Convierte el objeto Usuario en un diccionario, para poder
        devolverlo como JSON en las respuestas de la API."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "edad": self.edad,
            "fecha_creacion": self.fecha_creacion.isoformat() if self.fecha_creacion else None,
        }


class Alimentos_R(db.Model):
    """Tabla de alimentos refrigerados."""
    __tablename__ = "Alimentos_Refrigerados"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alimento_especifico = db.Column(db.String(100), nullable=False)
    temperatura = db.Column(db.Float, nullable=False, unique=True)
    rango = db.Column(db.String(100), nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        """Convierte el objeto Alimentos_R en un diccionario, para poder
        devolverlo como JSON en las respuestas de la API."""
        return {
            "id": self.id,
            "alimento_especifico": self.alimento_especifico,
            "temperatura": self.temperatura,
            "rango": self.rango,
            "fecha_creacion": self.fecha_creacion.isoformat() if self.fecha_creacion else None,
        }


class Alimentos_PR(db.Model):
    """Tabla de alimentos perecederos."""
    __tablename__ = "Alimentos_perecederos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alimento_especifico = db.Column(db.String(100), nullable=False)
    temperatura = db.Column(db.Float, nullable=False, unique=True)
    rango = db.Column(db.String(100), nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        """Convierte el objeto Alimentos_PR en un diccionario, para poder
        devolverlo como JSON en las respuestas de la API."""
        return {
            "id": self.id,
            "alimento_especifico": self.alimento_especifico,
            "temperatura": self.temperatura,
            "rango": self.rango,
            "fecha_creacion": self.fecha_creacion.isoformat() if self.fecha_creacion else None,
        }


class Alimentos_PC(db.Model):
    """Tabla de alimentos perecibles."""
    __tablename__ = "Alimentos perecibles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alimento_especifico = db.Column(db.String(100), nullable=False)
    temperatura = db.Column(db.Float, nullable=False, unique=True)
    rango = db.Column(db.String(100), nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        """Convierte el objeto Alimentos_PC en un diccionario, para poder
        devolverlo como JSON en las respuestas de la API."""
        return {
            "id": self.id,
            "alimento_especifico": self.alimento_especifico,
            "temperatura": self.temperatura,
            "rango": self.rango,
            "fecha_creacion": self.fecha_creacion.isoformat() if self.fecha_creacion else None,
        }
