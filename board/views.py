from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Notice, Activity, Gallery, Member

def notice_list(request):
    notice_all = Notice.objects.all()
    paginator = Paginator(notice_all, 10)  # 한 페이지에 10개
    page = request.GET.get('page')
    notices = paginator.get_page(page)
    return render(request, 'board/notice_list.html', {'notices': notices})

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'board/notice_detail.html', {'notice': notice})

def activity_list(request):
    activity_all = Activity.objects.all()
    paginator = Paginator(activity_all, 5)  # 한 페이지에 5개
    page = request.GET.get('page')
    activities = paginator.get_page(page)
    return render(request, 'board/activity_list.html', {'activities': activities})

def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'board/activity_detail.html', {'activity': activity})

def gallery_list(request):
    photo_list = Gallery.objects.all()
    paginator = Paginator(photo_list, 6)
    page = request.GET.get('page')
    photos = paginator.get_page(page)
    return render(request, 'board/gallery_list.html', {'photos': photos})

def member_list(request):
    members = Member.objects.all()
    return render(request, 'board/member_list.html', {'members': members})