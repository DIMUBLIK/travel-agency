from django.shortcuts import render, redirect
from .models import FeedBack
from .forms import FeedBackForm


def reviews_home(request):
    reviews = FeedBack.objects.order_by('-date')
    return render(request, 'reviews.html', {'reviews': reviews})


def create(request):
    error = ''
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews_home')

        else:
            error = 'Форма была неверной'

    form = FeedBackForm()
    data = {
        'form': form,
        'error': error
    }


    return render(request, 'create.html', data)


