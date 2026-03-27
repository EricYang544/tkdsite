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


class NoticeImage(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE, related_name='images', verbose_name='공지사항')
    image = models.ImageField(upload_to='notice/', verbose_name='사진')

    class Meta:
        verbose_name = '공지 사진'

    def __str__(self):
        return f'{self.notice.title} 사진'


class Activity(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    is_new = models.BooleanField(default=True, verbose_name='NEW 표시')

    class Meta:
        verbose_name = '활동 소식'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='images', verbose_name='활동 보고')
    image = models.ImageField(upload_to='activity/', verbose_name='사진')

    class Meta:
        verbose_name = '활동 사진'

    def __str__(self):
        return f'{self.activity.title} 사진'


class Gallery(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    image = models.ImageField(upload_to='gallery/', verbose_name='사진')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '갤러리'
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title


class Member(models.Model):
    ROLE_CHOICES = [
        ('1_President', '회장'),
        ('2_Vice', '부회장'),
        ('3_Secretary', '총무'),
        ('4_PR Manager', '홍보부장'),
        ('5_Coach', '훈련부장'),
    ]
    BELT_CHOICES = [
        ('1', '1단'),
        ('2', '2단'),
        ('3', '3단'),
        ('4', '4단'),
        ('5', '5단'),
    ]

    name = models.CharField(max_length=50, verbose_name='이름')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='1_President', verbose_name='직책')
    generation = models.PositiveIntegerField(verbose_name='기수')
    belt = models.CharField(max_length=10, choices=BELT_CHOICES, blank=True, verbose_name='단수')
    department = models.CharField(max_length=100, verbose_name='학과')
    photo = models.ImageField(upload_to='members/', blank=True, verbose_name='사진')
    intro = models.TextField(blank=True, verbose_name='한마디')

    class Meta:
        verbose_name = '임원진'
        ordering = ['role', 'name']

    def __str__(self):
        return f'{self.name} ({self.get_role_display()})'