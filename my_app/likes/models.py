from django.db import models

# Create your models here.
class LikeCount(models.Model):
    content_type = models.ForeignKey('account_app.weibo', on_delete=models.CASCADE, null=True)
    liked_num = models.IntegerField(default=0)

class LikeRecord(models.Model):
    user = models.ForeignKey('account_app.MyUser', on_delete=models.CASCADE, null=False)
    content_type = models.ForeignKey('account_app.weibo', on_delete=models.CASCADE, null=True)
    liked_time = models.DateTimeField(auto_now_add=True)