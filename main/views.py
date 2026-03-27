from django.shortcuts import render
from board.models import Notice, Activity, Member

def index(request):
    notices = Notice.objects.all()[:5]
    activities = Activity.objects.all()[:5]
    return render(request, 'main/index.html', {
        'notices': notices,
        'activities': activities,
    })

def about(request):
    members = Member.objects.all()
    return render(request, 'main/about.html', {
        'members': members,
    })