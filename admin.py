from flask import abort, render_template, session
from user import User

def admin():
    user_data = session.get('user', None)
    if user_data and user_data.get('is_admin', False):
        return render_template('admin.html')
    else:
        abort(403)