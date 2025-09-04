from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

usuarios = {
    "admin@mail.com": {"password": "1234", "role": "admin"},
    "cliente@mail.com": {"password": "1234", "role": "cliente"},
    "emprendedor@mail.com": {"password": "1234", "role": "emprendedor"}
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    role = request.form.get("role")

    user = usuarios.get(email)
    if user and user["password"] == password and user["role"] == role:
        return jsonify({"success": True, "role": role})
    return jsonify({"success": False})

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/cliente")
def cliente():
    return render_template("cliente.html")

@app.route("/emprendedor")
def emprendedor():
    return render_template("emprendedor.html")

if __name__ == "__main__":
    app.run(debug=True)


from models.producto import Producto
from models.pedido import Pedido

# Productos disponibles (en memoria)
productos_disponibles = [
    Producto("Camiseta", 20, "camiseta.jpg"),
    Producto("Camiseta Premium", 35, "camisetapremium.jpg"),
    Producto("Labial", 10, "labial.jpg"),
    Producto("Serum", 25, "serum.jpg"),
    Producto("Taza", 12, "taza.jpg"),
    Producto("Zapatos", 50, "zapatos.jpg"),
]

# Lista de pedidos del cliente (en memoria)
pedidos_cliente = []
pedido_actual = Pedido()

@app.route("/cliente")
def cliente():
    return render_template("cliente.html", productos=productos_disponibles)

@app.route("/agregar/<nombre>")
def agregar_producto(nombre):
    global pedido_actual
    for p in productos_disponibles:
        if p.get_nombre() == nombre:
            pedido_actual.add_item(p)
            break
    return redirect("/cliente")

@app.route("/mis_pedidos")
def mis_pedidos():
    global pedido_actual, pedidos_cliente
    if pedido_actual.get_items():
        pedidos_cliente.append(pedido_actual)
        pedido_actual = Pedido()
    return render_template("mis_pedidos.html", pedidos=pedidos_cliente)
