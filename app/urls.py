from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import set_language  # ✅ Import necessário

from cars.views import (
    CarsListView, NewCarCreateView,
    CarDetailView, CarUpdateView, CarDeleteView
)

from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('set_language/', set_language, name='set_language'),  # ✅ Adicionada aqui
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car', NewCarCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
]

# ✅ Configuração para servir arquivos de mídia no modo de desenvolvimento
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
