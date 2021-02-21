from flask import Flask

app = Flask(__name__)


@app.template_filter("beautify_underscores")
def beautify_underscores(string):
    return string.lower().replace("_", " ")


from pantry.app import routes  # noqa E402
