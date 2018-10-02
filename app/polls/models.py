from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('게시일자') #게시일자는 사람이 읽는 설명; 안써도되지만 쓰는걸 권장


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
