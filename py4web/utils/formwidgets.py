from yatl.helpers import DIV, INPUT, LABEL
from py4web.utils.form import get_options

def radio_widget(field, values_dict):
    control = DIV()
    if "_table" in dir(field):
        tablename = field._table
    else:
        tablename = "no_table"
    for k, v in get_options(field.requires)[1:]:
        attrs = {}
        if values_dict and str(values_dict["order_type"]) == k:
            attrs["_checked"] = "ON"
        control.append(
            INPUT(
                v,
                _id="%s_%s" % (tablename, k),
                _value=k,
                _label=v,
                _name=field.name,
                _type="radio",
                **attrs,
            )
        )
        control.append(LABEL(v, _for="%s_%s" % (tablename, k)))

    return control
