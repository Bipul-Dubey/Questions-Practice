from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
# Create your models here.

P_CHOICES = [('Student','Student'),('Professional','Professional')]
class NewUser(AbstractUser):
    mobile_number=models.CharField(max_length=10,blank=True,null=True)
    photo=models.ImageField(verbose_name='Photo',upload_to='photos/',default='photos/default_pic.png')
    date_of_birth=models.DateField(verbose_name='Date of Birth',blank=True,null=True)
    profession=models.CharField(choices=P_CHOICES,max_length=15,blank=True,null=True)
    address=models.TextField(blank=True,null=True)

class McqTopic(models.Model):
    user=models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name='user_mcq_topic',null=True)
    mcq_topic=models.CharField(max_length=100)

    def __str__(self):
        return self.mcq_topic

class McqQuestion(models.Model):
    user=models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name='user_mcq_question')
    mcq_topic=models.ForeignKey(McqTopic,on_delete=models.CASCADE,related_name='mcq_topic_question')
    mcq_question=models.TextField()

    def __str__(self):
        return self.mcq_question

class QuestionOption(models.Model):
    mcq_question=models.ForeignKey(McqQuestion,on_delete=models.CASCADE,related_name='mcq_question_optn')
    option=models.TextField()
    is_correct=models.BooleanField(default=False)

    def __str__(self):
        return self.option


# subjective part
class SubjectiveTopic(models.Model):
    user=models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name="user_subj_topic",null=True)
    subj_topic=models.CharField(max_length=100)

    def __str__(self):
        return self.subj_topic

class SubjectiveQuestion(models.Model):
    user=models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name='user_subj_question')
    topic=models.ForeignKey(SubjectiveTopic,on_delete=models.CASCADE,related_name='subjective_topic')
    subj_question=models.TextField()

    def __str__(self):
        return self.subj_question

class Question_Comment(models.Model):
    user=models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name='user_ques_comment')
    sub_question=models.ForeignKey(SubjectiveQuestion,on_delete=models.CASCADE,related_name='subjective_question')

    comment=models.TextField()
    parent=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    timestamp=models.DateTimeField(default=now)

    likes=models.ManyToManyField(NewUser,related_name='comment_post')

    def __str__(self):
        return self.comment

class Contact(models.Model):
    user=models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name='user_contacts',blank=True, null=True)
    
    mobile_number=models.CharField(max_length=10,blank=True,null=True)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

    message=models.TextField()

    def __str__(self):
        return self.username+" "+(self.message[:7])+"..."

