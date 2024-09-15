
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings

import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    path(r'xadmin/', xadmin.site.urls),
    path('admin/', admin.site.urls),
    re_path(r'media/(?P<path>.*)',serve, {"document_root": settings.MEDIA_ROOT}),
    path('home/', include("home.urls") ),
]
