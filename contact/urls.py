

from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', view=views.index  ,name='index'),
    path('search', view=views.search, name='search'),

    # Contact CRUD
    path('contact/<int:contact_id>/detail/', view=views.contact, name='contact'),
    path('contact/create/', view=views.create, name='create'),
    path('contact/<int:contact_id>/update/', view=views.update, name='update'),
    path('contact/<int:contact_id>/delete/', view=views.delete, name='delete'),

    # User
  
    path('user/create/', view=views.register, name='register'),
    path('user/login/', view=views.login_view, name='login'),
    path('user/logout/', view=views.logout_view, name='user_logout'),
    path('user/update/', view=views.user_update, name='user_update')
]
 