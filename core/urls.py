
from django.contrib import admin
from django.urls import path
from apps.user.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),

    # path
    path('login/', LoginView.as_view(), name='login')
]
