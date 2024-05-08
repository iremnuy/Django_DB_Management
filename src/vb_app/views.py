from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from vb_app.queries.authenticate_manager import  authenticate_manager,see_stadiums as see_std
from .forms import PlayerForm, CoachForm, JuryForm
from django.db import connection


def execute_query(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        return cursor.fetchall()
    
def gen_login(request): #general login choice router like db manager login,coach login, player login 
    return render(request,'general_login.html')

def coach_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        success = authenticate_manager(table='Coach', username=username, password=password)
        if success:
            return redirect('dash_coach')  # Redirect to the dashboard URL pattern
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

def dashboard_coach(request):
    return render(request,'dash_coach.html') 

def see_stadiums(request) :
    if request.method == 'GET':
        stadiums = see_std()
        if stadiums:
            return render(request,'stadiums.html',{'stadiums':stadiums})  # Redirect to the dashboard URL pattern
        else:
            # Handle invalid login
            return render(request, 'result.html', {'message': 'An error occured, maybe there is no stadium ?'})
    return render(request, 'dash_coach.html')

def delete_match(request):
    if request.method == 'POST':
        match_id = request.POST.get('session_id')
        if match_id:
            # Delete match from the database
            query = "DELETE FROM MatchSession WHERE session_ID = %s" #also delete from sguadsession
            query2 = "DELETE FROM SessionSquads WHERE session_ID = %s"
            params = (match_id,)
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                cursor.execute(query2, params)
                # Commit the transaction if needed
                # connection.commit()
            # Redirect or render success message
            success_message="You just deleted the match and fully used your political power"
        else:
            failure_msg="Please provide a match id!"
            return render(request,'delete_match.html',{'message' :failure_msg})
        return render(request,'delete_match.html',{'message' :success_message})
    else:
        return render(request, 'delete_match.html')

def jury_login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        success=authenticate_manager(table='Jury',username=username,password=password)
        if success:
            return redirect('dash_jury')  # Redirect to the dashboard URL pattern
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

def player_login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        success=authenticate_manager(table='Jury',username=username,password=password)
        if success:
            return redirect('dash_player')  # Redirect to the dashboard URL pattern
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        success = authenticate_manager(table='DBManager',username=username, password=password)
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
    player_form = PlayerForm()
    coach_form = CoachForm()
    jury_form = JuryForm()
    if request.method == 'POST':
        if 'submit_player' in request.POST:
            form = PlayerForm(request.POST)
            if form.is_valid():
                # Extract form data
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                name = form.cleaned_data['name']
                surname = form.cleaned_data['surname']
                date_of_birth = form.cleaned_data['date_of_birth'] #todo, format all dates in  db to same format 
                height = form.cleaned_data['height']
                weight = form.cleaned_data['weight']
                # Execute SQL query to insert new player into database
                query = "INSERT INTO Player (username, password, name, surname, date_of_birth, height, weight) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                params = (username, password, name, surname, date_of_birth, height, weight)
                inserted=execute_query(query, params)
                return render(request,'result.html',{'message':'Player added successfully!'})
                # Perform any additional processing if needed
            else:
                print(form.errors)
        elif 'submit_coach' in request.POST:
            form = CoachForm(request.POST) #ask what will happen if a same username is added 
            if form.is_valid():
                # Extract form data
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                name = form.cleaned_data['name']
                surname = form.cleaned_data['surname']
                nationality = form.cleaned_data['nationality']
                # Execute SQL query to insert new coach into database
                query = "INSERT INTO Coach (username, password, name, surname, nationality) VALUES (%s, %s, %s, %s, %s)"
                params = (username, password, name, surname, nationality)
                inserted=execute_query(query, params)
                return render(request,'result.html',{'message':'Coach added successfully!'})
                # Perform any additional processing if needed
        elif 'submit_jury' in request.POST:
            form = JuryForm(request.POST)
            if form.is_valid():
                # Extract form data
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                name = form.cleaned_data['name']
                surname = form.cleaned_data['surname']
                nationality = form.cleaned_data['nationality']
                # Execute SQL query to insert new jury into database
                query = "INSERT INTO Jury (username, password, name, surname, nationality) VALUES (%s, %s, %s, %s, %s)"
                params = (username, password, name, surname, nationality)
                inserted=execute_query(query, params)
                return render(request,'result.html',{'message':'Jury added successfully!'})
                # Perform any additional processing if needed

    else:
        player_form = PlayerForm()
        coach_form = CoachForm()
        jury_form = JuryForm()
    return render(request, 'add_user.html', {'player_form': player_form, 'coach_form': coach_form, 'jury_form': jury_form})
def change_stadium_name_view(request):
    # Logic for changing stadium name
    if request.method == 'POST':
        new_stadium_name = request.POST.get('new_stadium_name')
        stadium_id=request.POST.get('stadium_id')
        if stadium_id:
            # Update stadium name in the database
            query = "UPDATE MatchSession M SET M.stadium_name = %s WHERE M.stadium_ID = %s"
            params = (new_stadium_name, stadium_id)
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                # Commit the transaction if needed
                # connection.commit()
            # Redirect or render success message
            success_message="You just updated the stadium name and fully used your political power"
        else:
            failure_msg="Please provide a stadium id!"
            return render(request,'change_stadium_name.html',{'failure_msg' :failure_msg})
        return render(request,'change_stadium_name.html',{'success_message' :success_message})
    else:
        return render(request, 'change_stadium_name.html')