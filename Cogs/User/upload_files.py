from werkzeug.utils import secure_filename
from Utils.verify_login import verify_login
from flask import request
from os import path


def upload_files_cogs(database, app):
    if not verify_login(database):
        return "loginerror"
    elif verify_login(database) == 'desactivated':  # Si l'utilisateur est connecté mais que son compte est désactivé
        return "desactivated"

    if 'file' not in request.files:
        return "Error"

    file = request.files['file']
    if file.filename == '':
        return "Error"

    # Sécurisation du nom de fichier et extraction de l'extension
    filename = secure_filename(file.filename)

    file.save(path.join(app.config['UPLOAD_FOLDER'], filename))

    return "hihihihih"
