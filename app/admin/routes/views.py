'''
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for, request, render_template

class CustomCategoryView(ModelView):
    list_template = 'admin/category_list.html'
    form_excluded_columns = ('posts',)

class CustomPostView(ModelView):
    list_template = 'admin/posts.html'
    form_excluded_columns = ('category',)
'''