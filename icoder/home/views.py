from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# from icoder.blog.models import Post
# Create your views here.3



def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        if len(name)<2 or len(email)<5 or len(phone)<10 or len(msg)<5:
            messages.error(request, 'Please Fill Form Correctly')   #dissmissal message framwork of django
        else:
            contact = Contact(name = name, email = email, phone = phone, msg = msg)
            contact.save()
            messages.success(request, 'Your Message has been Sent. Thank You!')

    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allPost = Post.objects.none() #this line make empty query set, it better than empty list which throw error
    else:
        allPostTitle = Post.objects.filter(title__icontains=query)
        allPostContent = Post.objects.filter(content__icontains=query)
        allPost = allPostTitle.union(allPostContent) #union can merge two query into one
    context = {'allPost':allPost, 'query':query}
    return render(request, 'home/search.html', context)

def handleSignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        #check verify sign field
        if len(username) > 10:
            messages.error(request, 'User name must not more than 10 characters')
            return redirect('/')
        if not username.isalnum():
            messages.error(request, 'User name must contain alpha numeric characters')
            return redirect('/')
        if pass1 != pass2:
            messages.error(request, 'Password did not match')
            return redirect('/')
        #create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'You account has been Successfully created')
        return redirect('/')
    else:
        return HttpResponse('404 not found')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')
        user = authenticate(request, username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, 'Your are sucessfully logged in')
            return redirect('/')
        else:
            messages.error(request, 'Wrong Credential, try again')
            return redirect('/')
    else: 
        return HttpResponse('handle login')
def handleLogout(request):
    logout(request)
    messages.success(request, 'Sucessfully Log out')
    return redirect('/')





    

        
