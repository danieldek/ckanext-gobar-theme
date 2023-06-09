import ckan.plugins.toolkit as tk


def gobar_theme_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "gobar_theme_required": gobar_theme_required,
    }
