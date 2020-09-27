from django.urls import path
from journal_app.views import (
    MyView, RegisterView, 
    LoginView, JournalView, 
    JournalListView, JournalEditView, 
    JournalDisplayTextArea, JournalDeleteView, 
    delete_view, JournalResetPassword,JournalUpdatePassword)
from . import views


app_name = "journal_app"

urlpatterns = [
    path('', MyView.as_view()),
    #journal/home/
    path('home/', MyView.as_view(), name="home"),
        #journal/register/
    path('register/',RegisterView.as_view(), name="register"),
     #journal/login/
    path('login/', LoginView.as_view(), name="login"),
    #journal/logout/
    path('logout/', views.user_logout, name="logout"),

    #journal/create
    path('create/', JournalView.as_view(), name="create"),
    #journal/list
    path('list/', JournalListView.as_view(), name="list"),
    #journal/edit/<int:question_id>
    path('edit/<int:journal_id>', JournalEditView.as_view(), name="edit"),
     #journal/view/<int:question_id>
    path('view/<int:journal_id>', JournalDisplayTextArea.as_view(), name="view"),
    #journal/delete/<int:journal_id>
    path('delete/<int:journal_id>', views.delete_view, name="delete_view" ),
    #journal/delete/
    path('delete/', JournalDeleteView.as_view(), name="delete"),
    #journal/reset_password/
    path('reset_password/', JournalResetPassword.as_view(), name="reset_password"),
    #journal/update_password/
    path('update_password/', JournalUpdatePassword.as_view(), name="updatepassword")

]