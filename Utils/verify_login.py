from json import loads
from flask import request


def verify_login(database):
    token = loads(request.form["json"])["uniqueID"]
    try:
        if database.select("""SELECT desactivated FROM cantina_administration.user WHERE token = %s""", (token,), 1)[0]:
            return "desactivated"
    except TypeError:
        return False

    token_validation = database.select("""SELECT id FROM cantina_administration.user WHERE token=%s""", (token,),
                                       number_of_data=1)
    validation = loads(request.form["json"])["secretID"]
    validation_from_db = database.select("""SELECT content FROM cantina_pensive.config WHERE name=%s""",
                                         ("secret_token",), number_of_data=1)

    return True if token_validation is not None and validation == validation_from_db[0] else False
