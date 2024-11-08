from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

@login_required
def map_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
        location = profile.location
    except Profile.DoesNotExist:
        location = None
    return render(request, 'map.html', {'location': location})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('map')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def update_location(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.location = Point(float(longitude), float(latitude))
        profile.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
