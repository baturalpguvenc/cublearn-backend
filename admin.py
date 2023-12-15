from flask import abort, render_template, session
from user import User

def admin():
    user_data = session.get('user', None)
    if user_data and user_data.get('is_admin', False):
        # Eğer kullanıcı admin yetkisine sahipse, admin sayfasını göster
        return render_template('admin.html')
    else:
        # Admin yetkisi yoksa, 403 hatası göster
        abort(403)