from flask import Flask, render_template, request, redirect, url_for

app = Flask("BaseBura")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Tipo_de_cuenta")
def cuentas():
    return render_template("cuentas.html")

@app.route("/Administrador")
def admin():
    return render_template("admin.html")

@app.route("/f", methods=["GET", "POST"])
def admino():
    if request.method == "POST":
        email = request.form.get("email")
        contraseña = request.form.get("contraseña")
        print(email)
        print(contraseña)
        #procesar datos de entrada
        return redirect(url_for("admincuentas", email= email))
    return render_template("admin.html")

@app.route("/Menú_Administrador")
def admincuentas():
    #obtener el parametro opcional
    email = request.args.get("email", "contraseña")
    return render_template("admincuentas.html", email=email)

@app.route("/Crear_cuentas")
def ccuentas():
    return render_template("ccuentas.html")

@app.route("/cc", methods=["GET", "POST"])
def cuentano():
    if request.method == "POST":
        email = request.form.get("email")
        #procesar datos de entrada
        return redirect(url_for("cuentac", email= email))
    return render_template("ccuentas.html")

@app.route("/Cuenta_creada")
def cuentac():
    #obtener el parametro opcional
    email = request.args.get("email", "contraseña")
    return render_template("cuenta_c.html", email=email)

@app.route("/Representante")
def representante():
    return render_template("representante.html")

@app.route("/r", methods=["GET", "POST"])
def repro():
    if request.method == "POST":
        email = request.form.get("email")
        contraseña = request.form.get("contraseña")
        print(email)
        print(contraseña)
        #procesar datos de entrada
        return redirect(url_for("srepre", email= email))
    return render_template("representante.html")

@app.route("/Menú_Representante")
def srepre():
    #obtener el parametro opcional
    email = request.args.get("email", "contraseña")
    return render_template("srepre.html", email=email)

@app.route("/Solicitar_Servicio")
def solicitars():
    return render_template("sservicio.html")

@app.route("/ss", methods=["GET", "POST"])
def solicitor():
    if request.method == "POST":
        email = request.form.get("email")
        tianguis = request.form.get("tianguis")
        print(email)
        print(tianguis)
        #procesar datos de entrada
        return redirect(url_for("servicios", email= email, tianguis=tianguis))
    return render_template("sservicio.html")

@app.route("/Servicio_Solicitado")
def servicios():
    #obtener el parametro opcional
    email = request.args.get("email")
    tianguis = request.args.get("tianguis")
    if tianguis == "Tianguis 1":
        return render_template("servicios1.html", email=email, tianguis=tianguis)
    if tianguis == "Tianguis 2":
        return render_template("servicios2.html", email=email, tianguis=tianguis)
    if tianguis == "Tianguis 3":
        return render_template("servicios3.html", email=email, tianguis=tianguis)
    if tianguis == "Tianguis 4":
        return render_template("servicios4.html", email=email, tianguis=tianguis)
    if tianguis == "Tianguis 5":
        return render_template("servicios5.html", email=email, tianguis=tianguis)
    if tianguis == "Tianguis 6":
        return render_template("servicios6.html", email=email, tianguis=tianguis)
    if tianguis == "Tianguis 7":
        return render_template("servicios7.html", email=email, tianguis=tianguis)

@app.route("/Advertencia")
def advertencia():
    return render_template("advertencia.html")

@app.route("/Contactos")
def contactos():
    return render_template("contactosre.html")

@app.route("/Comunicarse")
def comunicarse():
    return render_template("contactostr.html")

@app.route("/Reporte")
def datos():
    return render_template("datos.html")

@app.route("/Editar_cuentas")
def edita():
    return render_template("edita.html")

@app.route("/Cuenta_eliminada")
def eliminada():
    return render_template("eliminada.html")

@app.route("/Eliminar_cuentas")
def eliminar():
    return render_template("eliminar.html")

@app.route("/Estatus_recolección")
def estatusreco():
    return render_template("Estatusrecoleccion.html")

@app.route("/Estatus_representante")
def estatusrepre():
    return render_template("Estatusrepre.html")

@app.route("/Ubicaciones")
def mapa():
    return render_template("MAPAINTEGRADO.html")

@app.route("/Datos_de_modificación")
def datosmodi():
    return render_template("nuevaeditar.html")

@app.route("/Cuenta_Editada")
def cuentae():
    return render_template("cuentae.html")

@app.route("/Trabajador")
def trabajador():
    return render_template("trabajador.html")

@app.route("/t", methods=["GET", "POST"])
def trabo():
    if request.method == "POST":
        email = request.form.get("email")
        contraseña = request.form.get("contraseña")
        print(email)
        print(contraseña)
        #procesar datos de entrada
        return redirect(url_for("mtrabajador", email= email))
    return render_template("trabajador.html")

@app.route("/Menú_Trabajador")
def mtrabajador():
    #obtener el parametro opcional
    email = request.args.get("email", "contraseña")
    return render_template("mtrabajador.html", email=email)

@app.route("/Datos_de_Recolección")
def datosreco():
    return render_template("datosreco.html")

@app.route("/dr", methods=["GET", "POST"])
def datosrece():
    if request.method == "POST":
        cantidad = request.form.get("cantidad")
        tiempo = request.form.get("tiempo")
        trabajadores = request.form.get("trabajadores")
        print(trabajadores)
        print(cantidad)
        print(tiempo)
        #procesar datos de entrada
        return redirect(url_for("datosc"))
    return render_template("trabajador.html")

@app.route("/Datos_Registrados")
def datosc():
    #obtener el parametro opcional
    return render_template("datosc.html")

if __name__ == "__main__":
    app.run(debug=True)