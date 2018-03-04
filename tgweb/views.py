from django.shortcuts import render
from django.http import HttpResponse
from tgweb.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

# Create your views here.

def index(request):
	return render(request, 'tgweb/index.html')


def presentation(request):
	return render(request, 'tgweb/presentation.html')


def reservation(request):
	return render(request, 'tgweb/reservation.html')

def reservation1(request):
	return render(request, 'tgweb/reservation_page.html')



def promos(request):
	return render(request, 'tgweb/promos.html')


def contact(request):
	form_class = ContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get(
 				'contact_name'
			, '')
			contact_email = request.POST.get(
				'contact_email'
			, '')
			form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
			template = get_template('contact_template.txt')
			context = {
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content,
			}
			content = template.render(context)

			email = EmailMessage(
				"New contact form submission",
				content,
				"Your website" +'',
				['fouadlee9@gmail.com'],
				headers = {'Reply-To': contact_email }
			)
			email.send()
			return redirect('contact')

	return render(request, 'tgweb/contact.html', {
		'form': form_class,
	})


def article_page(request):
	return render(request, 'tgweb/article_page.html')



def test(request):
	return render(request, 'tgweb/test.html')

