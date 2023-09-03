from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisement
from .forms import AdvertisementForm

def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisement.objects.filter(title__contains=title)
    else:
        advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements, 'title': title}
    return render(request, 'advertisement/index.html', context)

def top_sellers(request):
    return render(request, 'advertisement/top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('advertisement/index')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement/advertisement-post.html', context)

def advertisement(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {'adv': advertisement}
    return render(request, 'advertisement/advertisement.html', context)
