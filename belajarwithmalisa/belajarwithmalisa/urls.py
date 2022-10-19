
from django.contrib import admin
from django.urls import path
from Materi.views import Materi
from Contoh.views import Contoh
from Latihan.views import Latihan
from Me.views import Me 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Materi/', Materi ),
    path('Contoh/', Contoh ),
    path('Latihan/', Latihan ),
    path('Me/', Me ),
]
