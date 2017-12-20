from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
	# Dec Vars
	categories = PhotoCategory.objects.filter(active=True, featured=True)

	context = {
        'page': 'index',
        'categories': categories
    }
	return render(request, 'index.html', context)


def single(request, category_id):
	category = get_object_or_404(PhotoCategory, pk=category_id)
	category_photos = category.photos.filter(show=True)

	context = {
		'page': 'single',
		'photos': category_photos,
		'category': category

	}
	return render(request, 'single.html', context)


def portfolio(request):
	# Dec Vars
	categories = PhotoCategory.objects.filter(active=True)

	context = {
		'page': 'portfolio',
		'categories': categories
	}
	return render(request, 'portfolio.html', context)


def about(request):
    context = {
        'page': 'about',
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'page': 'contact',
    }
    return render(request, 'contact.html', context)
