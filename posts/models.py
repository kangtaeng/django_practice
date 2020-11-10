from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='posts', null=True)
    created_at = models.DateTimeField()
    liked_users = models.ManyToManyField(User, related_name='liked_posts')

# __str__ : 인스턴스 출력시 데이터의 주소가 아닌 원하는 값이 나오게 함
    def __str__(self):
        if self.user:
            return f'{self.user.get_username()}: {self.body}'

        return f'{self.body}'
