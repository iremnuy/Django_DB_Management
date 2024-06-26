from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from vb_app.queries.authenticate_manager import  authenticate_manager,see_stadiums as see_std
from .forms import PlayerForm, CoachForm, JuryForm,MatchForm,SquadForm,RateForm
from django.db import connection


def execute_query(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        return cursor.fetchall()
def execute_query_post(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        return cursor.rowcount
def gen_login(request): #general login choice router like db manager login,coach login, player login 
    return render(request,'general_login.html')

def coach_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        success = authenticate_manager(table='coaches', username=username, password=password)
        if success:
            request.session['username'] = username
            return redirect('dash_coach')  # Redirect to the dashboard URL pattern
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

def dashboard_coach(request):
    return render(request,'dash_coach.html') 
def dashboard_jury(request):
    return render(request,'dash_jury.html')
def dashboard_player(request):
    return render(request,'dash_player.html')

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
            query = "DELETE FROM matchsession WHERE session_ID = %s" #also delete from squadsession
            params = (match_id,)
            with connection.cursor() as cursor:
                cursor.execute(query, params)
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
        success=authenticate_manager(table='juries',username=username,password=password) #check the jury table if match
        if success:
            request.session['username'] = username  # Store the username in the session TODO do this for other logins
            return redirect('dash_jury')  # Redirect to the dashboard URL pattern
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

def player_login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        success=authenticate_manager(table='players',username=username,password=password)
        if success:
            request.session['username'] = username  # Store the username in the session
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

def view_ratings(request):
    jury_name=request.session['username']
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT COUNT(session_id) AS total_rated_sessions,
                    AVG(rating) AS avg_rating
            FROM assignedto
            WHERE assigned_jury_username = %s AND rating IS NOT NULL
        """, [jury_name])
        row = cursor.fetchone()
        total_rated_sessions = row[0] if row[0] else 0
        avg_rating = row[1] if row[1] else 0
    return render(request, 'view_ratings.html', {'total_rated_sessions': total_rated_sessions, 'avg_rating': avg_rating})


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
                query = "INSERT INTO players (username, password, name, surname, date_of_birth, height, weight) VALUES (%s, %s, %s, %s, %s, %s, %s)"
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
                query = "INSERT INTO coaches (username, password, name, surname, nationality) VALUES (%s, %s, %s, %s, %s)"
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
                query = "INSERT INTO juries (username, password, name, surname, nationality) VALUES (%s, %s, %s, %s, %s)"
                params = (username, password, name, surname, nationality)
                inserted=execute_query(query, params)
                return render(request,'result.html',{'message':'Jury added successfully!'})
                # Perform any additional processing if needed

    else:
        player_form = PlayerForm()
        coach_form = CoachForm()
        jury_form = JuryForm()
    return render(request, 'add_user.html', {'player_form': player_form, 'coach_form': coach_form, 'jury_form': jury_form})
def change_stadium_name_view(request): #CHECKED
    # Logic for changing stadium name
    if request.method == 'POST':
        new_stadium_name = request.POST.get('new_stadium_name')
        stadium_id=request.POST.get('stadium_id')
        if stadium_id:
            # Update stadium name in the database
            query = "UPDATE stadium S SET S.stadium_name = %s WHERE S.stadium_ID = %s"
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
    
def add_match(request):
    """
    Coaches shall be able to add a new match session, he/she can only put his/her current team ID. 
    Stadium info and date, time, timeslot info are up to the coach’s choice but they should not be conflicting.
        You should check for any type of con- flict with triggers. Also coach can choose(assign) 
        his/her own session’s assigned jury (by jury’s name and surname). 
        The rating of the newly added session should be left blank or null at first,
        till a jury logs in and rates the match.
    """
    form = MatchForm()
    if request.method == 'POST':
        if 'submit_match' in request.POST:
            form = MatchForm(request.POST)
            if form.is_valid():   
                # Extract form data
                date = form.cleaned_data['date']
                time_slot = form.cleaned_data['time_slot']
                stadium_id = form.cleaned_data['stadium']
                jury_name = form.cleaned_data['jury_name']
                jury_surname = form.cleaned_data['jury_surname']
                team_id_form = form.cleaned_data['team_id']
                #check if coach's team is the same with the team_id from contract table , check if contract finish date is not passed
                query_2="SELECT team_id FROM contract WHERE coach_username=%s AND contract_finish>%s" #TODO: do not make hardcoded
                username=request.session['username']
                params_2=(username,date)
                print("username of coach is",params_2)
                teams=execute_query(query_2,params_2)
                if not teams:
                    message=f"Hello {username},you do not have a team right now or your contract is expired!"
                    return render(request,'result.html',{'message':message})
                team_id= teams[0][0]
                request.session['team_id']=team_id
                if team_id_form!=team_id:
                    return render(request,'result.html',{'message':'You can only add a match session to your own team, your team_id is {team_id}!'})
                print("coach's current team is ",team_id)
                #CHECK if jury name and surname is valid
                query_4="SELECT username FROM juries WHERE name=%s AND surname=%s"
                params_4=(jury_name,jury_surname)
                assigned_jury_username=execute_query(query_4,params_4)
                print("jury_username is",assigned_jury_username)
                if not assigned_jury_username:
                    return render(request,'result.html',{'message':'Please enter a valid jury name and surname!'})
                #choose session_id as max(session_id)+1
                query_session_id="SELECT MAX(session_id) FROM matchsession"
                session_id=execute_query(query_session_id)
                session_id=session_id[0][0]+1 #THIS WILL BE THE NEW SESSION ID
                print("session_id is",session_id)
                    
                #TODO: CREATE A TRIGGER TO INSERT INTO ASSIGNEDTO,PLAYEDBY,PLAYEDIN TABLES !!! ALSO CHECK INTEGRITY 
                #HERE I USED MULTİPLE CURSOR EXECUTIONS AND CREATED A MANUAL ROLLBACK MECHANISM TO HANDLE THE INTEGRITY CHECKS
                #TO AVOID USING TRANSACTIONS AND JOINING MULTIPLE TABLES IN A SINGLE QUERY WHICH WOULD LED TO OVERHEAD 
                query = "INSERT INTO matchsession (session_id,team_id) VALUES (%s , %s)"
                params = (session_id,team_id_form)
                rollback="DELETE FROM matchsession WHERE session_id=%s"
                query_3="INSERT INTO assignedto (assigned_jury_username, session_id) VALUES (%s , %s)"
                params_3=(assigned_jury_username , session_id)
                rollback_3="DELETE FROM assignedto WHERE session_id=%s and assigned_jury_username=%s"
                query_5="INSERT INTO playedin (time_slot, date, stadium_id, session_id) VALUES (%s ,%s, %s ,%s)"
                params5=(time_slot,date,stadium_id,session_id)
                rollback_5="DELETE FROM playedin WHERE session_id=%s"
                query_6="INSERT INTO playedby (session_id, date, time_slot, team_id) VALUES (%s ,%s, %s ,%s)"
                params6=(session_id,date,time_slot,team_id_form)
                rollback_6="DELETE FROM playedby WHERE session_id=%s"
                try:
                    execute_query_post(query, params)
                except:
                    execute_query(rollback,(session_id,))
                    return render(request,'result.html',{'message':'An error occured while adding the match session!'})
                try:
                    execute_query_post(query_3,params_3)
                except:
                    execute_query(rollback_3,(session_id,assigned_jury_username))
                    execute_query(rollback,(session_id,))
                    return render(request,'result.html',{'message':'An error occured while adding the assigned jury!'})
                
                #check if the date is not conflicting TODO
                try:
                    execute_query_post(query_5,params5)
                except:
                    execute_query(rollback_5,(session_id,))
                    execute_query(rollback_3,(session_id,assigned_jury_username))
                    execute_query(rollback,(session_id,))
                    return render(request,'result.html',{'message':'An error occured while adding the playedin info!'})

                #TODO : add to playedby table fileds : session_id,date,time_slot,team_id
                try:
                    execute_query_post(query_6,params6)
                except:
                    execute_query(rollback_6,(session_id,))
                    execute_query(rollback_5,(session_id,))
                    execute_query(rollback_3,(session_id,assigned_jury_username))
                    execute_query(rollback,(session_id,))
                    return render(request,'result.html',{'message':'An error occured while adding the playedin info!'})
                link='add_squad'
                request.session['session_id']=session_id
                return render(request,'result.html',{'message':'Match session added successfully! \n Here is the information of the match session you added: \n session_id: '+str(session_id)+'\n team_id: '+str(team_id_form)+'\n jury_username: '+str(assigned_jury_username)+'\n date: '+str(date)+'\n time_slot: '+str(time_slot)+'\n stadium_id: '+str(stadium_id),'link':link,'link_text':'Add squad to this match session'})
                #join tables al together recompose them 
                #return the newly added match session
                
            
                # Perform any additional processing if needed

                
                
            else:
                print("form is not valid")
                print(form.errors)
                return render(request,'result.html',{'message':form.errors})
    else :
        form = MatchForm()        
        return render(request,'add_match.html',{'match_form':form})
    
def add_squad(request):
    print("hello")
    form= SquadForm()
    session_id,time_slot,date,team_id,players=get_players_of_team(request)
    print("session id, team id and players are : ",session_id,team_id,players)
    if request.method == 'POST':
        print("posted")
        form = SquadForm(request.POST)
        if form.is_valid():
            # Extract form data
            player1 = form.cleaned_data['player1']
            player2 = form.cleaned_data['player2']
            player3 = form.cleaned_data['player3']
            player4 = form.cleaned_data['player4']
            player5 = form.cleaned_data['player5']
            player6 = form.cleaned_data['player6']
            team_id_form = form.cleaned_data['team_id']
            session_id_form= form.cleaned_data['session_id']
            position1 = form.cleaned_data['position1']
            position2 = form.cleaned_data['position2']
            position3 = form.cleaned_data['position3']
            position4 = form.cleaned_data['position4']
            position5 = form.cleaned_data['position5']
            position6 = form.cleaned_data['position6']
            #zip players and positions as a list of tuples, check if position is valid for that player
            players=[player1, player2, player3, player4, player5, player6]
            positions=[position1, position2, position3, position4, position5, position6]
            zipped_list=zip(players,positions)
            valid,player=check_positions(zipped_list) #if false return also the player name
            message=f"Please enter a valid position for player {player}!"
            if not valid:
                return render(request,'result.html',{'message':message})
            # Execute SQL query to insert new squad into database
            #TODO: CHECK IF THE PLAYERS ARE IN THE SAME TEAM WITH THE COACH
            query_1="SELECT team_id FROM contract WHERE coach_username=%s AND contract_finish>%s"
            date='2024-05-10' #TODO: do not make hardcoded
            username=request.session['username']
            params_1=(username,date,)
            teams=execute_query(query_1,params_1)
            print("teams are",teams)
            #or check if tuple is empty
            if (not teams) or team_id_form!=teams[0][0]:
                return render(request,'result.html',{'message':'You can only add a squad to your own team!'})
            if session_id_form!=session_id:
                return render(request,'result.html',{'message':'You can only add a squad to the match session you added!'})
            
            for player, position in zip(players,positions):
                print("player and position in for are",player,position)
                query = "INSERT INTO playerinmatch (session_id, player_username, position_id,time_slot,date) VALUES (%s, %s, %s, %s,%s)"
                params = (session_id_form, player, position,time_slot,date,)
                try:
                    print("trying to execute")
                    execute_query_post(query, params)
                except:
                    message=f"Player named {player} has already a match in that time...or maybe you are trying to insert same player in the same squad,please don't!"
                    #rollback 
                    query_rollback="DELETE FROM playerinmatch WHERE session_id=%s"
                    params_rollback=(session_id_form,)
                    execute_query(query_rollback,params_rollback)
                    return render(request,'result.html',{'message':message})
            return render(request,'result.html',{'message':'Squad added successfully! ','link':'dash_coach','link_text':'Go back to dashboard'})
        else:
            return render(request,'result.html',{'message':form.errors})
    else:
        print("not post")
        return render(request,'add_squad.html',{'session_id':session_id,'team_id':team_id,'players':players,'squad_form':form})
def get_players_of_team(request):
    session_id = request.session['session_id']
    team_id = request.session['team_id']
    query = "SELECT username FROM playsin WHERE team_id = %s"
    params = (team_id,)
    players = execute_query(query, params)
    query = "SELECT time_slot,date FROM playedin WHERE session_id = %s"
    params = (session_id,)
    result = execute_query(query, params)
    time_slot=result[0][0]
    date=result[0][1]
    return session_id,time_slot,date,team_id,players


def check_positions(zipped_list):
    for player, position in zipped_list:
        print("player and position are",player,position)
        query = "SELECT * FROM playerpositions WHERE username = %s AND position_id=%s" #there can be multiple positions for a player
        params = (player,position)
        result = execute_query(query, params)
        if not result: #if there is no player with that position
            print("player and position are",player,position)
            print("result is",result)
            return False,player
    return True,None


def rate_matches(request):
    form=RateForm()
    juryname=request.session['username']
    query="SELECT session_id FROM assignedto WHERE assigned_jury_username=%s "
    params=(juryname,)
    available_matches=execute_query(query,params)
    if request.method=='POST':
        form = RateForm(request.POST)
        if form.is_valid():
            # Extract form data
            session_id=form.cleaned_data['session_id']
            rating=form.cleaned_data['rating']
            # Execute SQL query to insert new squad into database
            query = "UPDATE assignedto SET rating=%s WHERE assigned_jury_username=%s AND session_id=%s AND rating is NULL" #all matches including already rated ones 
            params = (rating,juryname,session_id)
            #if match date is not passed, trigger should not allow to rate by checking playedin table 
            try:
                rowcount=execute_query_post(query, params) #ASK: What happens if here a trigger is fired and it fails?
            except:
                return render(request,'result.html',{'message':'An error occured while rating the match..Maybe you are trying to rate a future match!'})
            if rowcount==0:
                return render(request,'result.html',{'message':'You already rated this match or session id mismatches!'}) 
            return render(request,'result.html',{'message':'Match rated successfully!'})   
    return render(request,'rate_matches.html',{'rate_match_form':form,'available_matches':available_matches})

def view_height_of_most_played(request):
    current_player_username = request.session.get('username')
    if not current_player_username:
        return redirect('login')  # Redirect if not logged in

    most_played_with_height_query = """
    SELECT AVG(players.height) AS average_height
    FROM (
        SELECT other.player_username
        FROM playerinmatch AS current
        JOIN playerinmatch AS other ON current.session_id = other.session_id
        WHERE current.player_username = %s AND current.player_username != other.player_username
        GROUP BY other.player_username
        HAVING COUNT(*) = (
            SELECT MAX(num_matches)
            FROM (
                SELECT COUNT(*) AS num_matches
                FROM playerinmatch AS current
                JOIN playerinmatch AS other ON current.session_id = other.session_id
                WHERE current.player_username = %s AND current.player_username != other.player_username
                GROUP BY other.player_username
            ) AS max_matches
        )
    ) AS most_played
    JOIN players ON most_played.player_username = players.username
    """

    with connection.cursor() as cursor:
        cursor.execute(most_played_with_height_query, [current_player_username, current_player_username])
        result = cursor.fetchone()
        average_height = result[0] if result else None  # Safe access to the first element

    return render(request, 'height_of_most_played.html', {'average_height': average_height})

def view_played_with_players(request):
    current_player_username = request.session.get('username')
    if not current_player_username:
        return redirect('login')  # Redirect if not logged in

    played_with_query = """
    SELECT DISTINCT players.username, players.name, players.surname
    FROM playerinmatch AS current
    JOIN playerinmatch AS other ON current.session_id = other.session_id
    JOIN players ON other.player_username = players.username
    WHERE current.player_username = %s AND current.player_username != other.player_username
    """
    with connection.cursor() as cursor:
        cursor.execute(played_with_query, [current_player_username])
        played_with_players = cursor.fetchall()

    # Transform result into a list of dicts for easier handling in the template
    players_list = [{'username': row[0], 'name': row[1], 'surname': row[2]} for row in played_with_players]

    return render(request, 'played_with_players.html', {'played_with_players': players_list})