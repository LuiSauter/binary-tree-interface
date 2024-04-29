from flask import Flask, render_template, request
from tree import Tree
from nodo import Nodo

app = Flask(__name__)

tree = Tree()

def generate_html_tree(root):
    """Genera un árbol binario en formato SVG"""
    html = ""
    html = draw_tree(root, html, 500, 50, 200, 50)
    return f"<div>\n<svg width=\"1000\" height=\"1000\">\n{html}</svg>\n</div>\n"

def draw_tree(node: Nodo, html, x, y, dx, dy):
    if node:
        if node.left: # Dibujar rama izquierda
            html += f"<line x1=\"{x}\" y1=\"{y}\" x2=\"{x-dx}\" y2=\"{y+dy}\" stroke=\"black\" />\n"
            # Llamada recursiva para dibujar el subárbol izquierdo
            html = draw_tree(node.left, html, x-dx, y+dy, dx/2, dy)
        if node.right: # Dibujar rama derecha
            html += f"<line x1=\"{x}\" y1=\"{y}\" x2=\"{x+dx}\" y2=\"{y+dy}\" stroke=\"black\" />\n"
            # Llamada recursiva para dibujar el subárbol derecho
            html = draw_tree(node.right, html, x+dx, y+dy, dx/2, dy)
        # Dibujar nodo actual
        html += f"<circle cx=\"{x}\" cy=\"{y}\" r=\"20\" fill=\"lightblue\" />\n"
        html += f"<text x=\"{x}\" y=\"{y}\" text-anchor=\"middle\" dominant-baseline=\"middle\" fill=\"black\">{node.element}</text>\n"
    return html

@app.route("/", methods=["GET"])
def index():
    tree.__raiz__ = None
    return render_template(
        "index.html", tree=generate_html_tree(tree.__raiz__), order=""
    )

@app.post("/action")
def action():
    searchValue = ""
    print(request.form)
    element = request.form["value"]
    if request.form["method"] == "interative":
        if request.form["action"] == "delete":
            tree.delete_iterative(int(element))
        if request.form["action"] == "insert":
          tree.insert_iterative(int(element))
        if request.form["action"] == "search":
            findNodo = tree.search_iterative(int(element))
            searchValue = findNodo.element if findNodo else ""
    else:
        if request.form["action"] == "delete":
            tree.delete_recursive(int(element))
        if request.form["action"] == "insert":
            tree.insert_recursive(int(element))
        if request.form["action"] == "search":
            findNodo = tree.search_recursive(int(element))
            searchValue = findNodo.element if findNodo else ""
    html = ""
    html = generate_html_tree(tree.__raiz__)
    return {"tree": html, "searchValue": searchValue}

@app.post("/balance")
def balance():
    html = ""
    if tree.empty():
        return {"tree": html}
    tree.balance_recursive()
    html = generate_html_tree(tree.__raiz__)
    return {"tree": html}

@app.post("/methods")
def methods():
    order_result = ""
    if tree.empty():
        return {"order": ""}
    if request.form["action"] == "preorder":
        order_result = tree.pre_order_iterative()
    if request.form["action"] == "inorder":
        order_result = tree.in_order_iterative()
    if request.form["action"] == "postorder":
        order_result = tree.post_order_iterative()
    return {"order": order_result}

@app.post("/reset")
def reset():
    tree.__raiz__ = None
    html = generate_html_tree(tree.__raiz__)
    return {"tree": html}

@app.post("/test")
def test():
    # return a json
    html = ""
    html = draw_tree(tree.__raiz__, html, 500, 50, 200, 50)
    return {"nodo": html}