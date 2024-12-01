from flask import current_app

APP_CODES = {
    100: "OK.",
    101: "Feature not implemented.",
}


def jsonify(state={}, metadata={}, code=100, status=200, headers={}):
    resource = state.copy()
    resource.update(metadata)
    resource["code"] = code
    if current_app.debug is True:
        resource["message"] = APP_CODES[code]
    return resource, status, headers
