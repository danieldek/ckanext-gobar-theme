import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def gobar_theme_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "gobar_theme_get_sum": gobar_theme_get_sum,
    }
