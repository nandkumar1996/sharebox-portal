from django.shortcuts import render
from .models import Contact_form
from config.settings import local
from django.core.mail import send_mail
# Create your views here.
def Contact(request):
	return render(request, 'contact_page.html')


def Add_contact_details(request):
	name = request.POST['name']
	email = request.POST['email']
	message = request.POST['message']
    
	contact_info = Contact_form(name=name,email=email,message=message)
	contact_info.save()
	email_list=[email]
	from_email = local.EMAIL_HOST_USER
	print(from_email)
	send_mail('Sharebox',
			  'hii ,\n\tThis is Nandkumar from Sharebox.\nThank you for contacting us.\n\n\n\n\nWarm Regards\n Nandkumar Sanodiya',
			  from_email,
			  email_list,
			  fail_silently=False)
	return render(request, 'contact_page.html')

	


