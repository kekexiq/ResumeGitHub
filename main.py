from flask import Flask, render_template


app = Flask(__name__) #tuodaan flask-kirjasto, joka auttaa tekemään web-sivun

@app.route("/")
def index(): #kertoo, mitä nettisivuja haetaan ja millä osoitteella. Jossei ole mtn hakemistoa tms niin haetaan template cv.html
    return render_template("cv.html")

@app.route("/yhteystiedot")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)