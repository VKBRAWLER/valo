from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
import jwt, datetime
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is None:
            raise AuthenticationFailed('Invalid credentials, try again')
        payload = {
            'id': user.id,
            'exp': datetime.datetime.now() + datetime.timedelta(days=1),
            'iat': datetime.datetime.now()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        login(request, user)
        return JsonResponse({
            'status': 'success',
            'jwt': token,
            })
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token,
    }
    return Response({'status': 'success'})
def register_user(request):
    if request.method == "POST":
        print(request.POST)
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            print("NOT lol")
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'User registered successfully.')
            return redirect('/')
        else:
            messages.error(request, form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'register.html')