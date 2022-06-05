import logging

from .common import unauthenticated


@unauthenticated.callback("click me")
def a_callback(msg):
    logging.info(msg)


@unauthenticated.get()
def show_a_button():
    return dict(mybutton=a_callback.button("clickme")(msg="hello world"))
