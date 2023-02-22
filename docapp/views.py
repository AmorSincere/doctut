from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from docapp.models import CustomUser, Tutorials, Subjects, Contents

from docapp.services import gen_code


def index(request):
    generated_code = gen_code()
    return render(request, 'index.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if request.user.is_authenticated and not CustomUser.objects.filter(author=request.user):
                custom_user = CustomUser(author=request.user, generated_code=gen_code())
                custom_user.save()
            messages.success(request, "Registration successful.")
            return redirect("docapp:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                messages.info(request, f"You are now logged in as {username}.")
                return redirect("docapp:index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("docapp:index")


# ANOTHER VIEWS THAN AUTH
@login_required
def create_tutorial_page(request):
    try:
        tutorials = Tutorials.objects.all().filter(user=CustomUser.objects.get(author=request.user))
    except:
        tutorials = 'yoq'
    return render(request, 'tutorial_create.html', {"tutorials": tutorials, "envy": "envy"})


@login_required
def create_tutorial(request):
    if request.method == "POST":
        try:
            tutorial_name = request.POST.get('tutorial_name')
            custom_user = CustomUser.objects.get(author=request.user)
            generated_code = gen_code()
            tutorial = Tutorials(tutorial_name=tutorial_name, generated_code=generated_code, user=custom_user)
            tutorial.save()
        except Exception as error:
            print(error.__str__())
        return redirect("docapp:create_tutorial_page")


@login_required
def subject_create_page(request, generated_code):
    try:
        subjects = Subjects.objects.all().filter(tutorial=Tutorials.objects.get(generated_code=generated_code))
    except Exception as error:
        print(error.__str__())
        subjects = 'yoq'
    return render(request, "subject_create_page.html", {"generated_code": generated_code, "subjects": subjects})


@login_required
def subject_create(request, generated_code):
    try:
        subjects = Subjects.objects.all().filter(tutorial=Tutorials.objects.get(generated_code=generated_code))
    except Exception as error:
        print(error.__str__())
        subjects = 'yoq'
    try:
        if request.method == "POST":
            subject_name = request.POST.get('subject_name')
            generated_code1 = gen_code()
            subject = Subjects(tutorial=Tutorials.objects.get(generated_code=generated_code), subject_name=subject_name,
                               generated_code=generated_code1)
            subject.save()
    except Exception as error:
        print(error.__str__())

    return render(request, "subject_create_page.html", {"generated_code": generated_code, "subjects": subjects})


@login_required
def content_create_page(request, generated_code):
    try:
        contents = Contents.objects.all().filter(subject=Subjects.objects.get(generated_code=generated_code))
    except Exception as error:
        print(error.__str__())
        contents = 'yoq'
    return render(request, "content_create_page.html", {"generated_code": generated_code, "contents": contents})


@login_required
def content_create(request, generated_code):
    try:
        contents = Contents.objects.all().filter(subject=Subjects.objects.get(generated_code=generated_code))
    except Exception as error:
        print(error.__str__())
        contents = 'yoq'
    try:
        if request.method == "POST":
            content = request.POST.get('content')
            content = Contents(subject=Subjects.objects.get(generated_code=generated_code), content=content)
            content.save()
            print(content)
    except Exception as error:
        print(error.__str__())

    return render(request, "content_create_page.html", {"generated_code": generated_code, "contents": contents})


def tutorials(request, generated_code):
    tutorial = Tutorials.objects.get(generated_code=generated_code)
    subjects = Subjects.objects.all().filter(tutorial=tutorial)
    return render(request, 'tutorials.html', {"tutorial": tutorial, "subjects": subjects})


def tutorials_active(request, generated_code_tut, generated_code_subject):
    tutorial = Tutorials.objects.get(generated_code=generated_code_tut)
    if generated_code_subject == "envy":
        subjects = Subjects.objects.all().filter(tutorial=tutorial)
        contents = Contents.objects.all().filter(subject=Subjects.objects.all().filter(tutorial=tutorial)[0])
        return render(request, 'tutorials_active.html',
                      {"tutorial": tutorial, "subjects": subjects, "contents": contents})
    else:
        subjects = Subjects.objects.all().filter(tutorial=tutorial)
        contents = Contents.objects.all().filter(subject=Subjects.objects.get(generated_code=generated_code_subject))
        return render(request, 'tutorials_active.html',
                      {"tutorial": tutorial, "subjects": subjects, "contents": contents})
