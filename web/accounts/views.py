from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import opinion
from django.utils.timezone import now
from rest_framework import viewsets, permissions
from .serializer import *
# Create your views here.

@login_required # Redirects to login page if user is not logged in.
def home(request):
    return render(request, 'accounts/home.html')

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        u = form.save()
        login(request, u)
        context['opinion'] = opinion.objects.all().order_by('posted_date_time')
        return render(request, 'accounts/home.html', context)
    context['form'] = form
    return render(request, 'registration/signup.html', context)

def post_opinion(request):
    posted_by = request.user
    comment = request.POST['comment']
    post = opinion.objects.create(posted_by=posted_by, comment=comment, posted_date_time=now())
    return redirect(request, 'accounts/home.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerilizer
    permission_classes = [permissions.IsAuthenticated]

class OpinionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Opinions to be viewed or edited.
    """
    queryset = opinion.objects.all().order_by('posted_date_time')
    serializer_class = OpinionSerilizer