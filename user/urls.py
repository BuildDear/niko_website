from django.urls import path, include
from product.views import products
from user.views import login, registration, profile, logout


app_name = 'user'

urlpatterns = [
   path('login/', login, name='login'),
   path('registration/', registration, name='registration'),
   path('profile/', profile, name='profile'),
   path('logout/', logout, name='logout')
]
