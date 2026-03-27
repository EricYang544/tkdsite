from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    is_new = models.BooleanField(default=True, verbose_name='NEW 표시')

    class Meta:
        verbose_name = '공지사항'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Activity(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    class Meta:
        verbose_name = '활동 소식'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    image = models.ImageField(upload_to='gallery/', verbose_name='사진')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '갤러리'

    def __str__(self):
        return self.title


class Member(models.Model):
    ROLE_CHOICES = [
    ('President', '회장'),
    ('Vice', '부회장'),
    ('Secretary', '총무'),
    ('PR Manager', '홍보부장'),
    ('Coach', '훈련부장'),
    ]
    
    BELT_CHOICES = [
        ('1', '1단'),
        ('2', '2단'),
        ('3', '3단'),
        ('4', '4단'),
        ('5', '5단'),
    ]

    name = models.CharField(max_length=50, verbose_name='이름')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member', verbose_name='직책')
    belt = models.CharField(max_length=10, choices=BELT_CHOICES, blank=True, verbose_name='단수')
    department = models.CharField(max_length=100, verbose_name='학과')
    photo = models.ImageField(upload_to='members/', blank=True, verbose_name='사진')
    intro = models.TextField(blank=True, verbose_name='한마디')

    class Meta:
        verbose_name = '부원'
        ordering = ['role', 'name']

    def __str__(self):
        return f'{self.name} ({self.get_role_display()})'