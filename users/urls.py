from django.urls import path
from . views import ContactListView

app_name = 'users'

urlpatterns = [
    path('', ContactListView.as_view(), name='contact-index'),
]
