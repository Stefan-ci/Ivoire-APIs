from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages


def unauthenticated_user(view_func):
	"""
		Decorator to check if the current visitor is not authenticated.
		Used to check if the visitor is not authenticated when trying to 
		create an account and when logging in.
	"""
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			messages.warning(request, 'Sorry, You already signed in!')
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func




def admin_only(view_func):
	"""
		Decorator to allow access to admins (superusers) only
		and deny public users' access.
	"""
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			if not request.user.is_superuser:
				return 404
			else:
				return view_func(request, *args, **kwargs)
	return wrapper_func




def allowed_users(allowed_roles=[]):
	"""
		Decorator to allow to a list of groups of users to access a page.
	"""
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None

			if request.user.is_authenticated:
				if request.user.groups.exists():
					group = request.user.groups.all()[0].name
				if group in allowed_roles:
					return view_func(request, *args, **kwargs)
				else:
					return 404
			return redirect('login')
		return view_func
	return decorator
