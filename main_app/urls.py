from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('characters/', views.character_index, name='index'),
    path('characters/<int:char_id>/', views.char_detail, name='detail'),
    path('characters/create', views.CharCreate.as_view(), name='chars_create'),
    path('characters/<int:pk>/update/', views.CharUpdate.as_view(), name='chars_update'),
    path('characters/<int:pk>/delete/', views.CharDelete.as_view(), name='chars_delete')
]