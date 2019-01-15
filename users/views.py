from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import ProfileForm, SignupForm


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


@login_required
def profile_update(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            user_profile.org = form.cleaned_data['org']
            user_profile.tel = form.cleaned_data['telephone']
            user_profile.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            defaulte_data = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'org': user_profile.org,
                'telephone': user_profile.tel
            }
            form = ProfileForm(defaulte_data)
    return render(request, 'profile_date.html', {'user': user, 'form': form})
