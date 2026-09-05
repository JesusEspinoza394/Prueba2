# ============================================================================
# routes.py — Los endpoints de la API: qué pasa cuando llega cada petición
# ============================================================================
from flask import Blueprint, request, jsonify
from models import db, Usuario, Alimentos_R, Alimentos_PR, Alimentos_PC

# Un Blueprint agrupa un conjunto de rutas relacionadas (aquí, todas las
# de usuarios) para luego "engancharlas" a la app principal en run.py.
usuarios_bp = Blueprint("usuarios", __name__)

# Blueprint para Alimentos_R
alimentos_bp = Blueprint("alimentos", __name__)

# Blueprint para Alimentos_PR
alimentos_pr_bp = Blueprint("alimentos_pr", __name__)

# Blueprint para Alimentos_PC
alimentos_pc_bp = Blueprint("alimentos_pc", __name__)


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
# ENDPOINTS DE ALIMENTOS_PR (perecederos)
# ============================================================================

@alimentos_pr_bp.route("/alimentos_pr", methods=["GET"])
def listar_alimentos_pr():
    """GET /alimentos_pr → devuelve todos los alimentos perecederos."""
    alimentos = Alimentos_PR.query.all()
    return jsonify([a.to_dict() for a in alimentos])


@alimentos_pr_bp.route("/alimentos_pr/<int:alimento_id>", methods=["GET"])
def buscar_alimento_pr(alimento_id):
    """GET /alimentos_pr/5 → busca y devuelve un alimento perecedero por id."""
    alimento = db.session.get(Alimentos_PR, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404
    return jsonify(alimento.to_dict())


@alimentos_pr_bp.route("/alimentos_pr", methods=["POST"])
def agregar_alimento_pr():
    """POST /alimentos_pr → agrega un alimento perecedero nuevo."""
    datos = request.get_json()

    nuevo_alimento = Alimentos_PR(
        alimento_especifico=datos["alimento_especifico"],
        temperatura=datos["temperatura"],
        rango=datos.get("rango"),
    )

    db.session.add(nuevo_alimento)
    db.session.commit()

    return jsonify(nuevo_alimento.to_dict()), 201


@alimentos_pr_bp.route("/alimentos_pr/<int:alimento_id>", methods=["PUT"])
def editar_alimento_pr(alimento_id):
    """PUT /alimentos_pr/5 → edita un alimento perecedero existente."""
    alimento = db.session.get(Alimentos_PR, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404

    datos = request.get_json()

    alimento.alimento_especifico = datos.get("alimento_especifico", alimento.alimento_especifico)
    alimento.temperatura = datos.get("temperatura", alimento.temperatura)
    alimento.rango = datos.get("rango", alimento.rango)

    db.session.commit()

    return jsonify(alimento.to_dict())


@alimentos_pr_bp.route("/alimentos_pr/<int:alimento_id>", methods=["DELETE"])
def eliminar_alimento_pr(alimento_id):
    """DELETE /alimentos_pr/5 → elimina un alimento perecedero."""
    alimento = db.session.get(Alimentos_PR, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404

    db.session.delete(alimento)
    db.session.commit()

    return jsonify({"mensaje": "Alimento eliminado correctamente."})


# ============================================================================
# ENDPOINTS DE ALIMENTOS_PC (perecibles)
# ============================================================================

@alimentos_pc_bp.route("/alimentos_pc", methods=["GET"])
def listar_alimentos_pc():
    """GET /alimentos_pc → devuelve todos los alimentos perecibles."""
    alimentos = Alimentos_PC.query.all()
    return jsonify([a.to_dict() for a in alimentos])


@alimentos_pc_bp.route("/alimentos_pc/<int:alimento_id>", methods=["GET"])
def buscar_alimento_pc(alimento_id):
    """GET /alimentos_pc/5 → busca y devuelve un alimento perecible por id."""
    alimento = db.session.get(Alimentos_PC, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404
    return jsonify(alimento.to_dict())


@alimentos_pc_bp.route("/alimentos_pc", methods=["POST"])
def agregar_alimento_pc():
    """POST /alimentos_pc → agrega un alimento perecible nuevo."""
    datos = request.get_json()

    nuevo_alimento = Alimentos_PC(
        alimento_especifico=datos["alimento_especifico"],
        temperatura=datos["temperatura"],
        rango=datos.get("rango"),
    )

    db.session.add(nuevo_alimento)
    db.session.commit()

    return jsonify(nuevo_alimento.to_dict()), 201


@alimentos_pc_bp.route("/alimentos_pc/<int:alimento_id>", methods=["PUT"])
def editar_alimento_pc(alimento_id):
    """PUT /alimentos_pc/5 → edita un alimento perecible existente."""
    alimento = db.session.get(Alimentos_PC, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404

    datos = request.get_json()

    alimento.alimento_especifico = datos.get("alimento_especifico", alimento.alimento_especifico)
    alimento.temperatura = datos.get("temperatura", alimento.temperatura)
    alimento.rango = datos.get("rango", alimento.rango)

    db.session.commit()

    return jsonify(alimento.to_dict())


@alimentos_pc_bp.route("/alimentos_pc/<int:alimento_id>", methods=["DELETE"])
def eliminar_alimento_pc(alimento_id):
    """DELETE /alimentos_pc/5 → elimina un alimento perecible."""
    alimento = db.session.get(Alimentos_PC, alimento_id)
    if alimento is None:
        return jsonify({"error": "Alimento no encontrado."}), 404

    db.session.delete(alimento)
    db.session.commit()

    return jsonify({"mensaje": "Alimento eliminado correctamente."})
