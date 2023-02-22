app_name = 'docapp'

from django.urls import path
from .views import index, register_request, login_request, logout_request, create_tutorial_page, create_tutorial, \
    subject_create_page, subject_create, content_create_page, content_create, tutorials, tutorials_active

urlpatterns = [
    path('', index, name='index'),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),
    path("create_tutorial_page", create_tutorial_page, name="create_tutorial_page"),
    path("create_tutorial", create_tutorial, name="create_tutorial"),
    path("subject_create_page/<str:generated_code>", subject_create_page, name="subject_create_page"),
    path("subject_create/<str:generated_code>", subject_create, name="subject_create"),
    path("content_create_page/<str:generated_code>", content_create_page, name="content_create_page"),
    path("content_create/<str:generated_code>", content_create, name="content_create"),
    path("tutorials_active/<str:generated_code_tut>/<str:generated_code_subject>", tutorials_active, name="tutorials_active"),

    path("tutorials/<str:generated_code>", tutorials, name="tutorials"),
    # path("tutorials/<str:generated_code>/<str:generated_code1>", tutorials_choose, name="tutorials_choose"),
]
