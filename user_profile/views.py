from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from .forms import *
from .models import Post, Profile

@login_required(login_url='user_auth:login')
def ProfileView(request):
    user = request.user
    posts = Post.objects.order_by('-published')
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            username = request.user.id
            post_body = form.cleaned_data['post_text']
            new_post = Post(user=user, body=post_body)
            new_post.save()
            form = CreatePostForm()
            context = {
                'user': user,
                'form': form,
                'posts': posts,
            }
            return render(request, 'user_profile/profile.html', context)
    else:
        form = CreatePostForm()
    return render(request, 'user_profile/profile.html', {'form': form, 'user': user, 'posts': posts})


@login_required(login_url='user_auth:login')
def ProfileEditView(request):
    if request.method == 'POST':
        edit_profile_form = ProfileEditForm(request.POST, request.FILES)
        if edit_profile_form.is_valid():
            cleaned_data = edit_profile_form.cleaned_data
            user = request.user
            if cleaned_data['name'] != '': user.first_name = cleaned_data['name'] 
            if cleaned_data['surname'] != '': user.last_name = cleaned_data['surname'] 
            if hasattr(user, 'user_profile'):
                profile = user.user_profile
            else:
                profile = Profile(user=user)
            if request.FILES: profile.avatar = request.FILES['avatar'] 
            if cleaned_data['age'] != '': profile.age = cleaned_data['age']
            if cleaned_data['location'] != '': profile.location = cleaned_data['location'] 
            if cleaned_data['work_exp'] != '': profile.work_exp = cleaned_data['work_exp'] 
            if cleaned_data['it_stack'] != '': profile.it_stack = cleaned_data['it_stack'] 
            user.save()
            profile.save()
            messages.success(request, 'Профиль успешно изменен!')
            return HttpResponseRedirect(reverse('user_profile:edit_profile'))
        else:
            messages.error(request, 'Что-то пошло не так(')
            return HttpResponseRedirect(reverse('user_profile:edit_profile'))
    else:
        edit_profile_form = ProfileEditForm()


    return render(request, 'user_profile/edit_prof.html', {'form': edit_profile_form})


