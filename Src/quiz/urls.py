from django.contrib import admin
from django.urls import path
from .views import quiz_view, test_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', quiz_view),
    path('test/<int:id>/<str:answ>', test_view)
]