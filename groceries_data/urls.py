from django.urls import path
from .views import home, info, update_info, delete_info

urlpatterns = [
    path('', home, name='home'),
    path('info', info, name='info'),
    path('info/<id>/update', update_info, name='update_info'),           
    path('info/<id>/delete', delete_info, name='delete_info'),    

]
