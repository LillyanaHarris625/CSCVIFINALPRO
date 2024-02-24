from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
#from Cacti.models import CustomUser

# Create your views here.
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        # address = request.POST['address']
        # address_2 = request.POST['address_2']
        # city = request.POST['city']
        # state = request.POST['state']
        # zip = request.POST['zip']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists ')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name) #, address=address, city=city, state=state, zip=zip
                #user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, address=address, city=city, state=state, zip=zip)
                user.set_password(password)
                user.is_staff=True
                user.save()
                print("Success")
                return redirect('login_user')

    else:
        print("this is not post method")
        return render(request, "register.html")

def login_user(request):
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']

        user = auth.authenticate(username=username, password=password)
        #user = CustomUser.objects.get(username=username)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username of Password')
            return redirect('login_user')

    else:
        return render(request,"login.html")

def logout_user(request):
    auth.logout(request)
    return redirect('home') #Redirect to the home page