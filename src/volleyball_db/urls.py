"""
URL configuration for volleyball_db project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vb_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.gen_login,name='general'),
    path('login/', views.login_view, name='general_login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add_user/', views.add_user_view, name='add_user_view'),
    path('change_stadium_name/', views.change_stadium_name_view, name='change_stadium_name_view'),
    path('coach_login/',views.coach_login_view,name='coach_login'),
    path('jury_login/',views.jury_login_view,name='jury_login'),
    path('player_login/',views.player_login_view,name='player_login'),
    path('dash_coach',views.dashboard_coach,name='dash_coach'),
    path('see_std/',views.see_stadiums,name='see_stadiums'),
    path('delete_match/',views.delete_match,name='delete_match'),

]
"""
path('add_match/',views.add_match,name='add_match'),
path('create_squad/',views.create_squad,name='create_squad'),
path('delete_match/',views.delete_match,name='delete_match'),
path('get_other_pl/',views.get_other_players,name='get_other_players'),
path('height/',views.height_of_most_played,name='height_of_most_played'),
path('avg_rate/',views.avg_rate,name='avg_rate'),
path('count_total/',views.count_total,name='count_total')
"""