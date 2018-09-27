from flask import Flask, request
from jinja2 import Environment, FileSystemLoader


app = Flask(__name__)
environment = Environment(loader=FileSystemLoader("./"))


@app.route("/")
def greet():
    name = request.args['name']
    template = environment.get_template("index.html")
    return template.render(name=name)


def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
