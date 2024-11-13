import os
import re

from py4web import HTTP, action, request

MODE = os.environ.get("PY4WEB_DASHBOARD_MODE", "none")

from .examples.component_loader import component_loader
from .examples.count import count
from .examples.example_helpers import example_helpers
from .examples.flash_example_fixture import flash_example_fixture
from .examples.flash_example_naive import flash_example_naive
from .examples.hcaptcha_form import hcaptcha_form
from .examples.hello import hello
from .examples.page_with_error import page_with_error
from .examples.page_with_parameters import page_with_parameters
from .examples.page_with_postback import page_with_postback
from .examples.page_with_query import page_with_query
from .examples.page_with_raise import page_with_raise
from .examples.page_with_redirect import page_with_redirect, target
from .examples.page_with_template import page_with_template
from .examples.page_without_template import page_without_template
from .examples.rest import rest
from .examples.rpc import rpc
from .examples.session_clear import session_clear
from .examples.session_counter import session_counter
from .examples.tagsinput_form import tagsinput_form
from .vue_components_examples.vue_file_uploader import vue_file_uploader
from .vue_components_examples.vue_grid import vue_grid
from .vue_components_examples.vue_star_rater import vue_star_rater

if MODE == "full":
    from .vue_components_examples.models import db
    from .examples.auth_form import auth_form
    from .examples.auth_forms import auth_forms
    from .examples.create_form import create_form
    from .examples.custom_form import custom_form
    from .examples.example_ajax_grid import example_ajax_grid
    from .examples.example_html_grid import example_html_grid
    from .examples.example_multiple_forms import example_multiple_forms
    from .examples.hello_world import hello_world
    from .examples.hello_world_msg import hello_world_msg
    from .examples.show_a_button import show_a_button
    from .examples.socketio import index as socketio
    from .examples.test_expose import test_expose1, test_expose2, test_expose3
    from .examples.update_form import update_form
    from .examples.ws import index as ws
    from .vue_components_examples.vue_edit_form import vue_edit_form
    from .vue_components_examples.vue_grid_and_forms import vue_grid_and_forms
    from .vue_components_examples.vue_insert_form import vue_insert_form
    from .vue_components_examples.vue_view_form import vue_view_form


@action("index")
@action.uses("index.html")
def index():
    return {"mode": MODE}


@action("show/<name:path>")
@action.uses("show.html")
def show(name):
    path = name
    name = name.rstrip("/0123456789")
    data = []
    here = os.path.dirname(__file__)
    filename = f"{here}/{name}.md"
    if os.path.exists(filename):
        with open(filename) as stream:
            metadata = stream.read().strip()
        data.append({"name": f"{name}.md", "content": metadata, "language": "markdown"})
    filename = f"{here}/{name}.py"
    if not os.path.exists(filename):
        raise HTTP(404)
    with open(filename) as stream:
        controller = stream.read().strip()
    data.append({"name": f"{name}.py", "content": controller, "language": "python"})
    templates = re.compile(r"[/\w]+\.html").findall(controller)
    for template in templates:
        with open(f"{here}/templates/{template}") as stream:
            content = stream.read().strip()
            data.append(
                {
                    "name": f"templates/{template}",
                    "content": content,
                    "language": "html",
                }
            )
    others = re.compile(r"from [.](\S+)").findall(controller)
    for other in others:
        if not other.startswith("."):
            continue
        filename = other[1:].replace(".", "/") + ".py"
        with open(f"{here}/{filename}") as stream:
            content = stream.read().strip()
            data.append({"shortname": filename, "content": content, "language": "python"})
    # drop the subfolder name
    path = "/".join(path.split("/")[1:])
    executable = MODE == "full" or name.split("/")[-1] in globals()
    return {"files": data, "mode": MODE, "path": path, "executable": executable}
