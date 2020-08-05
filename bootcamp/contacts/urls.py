from django.conf.urls import url
from bootcamp.contacts import views

app_name = 'contacts'
urlpatterns = [
    url(r'^$', views.Contact, name='contact_page'),
    url(r'^Add_contact_details/', views.Add_contact_details, name='Add_contact_details')    
]
