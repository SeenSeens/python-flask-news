
from flask_admin.contrib.sqla import ModelView


class CustomCategoryView(ModelView):
    list_template = 'admin/category_list.html'
    form_excluded_columns = ('posts',)

class CustomPostView(ModelView):
    list_template = 'admin/posts.html'
    form_excluded_columns = ('category',)
