import os

from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def auto_exec():
    if request.method == "POST":
        if request.form.get('name'):
            print(request.form.get('name'))
            return render_template("exec_pkg_go_info.html")
        else:
            return render_template("exec_pkg_go_info.html")
    else:
        return render_template("exec_pkg_go_info.html")


@app.route("/reboot", methods=['GET', 'POST'])
def reboot():
    os.system("reboot")


if __name__ == "__main__":
    app.run(debug=True)
