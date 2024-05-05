from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from vb_app.queries.authenticate_manager import authenticate_manager

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        success = authenticate_manager(username=username, password=password)
        if success :
            #login(request, user)
            # Redirect to the desired page after login
            return redirect('dashboard')  # Change 'home' to the name of your desired URL pattern
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

# Create your views here.

def dashboard_view(request):
    return render(request, 'dashboard.html')


def add_user_view(request):
    # Logic for adding a user
    return render(request, 'add_user.html')

def change_stadium_name_view(request):
    # Logic for changing stadium name
    return render(request, 'change_stadium_name.html')