from django.shortcuts import render, redirect, reverse
from .models import ExternalLink, Image, Hint, Question, Location, StartingInstance, QuestionInstance, PaveMember, Profile, ExtraPageAbout
from .tokens import activate_account_token
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login, authenticate, logout, tokens
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode, urlencode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
# Create your views here.
def signup_view(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            currentSite = get_current_site(request)
            subject = 'Activate Account'
            message = render_to_string('activate_account_email.html', {
                'user': user,
                'domain': currentSite.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': activate_account_token.make_token(user),
            })
            cleaned_email = form.cleaned_data.get('email')
            email = EmailMessage(subject, message, to=[cleaned_email])
            try:
                email.send()
                return redirect('activate_account_sent')
            except:
                try:
                    send_mail(subject, message, 'pavescavengerhunt@gmail.com', [cleaned_email,])
                    return redirect('activate_account_sent')
                except:
                    user.is_active = True
                    user.save()
                    return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


def activate_view(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist): # User.ObjectDoesNotExist?
        user = None

    if user is not None and activate_account_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, "Link is invalid")

def activate_account_sent_view(request):
    return render(request, "activate_account_sent.html")

def activate_account_invalid_view(request):
    return render(request, "activate_account_invalid.html")

def home_view(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html', {})

def start_view(request):

    starting_location = StartingInstance.objects.get().location

    context = {
        'starting_location': starting_location,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'starting.html', context=context)

def scavengerhunt_view(request):

    user_instance = Profile.objects.get(user=request.user)

    if 'answer' in request.POST:
        question_answered = QuestionInstance.objects.get(pk=request.POST['questionno'])
        if question_answered.question.answer.lower() == request.POST['answer'].lower():
            user_instance.questions_completed.add(question_answered)
            user_instance.save()

    questions_answered = user_instance.questions_completed.all().count()
    to_show = questions_answered+1 if questions_answered < QuestionInstance.objects.all().count() else questions_answered
    available = QuestionInstance.objects.all().order_by('question_number')[:to_show] #thought: could index by a parameter to limit
    paginator = Paginator(available, 1)
    if 'page' in request.GET:
        page_obj = paginator.get_page(request.GET['page'])
    else:
        page_obj = paginator.get_page(paginator.num_pages)

    return render(request, 'questions.html', {'page_obj': page_obj, 'answered': questions_answered})

def extras_view(request):
    extras = ExternalLink.objects.all()
    about = ExtraPageAbout.objects.get()
    return render(request, 'extras.html', {'extras': extras, 'aboutExtras': about})

def about_view(request):
    members = PaveMember.objects.all()
    return render(request, 'about.html', {'members': members})

def completed_view(request):
    return render(request, 'completed.html', {})