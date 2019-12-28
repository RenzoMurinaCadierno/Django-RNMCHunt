from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):

    # User is signing up
    if request.method == 'POST':

        # Check if the passwords match
        if request.POST['password1'] == request.POST['password2']:

            try:
                # Check on the DB for any username with the same name
                user = User.objects.get(
                    username=request.POST['username']
                )

                return render(
                    request,
                    'accounts/signup.html',
                    {'error': 'Username not available.'}
                )

            # if User.objects.get() fails to retrieve a user with that
            # name, an exception will rise. Catch it and create the user
            except User.DoesNotExist:

                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )

                # login the newly signed up user
                auth.login(request, user)

                # and redirect them to home
                return redirect('home')

        # Passwords did not match
        else:

            return render(
                request,
                'accounts/signup.html',
                {'error': 'Passwords must match.'}
            )

    else:
        # GET request, user wants to sign up.
        return render(request, 'accounts/signup.html')

def login(request):

    # If the user is trying to log in
    if request.method == 'POST':

        # try to authenticate them
        user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password1']
        )

        # if authentication returned a valid user (user and pass OK)
        if user is not None:

            # log them in
            auth.login(request, user)

            # redirect them to home
            return redirect('home')

        # authentication failed
        else:

            # render login.html with a display message
            return render(
                request,
                'accounts/login.html',
                {'error': 'Username or password are incorrect.'}
            )

    # User requested on GET, deliver login.html
    else:

        return render(request, 'accounts/login.html')

def logout(request):

    # We NEED to ensure the user is requesting logout as a POST,
    # since on reload, some browsers auto-trigger all GET requests,
    # eventually logging out the user.
    if request.method == 'POST':

        # logout the user
        auth.logout(request)

        # redirect the logged out user to home
        return redirect('home')
