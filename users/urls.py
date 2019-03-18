from django.urls import path
from . views import ContactListView, ContactCreateView, ContactUpdateView, ContactDeleteView

app_name = 'users'

urlpatterns = [
    path('', ContactListView.as_view(), name='contact-index'),
    path('contact-create/', ContactCreateView.as_view(), name='contact-create'),
    path('<int:pk>/contact-update/', ContactUpdateView.as_view(), name='contact-update'),
    path('<int:pk>/contact-delete/', ContactDeleteView.as_view(), name='contact-delete'),
]
