from django.contrib.gis.db import models  # 使用 GeoDjango 的模型类
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.PointField(null=True, blank=True)  # 用于存储用户地理位置

    def __str__(self):
        return self.user.username
