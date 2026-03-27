from django.contrib import admin
from .models import Notice, Activity, Gallery, Member, NoticeImage, ActivityImage

class NoticeImageInline(admin.TabularInline):
    model = NoticeImage
    extra = 3

class ActivityImageInline(admin.TabularInline):
    model = ActivityImage
    extra = 3

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_new', 'created_at']
    list_filter = ['is_new']
    inlines = [NoticeImageInline]

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_new', 'created_at']
    list_filter = ['is_new']
    inlines = [ActivityImageInline]

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'generation', 'role', 'belt', 'department']
    list_filter = ['role', 'belt']