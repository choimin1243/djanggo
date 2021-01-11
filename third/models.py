from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name=models.CharField(max_length=30,default='')
    address=models.CharField(max_length=20,null=True)
    password=models.CharField(max_length=20, default=None, null=True)
    image=models.CharField(max_length=500,default=None, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)  # 글 작성 시 (이 모델의 데이터(레코드) 저장 시) 생성 시각
    updated_at = models.DateTimeField(auto_now=True)

