from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Leaders
from user.models import Player
from quiz.forms import UserAnswer
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def not_logged_in(user):
    return not user.is_authenticated


def base(request):
    return render(request, 'home/base.html')


def home(request):
    return render(request, 'home/home.html')


def hello(request):
    return render(request, 'home/hello.html')


@user_passes_test(not_logged_in, login_url='/user/dashboard', redirect_field_name=None)
def login(request):
    return render(request, 'home/login.html')


def rules(request):
    return render(request, 'home/rule.html')


def page(request):
    "Only After 1st Round is complete"

    p = get_object_or_404(Leaders, pk=1)
    n = p.playerNum
    lst = [0, 1, 2]
    form = UserAnswer

    if request.method == 'GET':
        # print(n)
        j = 1
        leaders = Player.objects.order_by(
            '-score', 'last_submit')[:n]

        email_list = []

        for i in leaders:
            i.rank = j
            j += 1
            i.save()

            email_list.append(i.email)

        print(email_list)
        return render(request, 'home/page.html', {"n": n, "leaders": leaders, "form": form, "lst": lst[0]})

    if request.method == "POST":    # if the admin submits the passcode
        my_form = UserAnswer(request.POST)

        if my_form.is_valid():
            ans = my_form.cleaned_data.get("answer")
            organs = "AlohaMoraHarryPotter"

            

            # correct answer
            if (str(organs) == str(ans)):   # if the answer is correct
                leaders = Player.objects.order_by(
                    '-score', 'last_submit')[:n]
                for x in leaders:
                    x.level2 = 0           
                    
                    x.save()
                    print(x.name)

                    with open('text_messages/login_user.txt', 'r') as file:
                        data_email = file.read()

                    send_mail(
                            'Signup Sucessfull',
                            str(data_email).format(x.user.first_name , x.user.first_name , 
                            x.user.last_name , x.user.username ),
                            'ieeesbnitd@gmail.com',
                            [x.email],
                            fail_silently=True,
                            )



                return render(request, 'home/page.html', {"n": n, "leaders": leaders, "form": form, "lst": lst[1]})

            # incorrect answer
            else:   # returns the same page
                leaders = Player.objects.order_by(
                    '-score', 'last_submit')[:n]
                return render(request, 'home/page.html', {"n": n, "leaders": leaders, "form": form, "lst": lst[2]})
        else:
            return HttpResponse('<h2> Your Form Data was Invalid </h2>')


def error_404(request, exception):
        data = {}
        return render(request,'home/404.html', data)



