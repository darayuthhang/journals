from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.models import User

from .models import Journal

from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse

from .forms import UserForm
# Create your views here.


class MyView(View):
    def get(self, request):
        return render(request, "index.html")


class RegisterView(View):
    '''
        RegisterView accepts the post request from sign up form.
    '''
    template_name = "register.html"
    
    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})
    
    @csrf_exempt
    def post(self, request):
        form = UserForm(request.POST or None) 
        # In the 'form' class the clean function  
        # is defined, if all the data is correct  
        # as per the clean function, it returns true 
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            # redirect it to some another page indicating data
            # is sucessfully inserted.
            return redirect('/journal/home')
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    '''
        LoginView accept post request from login form
    '''

    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name, {})

    @csrf_exempt
    def post(self, request):
        # accept username, password from template login.html
        username = request.session['username'] = request.POST['username']
        password = request.session['password'] = request.POST['password']

        
        # authenticate user if user does not exist, return HTTResponse    
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            if user is not None:
                login(request, user)
                return redirect("/journal/list/")
            else:
                return HttpResponse("account is not activate")
        else:
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid")
        return render(request, self.template_name, context)
       
    
@login_required
def user_logout(request):
    logout(request)
    return redirect('/journal/home/')
  
@method_decorator(login_required, name='dispatch')
class JournalView(View):
    '''
        JournalView accept text journal from the user
    '''
    template_name = "authenticate/create_journal.html"
    def get(self, request):
        return render(request, self.template_name, {})
    

    def post(self, request):
        title = request.POST['title']
        date = request.POST['date']
        text_area = request.POST['text_area']


        journal = Journal(user=request.user, title=title, text_area=text_area, date=date)

        journal.save()
        return redirect('/journal/list')

@method_decorator(login_required, name='dispatch')
class JournalListView(View):
    '''
        JournalLISTView is responsible for listing all the list of journal
    '''

    template_name = "authenticate/list_journal.html"
    
    def get(self, request):
        journal = Journal.objects.filter(user=request.user)
       
        context = {'journal': journal}
        return render(request, self.template_name, context)


@method_decorator(login_required, name='dispatch')
class JournalEditView(View):
    template_name ="authenticate/edit_journal.html"
    
    '''
    JournalEditView is responsible for updating the journal 
    '''
 
    def get(self, request, journal_id):
        try:
            journal = Journal.objects.get(id=journal_id)
            context = {'journal': journal}
        except Journal.DoesNotExist:
            raise Http404("Journal does not exist")
        return render(request, self.template_name, context)

    def post(self, request, journal_id):
        title = request.POST['title']
        date = request.POST['date']
        text_area = request.POST['text_area']

        
        journal = Journal.objects.get(pk=journal_id)
        
        journal.title = title
        journal.date = date
        journal.text_area = text_area
        
        journal.save()
        
        return redirect('/journal/list')

    
@method_decorator(login_required, name='dispatch')
class JournalDisplayTextArea(View):
    template_name = "authenticate/display.html"


    def get(self, request, journal_id):
        try:
            journal = Journal.objects.get(id=journal_id)
            context = {'journal': journal}
            
        except Journal.DoesNotExist:
            raise Http404('journal does not exist')
        return render(request, self.template_name, context)



@method_decorator(login_required, name='dispatch')
class JournalDeleteView(View):

    '''
        @JournalDeleteView is responsible for deleting journal after user hit delete button

    '''
    def post(self, request):
        try:
            journal_id = request.POST['journal_id']
            journal = Journal.objects.get(id=journal_id)
            journal.delete()
        except Journal.DoesNotExist:
            raise Http404('journal does not exist')
        return redirect('/journal/list')
    
@login_required
def delete_view(request, journal_id):
    return render(request, 'authenticate/delete.html', {'journal_id': journal_id})


class JournalResetPassword(View):
    template_name = 'account/reset_password.html'
    '''
       JournalResetPassword for sending email to user to allow user
       to reset password
    '''

    def get(self, request):
        return render(request, self.template_name, {})
    

    def post(self, request):
        try:
            user = User.objects.get(email=request.POST['email'])
            email = request.session['email'] = request.POST['email']

            ROUTE_UPDATE_PASSWORD = "http://127.0.0.1:8000/journal/update_password/"
            HOST_EMAIL = "khjournals@gmail.com"


            send_mail(
            subject = 'From Kh Journals',
            message = ROUTE_UPDATE_PASSWORD,
            from_email = HOST_EMAIL,
            recipient_list = [email,],
            fail_silently = False,
            )        
            
        except User.DoesNotExist:
            raise Http404("User does not exists")
        return redirect('/journal/home/')
        

class JournalUpdatePassword(View):
    template_name = "account/update_password.html"

    '''
        JournalUpdatePassword is responsible for updating, or reseting user password 
        after user receive email to reset password.
    '''
    
    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):

        password = request.POST['new_password']
        email = request.session['email']
        
        if not email:
            user = User.objects.get(email=email)
            user.password = password
            # hash the password, and update user in database
            user.set_password(user.password)
            user.save()
            return redirect("/journal/home")
        return HttpResponse("There is no nothing to update")
    

        
    


    















    
