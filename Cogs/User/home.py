from flask import request, redirect, url_for
from cantinaUtils.verify_login import verify_login


def user_home_cogs(database):
    # Vérification si l'utilisateur est connecté
    if not verify_login(database):
        return redirect(url_for('sso_login', error='0'))
    elif verify_login(database) == "desactivated":
        pass
