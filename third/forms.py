from django.forms import ModelForm
from django import forms
from third.models import Restaurant,Review
from django.utils.translation import gettext_lazy as _

REVIEW_POINT_CHOICES=(('1',1),('2',2),('3',3),('4',4),('5',5))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'comment', 'restaurant']
        labels = {
            'point': _('평점'),
            'comment': _('코멘트'),
        }
        widgets = {
            'restaurant': forms.HiddenInput(),  # 리뷰를 달 식당 정보는 사용자에게 보여지지 않도록 합니다.
            'point': forms.Select(choices=REVIEW_POINT_CHOICES)  # 선택지를 인자로 전달합니다.
        }




class RestaurantForm(ModelForm):
    class Meta:
        model=Restaurant
        fields=['name','address' ,'image', 'password']
        labels={
            'name':_('이름'),
            'address':_('주소'),
            'image':_('이미지 url'),
            'password':_('게시물 비밀번호')
        }

        widgets={ 'password': forms.PasswordInput() }

class UpdateRestaurantForm(RestaurantForm):
    class Meta:
        model=Restaurant
        exclude=['password']

