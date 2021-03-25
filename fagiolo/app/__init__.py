import enum
from typing import cast

from flask import Flask

app = Flask(__name__)


@app.template_filter("beautify_enum")
def beautify_enum(enum_member: enum.Enum) -> str:
    return cast(str, enum_member.value.lower().replace("_", " "))


from fagiolo.app import views  # noqa E402
