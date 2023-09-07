
from django.contrib import admin
from django.urls import path,include

from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('geofence.urls')),
    path("", RedirectView.as_view(url="qr-code-demo/", permanent=True)),
    path("qr-code-demo/", include("qr_code_demo.urls", namespace="qr_code_demo")),
    path("qr-code/", include("qr_code.urls", namespace="qr_code")),
]
