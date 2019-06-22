from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from orders.forms import UserRegisterForm
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.contrib.auth.models import User

from orders.models import (DinnerPlatter, Pasta, Pizza, Salad, Sub, Addition,
                           Topping)

# Create your views here.
def index(request):
# If the user isn't logged in redirect to login page
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))

	context = {
		"pizzas": Pizza.objects.all(),
		"toppings": Topping.objects.all(),
		"subs": Sub.objects.all(),
		"additions": Addition.objects.all(),
		"pastas": Pasta.objects.all(),
		"salads": Salad.objects.all(),
		"platters": DinnerPlatter.objects.all()
	}

	return render(request, "menu.html", context)
	#HttpResponse("Project 3: Started")

def login_view(request):
	if request.method == "POST":
		# when page is loaded no post data
		username = request.POST["username"]
		password = request.POST["password"]

		# check if user has inputted valid username and password
		user = authenticate(request, username=username, password=password)

		# if valid logs user in and redirects home
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))
		# if not valid redirects to login page
		else:
			return render(request, "login.html")
	else:
		logout(request)
		return render(request, "login.html")

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse("login"))

def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			raw_password = form.cleaned_data.get("password1")

			user = authenticate(request, username=username, password=raw_password)
			
			if user is not None:
				login(request, user)
			return HttpResponseRedirect(reverse("index"))
		else:
			return HttpResponseRedirect(reverse("register"))
	else:
		logout(request)
		form = UserRegisterForm()
		return render(request, "register.html", {"form": form})

def cart(request):
	if request.method == "POST":
		address = request.user.email
		#emails = User.objects.filter(user=request.user)
#		address = from database
		send_mail(
			"Pinnochio's Pizza Order",
			"Thank you for ordering from Pinnochio's Pizza",
			"matalex412@gmail.com",
			[address],
			fail_silently=False
		)
		print(f"{address}")
		return HttpResponseRedirect(reverse("index"))

	else:
		return render(request, "cart.html")

@staff_member_required
def orders(request):
	return render(request, "orders.html")