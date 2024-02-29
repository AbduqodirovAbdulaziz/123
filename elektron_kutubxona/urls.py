from django.contrib import admin
from django.urls import path
from mainAPP.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('barcha_bolim/', hamma_bolimlar),
    path('hamma_kitoblar/', hamma_kitoblar),
    path('yangi_asarlar/', tirik_muallif),
    path('ochir/<int:pk>/', kitob_ochir),

    path('',LoginView.as_view(), name='login'),
]
