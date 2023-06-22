from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')


def find_tour(request):
    return render(request, 'tours.html')


def contacts(request):
    return render(request, 'contacts.html')
