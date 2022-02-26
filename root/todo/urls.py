from django.urls import path
from . import views
urlpatterns = [
    path('', views.main_view),
    path('<int:task_id>/update', views.update_task),
    path('<int:task_id>/delete', views.delete_task),
    path('home/', views.home_page),
    path('pending/', views.pending_task),

]
