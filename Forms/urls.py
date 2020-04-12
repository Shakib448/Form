from django.contrib import admin
from django.urls import path, include
from .views import home, register, secrect_page
urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secret/', secrect_page, name='secrect'),
    # path('login/', login_page),
    # path('register/', register_page),
    # path('contact/', contact_page),
    path('admin/', admin.site.urls),
]
