from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# -------------------------
# LOGIN / SIGNUP
# -------------------------
def loginsignuppage(request):
    mode = request.GET.get('mode', 'login')

    if request.method == "POST" and "login_submit" in request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "✅ Logged in successfully!")
            next_url = request.GET.get("next", None)
            if not next_url:
                next_url = "soildata:dashboard"
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")
            mode = "login"

    elif request.method == "POST" and "signup_submit" in request.POST:
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        location = request.POST.get("location")
        agree_terms = request.POST.get("agreeTerms")

        if not agree_terms:
            messages.error(request, "You must agree to Terms & Privacy Policy!")
            mode = "signup"
        elif password1 != password2:
            messages.error(request, "Passwords do not match!")
            mode = "signup"
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            mode = "signup"
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=full_name
            )
            UserProfile.objects.create(
                user=user,
                phone_number=phone_number,
                location=location
            )
            messages.success(request, "Account created! Please log in.")
            return redirect("account:login")

    elif request.method == "POST" and "forgot_submit" in request.POST:
        email = request.POST.get("forgot_email")
        try:
            user = User.objects.get(email=email)
            messages.success(request, "Password reset link sent to your email!")
        except User.DoesNotExist:
            messages.error(request, "No account found with this email.")
        mode = "login"

    return render(request, "login_signup.html", {"mode": mode})

#=======================
#terms and views
#=======================
def terms_privacy(request):
    return render(request, "terms_privacy.html")


# -------------------------
# LOGOUT
# -------------------------
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("account:login")

