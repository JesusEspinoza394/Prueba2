# ============================================================================
# routes.py — Los endpoints de la API: qué pasa cuando llega cada petición
# ============================================================================
from flask import Blueprint, request, jsonify
from models import db, Usuario, Alimentos_R, Alimentos_Verduras, Alimentos_Congelados

# Un Blueprint agrupa un conjunto de rutas relacionadas (aquí, todas las
# de usuarios) para luego "engancharlas" a la app principal en run.py.
usuarios_bp = Blueprint("usuarios", __name__)

# Blueprint para Alimentos_R
alimentos_bp = Blueprint("alimentos", __name__)

# Blueprint para Alimentos_Verduras (antes: alimentos_pr)
alimentos_verduras_bp = Blueprint("alimentos_verduras", __name__)

# Blueprint para Alimentos_Congelados (antes: alimentos_pc)
alimentos_congelados_bp = Blueprint("alimentos_congelados", __name__)


# ============================================================================
# ENDPOINTS DE USUARIOS
# ============================================================================

@usuarios_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    """GET /usuarios → devuelve todos los usuarios."""
    usuarios = Usuario.query.all()
    return jsonify([u.to_dict() for u in usuarios])


@usuarios_bp.route("/usuarios/<int:usuario_id>", methods=["GET"])
def buscar_usuario(usuario_id):
    """GET /usuarios/5 → busca y devuelve un solo usuario por id."""
    usuario = db.session.get(Usuario, usuario_id)
    if usuario is None:
        return jsonify({"error": "Usuario no encontrado."}), 404
    return jsonify(usuario.to_dict())


@usuarios_bp.route("/usuarios", methods=["POST"])
def agregar_usuario():
    """POST /usuarios → agrega un usuario nuevo."""
    datos = request.get_json()

    nuevo_usuario = Usuario(
        nombre=datos["nombre"],
        email=datos["email"],
        edad=datos.get("edad"),
    )

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify(nuevo_usuario.to_dict()), 201


@usuarios_bp.route("/usuarios/<int:usuario_id>", methods=["PUT"])
def editar_usuario(usuario_id):
    """PUT /usuarios/5 → edita los datos de un usuario existente."""
    usuario = db.session.get(Usuario, usuario_id)
    if usuario is None:
        return jsonify({"error": "Usuario no encontrado."}), 404

    datos = request.get_json()

    usuario.nombre = datos.get("nombre", usuario.nombre)
    usuario.email = datos.get("email", usuario.email)
    usuario.edad = datos.get("edad", usuario.edad)

    db.session.commit()

    return jsonify(usuario.to_dict())


@usuarios_bp.route("/usuarios/<int:usuario_id>", methods=["DELETE"])
def eliminar_usuario(usuario_id):
    """DELETE /usuarios/5 → elimina un usuario."""
    usuario = db.session.get(Usuario, usuario_id)
    if usuario is None:
        return jsonify({"error": "Usuario no encontrado."}), 404

    db.session.delete(usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario eliminado correctamente."})


# ============================================================================
# ENDPOINTS DE ALIMENTOS_R
# ============================================================================

@alimentos_bp.route("/alimentos", methods=["GET"])
def listar_alimentos():
    """GET /alimentos → devuelve todos los alimentos refrigerados."""
    alimentos = Alimentos_R.query.all()
    return jsonify([a.to_dict() for a in alimentos])


@alimentos_bp.route("/alimentos/<int:alimento_id>", methods=["GET"])
def buscar_alimento(alimento_id):
    """GET /alimentos/5 → busca y devuelve un solo alimento por id."""
    alimento = db.session.get(Alimentos_R, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404
    return jsonify(alimento.to_dict())


@alimentos_bp.route("/alimentos", methods=["POST"])
def agregar_alimento():
    """POST /alimentos → agrega un alimento nuevo."""
    datos = request.get_json()

    nuevo_alimento = Alimentos_R(
        alimento_especifico=datos["alimento_especifico"],
        temperatura=datos["temperatura"],
        rango=datos.get("rango"),
    )

    db.session.add(nuevo_alimento)
    db.session.commit()

    return jsonify(nuevo_alimento.to_dict()), 201


@alimentos_bp.route("/alimentos/<int:alimento_id>", methods=["PUT"])
def editar_alimento(alimento_id):
    """PUT /alimentos/5 → edita los datos de un alimento existente."""
    alimento = db.session.get(Alimentos_R, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404

    datos = request.get_json()

    alimento.alimento_especifico = datos.get("alimento_especifico", alimento.alimento_especifico)
    alimento.temperatura = datos.get("temperatura", alimento.temperatura)
    alimento.rango = datos.get("rango", alimento.rango)

    db.session.commit()

    return jsonify(alimento.to_dict())


@alimentos_bp.route("/alimentos/<int:alimento_id>", methods=["DELETE"])
def eliminar_alimento(alimento_id):
    """DELETE /alimentos/5 → elimina un alimento."""
    alimento = db.session.get(Alimentos_R, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404

    db.session.delete(alimento)
    db.session.commit()

    return jsonify({"mensaje": "Alimento eliminado correctamente."})


# ============================================================================
# ENDPOINTS DE ALIMENTOS_VERDURAS (antes: alimentos_pr / perecederos)
# ============================================================================

@alimentos_verduras_bp.route("/alimentos_verduras", methods=["GET"])
def listar_alimentos_verduras():
    """GET /alimentos_verduras → devuelve todos los alimentos verduras."""
    alimentos = Alimentos_Verduras.query.all()
    return jsonify([a.to_dict() for a in alimentos])


@alimentos_verduras_bp.route("/alimentos_verduras/<int:alimento_id>", methods=["GET"])
def buscar_alimento_verduras(alimento_id):
    """GET /alimentos_verduras/5 → busca y devuelve un alimento verduras por id."""
    alimento = db.session.get(Alimentos_Verduras, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404
    return jsonify(alimento.to_dict())


@alimentos_verduras_bp.route("/alimentos_verduras", methods=["POST"])
def agregar_alimento_verduras():
    """POST /alimentos_verduras → agrega un alimento verduras nuevo."""
    datos = request.get_json()

    nuevo_alimento = Alimentos_Verduras(
        alimento_especifico=datos["alimento_especifico"],
        temperatura=datos["temperatura"],
        rango=datos.get("rango"),
    )

    db.session.add(nuevo_alimento)
    db.session.commit()

    return jsonify(nuevo_alimento.to_dict()), 201


@alimentos_verduras_bp.route("/alimentos_verduras/<int:alimento_id>", methods=["PUT"])
def editar_alimento_verduras(alimento_id):
    """PUT /alimentos_verduras/5 → edita un alimento verduras existente."""
    alimento = db.session.get(Alimentos_Verduras, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404

    datos = request.get_json()

    alimento.alimento_especifico = datos.get("alimento_especifico", alimento.alimento_especifico)
    alimento.temperatura = datos.get("temperatura", alimento.temperatura)
    alimento.rango = datos.get("rango", alimento.rango)

    db.session.commit()

    return jsonify(alimento.to_dict())


@alimentos_verduras_bp.route("/alimentos_verduras/<int:alimento_id>", methods=["DELETE"])
def eliminar_alimento_verduras(alimento_id):
    """DELETE /alimentos_verduras/5 → elimina un alimento verduras."""
    alimento = db.session.get(Alimentos_Verduras, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404

    db.session.delete(alimento)
    db.session.commit()

    return jsonify({"mensaje": "Alimento eliminado correctamente."})


# ============================================================================
# ENDPOINTS DE ALIMENTOS_CONGELADOS (antes: alimentos_pc / perecibles)
# ============================================================================

@alimentos_congelados_bp.route("/alimentos_congelados", methods=["GET"])
def listar_alimentos_congelados():
    """GET /alimentos_congelados → devuelve todos los alimentos congelados."""
    alimentos = Alimentos_Congelados.query.all()
    return jsonify([a.to_dict() for a in alimentos])


@alimentos_congelados_bp.route("/alimentos_congelados/<int:alimento_id>", methods=["GET"])
def buscar_alimento_congelados(alimento_id):
    """GET /alimentos_congelados/5 → busca y devuelve un alimento congelado por id."""
    alimento = db.session.get(Alimentos_Congelados, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404
    return jsonify(alimento.to_dict())


@alimentos_congelados_bp.route("/alimentos_congelados", methods=["POST"])
def agregar_alimento_congelados():
    """POST /alimentos_congelados → agrega un alimento congelado nuevo."""
    datos = request.get_json()

    nuevo_alimento = Alimentos_Congelados(
        alimento_especifico=datos["alimento_especifico"],
        temperatura=datos["temperatura"],
        rango=datos.get("rango"),
    )

    db.session.add(nuevo_alimento)
    db.session.commit()

    return jsonify(nuevo_alimento.to_dict()), 201


@alimentos_congelados_bp.route("/alimentos_congelados/<int:alimento_id>", methods=["PUT"])
def editar_alimento_congelados(alimento_id):
    """PUT /alimentos_congelados/5 → edita un alimento congelado existente."""
    alimento = db.session.get(Alimentos_Congelados, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404

    datos = request.get_json()

    alimento.alimento_especifico = datos.get("alimento_especifico", alimento.alimento_especifico)
    alimento.temperatura = datos.get("temperatura", alimento.temperatura)
    alimento.rango = datos.get("rango", alimento.rango)

    db.session.commit()

    return jsonify(alimento.to_dict())


@alimentos_congelados_bp.route("/alimentos_congelados/<int:alimento_id>", methods=["DELETE"])
def eliminar_alimento_congelados(alimento_id):
    """DELETE /alimentos_congelados/5 → elimina un alimento congelado."""
    alimento = db.session.get(Alimentos_Congelados, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404

    db.session.delete(alimento)
    db.session.commit()

    return jsonify({"mensaje": "Alimento eliminado correctamente."})
