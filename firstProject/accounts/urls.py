from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout', views.log_out, name='log_out'),
    path('forgot-password', views.forgot_password, name='forgot_password'),
    path(
        "update-password/<str:token>/<str:uid>/",
        views.update_password,
        name="update_password",
    ),
    path('profile', views.update_profile, name='profile'),
    path('courses-recommend', views.recommend_courses, name='courses'),
    path('course', views.courses_list, name='courses_list'),
    path('courses-add', views.add_course, name='courses_add'),
    path('cours/<int:course_id>/participer/', views.participer_cours, name='participer_cours'),
    path('cours-participer', views.mes_cours_participes, name='mes_cours_participes'),





]
