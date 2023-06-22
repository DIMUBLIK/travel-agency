from django.shortcuts import render, redirect
from .models import Applications
from .forms import ApplicationsForm


def tours_home(request):

    return render(request, 'tours.html')


def application(request):
    error = ''
    if request.method == 'POST':
        form = ApplicationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tours_home')

        else:
            error = 'Форма была неверной'

    form = ApplicationsForm()
    data = {
        'form': form,
        'error': error
    }


    return render(request, 'applications.html', data)