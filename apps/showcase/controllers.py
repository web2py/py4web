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
from .examples.session_clear import session_clear
from .examples.session_counter import session_counter
from .examples.tagsinput_form import tagsinput_form
from .examples.vue_file_uploader import vue_file_uploader
from .examples.vue_grid import vue_grid
from .examples.vue_grid_bulma import vue_grid_bulma
from .examples.vue_star_rater import vue_star_rater
from .examples.vue_star_rater_bulma import vue_star_rater_bulma

if MODE == "full":
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
    from .examples.vue_form import vue_form
    from .examples.vue_form_bulma import vue_form_bulma
    from .examples.vue_insert_form import vue_insert_form
    from .examples.vue_insert_form_bulma import vue_insert_form_bulma
    from .examples.vue_update_form import vue_update_form
    from .examples.vue_update_form_bulma import vue_update_form_bulma
    from .examples.ws import index as ws


@action("index")
@action.uses("index.html")
def index():
    return {"mode": MODE}


@action("show/<name>")
@action.uses("show.html")
def show(name):
    data = []
    filename = f"apps/showcase/examples/{name}.py"
    if not os.path.exists(filename):
        raise HTTP(404)
    with open(filename) as stream:
        controller = stream.read().strip()
    data.append(
        {"name": f"examples/{name}.py", "content": controller, "language": "python"}
    )
    templates = re.compile("[/\w]+\.html").findall(controller)
    for template in templates:
        with open(f"apps/showcase/templates/{template}") as stream:
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
        if not other.startswith(".") or other == '.common':
            continue
        filename = other[1:].replace(".", "/") + ".py"
        with open(f"apps/showcase/{filename}") as stream:
            content = stream.read().strip()
            data.append({"name": filename, "content": content, "language": "python"})
    executable = MODE == "full" or name in globals()
    return {"files": data, "mode": MODE, "name": name, "executable": executable}
