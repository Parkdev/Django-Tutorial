import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('게시일자') #게시일자는 사람이 읽는 설명; 안써도되지만 쓰는걸 권장

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """
        최근에 게시되었는지 여부를 리턴

        자신의 게시일자 >= 지금 - 하루
        :return:  24시간이 지나지않았으면 참, 지났으면 거짓
        """
        now = timezone.now()
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1) #참 or 거짓을 리턴
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text