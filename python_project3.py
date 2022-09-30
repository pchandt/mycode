from flask import Flask, jsonify
from flask import render_template
from datetime import date
from flask_navigation import Navigation


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


# grab the value 'username'
@app.route("/course")
def user():
    names = ["Java", "JavaScript", "Python", "HTML/CSS"]
    # render the jinja template "helloname.html"
    # apply the value of username for the var name
    return render_template("user.html", names=names)


@app.route("/date")
def getdate():
    return jsonify({"date": date.today()})


sde_apprenticeship = [{'course': 'java',
                       'duration': 'six weeks',
                       'projects': 1,
                       'labs': 40,
                       'instructor': [{'name': 'Nick',
                                       'email': 'nick@example.com'}]
                       },
                      {'course': 'javascript',
                       'duration': 'four weeks',
                       'projects': 1,
                       'labs': 10,
                       'instructor': [{'name': 'Nelly',
                                       'email': 'nelly@example.com'}]

                       },
                      {'course': 'python',
                       'duration': 'two weeks',
                       'projects': 3,
                       'labs': 100,
                       'instructor': [{'name': 'Jason',
                                       'email': 'jason@example.com'}]

                       },
                      {'course': 'data structure and alg',
                       'duration': 'one week',
                       'projects': 0,
                       'labs': 0,
                       'instructor': [{'name': 'sang',
                                       'email': 'sang@example.com'}]

                       }
                      ]


@app.route("/json")
def getjson():
    return jsonify(sde_apprenticeship)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
