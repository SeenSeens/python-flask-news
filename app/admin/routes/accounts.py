from flask import render_template
from app.admin import admin_bp
from flask_login import login_required
from utils.decorators import admin_required
@admin_bp.route('/accounts')
@login_required
@admin_required
def accounts():
    return render_template('admin/pages/accounts/accounts.html')