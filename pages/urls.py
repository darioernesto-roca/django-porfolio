from django.urls import path
from pages.views import contact_message_view, dynamic_pages_view, root_page_view

app_name = 'pages'

urlpatterns = [
    path('', root_page_view, name="index"),
    path('services/contact/', contact_message_view, name='contact_message'),
    path('<str:template_name>/', dynamic_pages_view, name='dynamic_pages')
]
