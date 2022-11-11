from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.signin,name='signin'),
    path('signup/',views.signup,name='register'),
    path('signout/',views.signout,name='signout'),
    path('Profile/',views.user_profile,name='profile'),
    path('home/',views.homepage,name='home'),
    path('MCQ/',views.allmcq,name='allmcq'),
    path('MCQ/<topic_id>',views.topicmcq,name='topicmcq'),
    path('Subjective/',views.subjective_questions,name='subjective'),
    path('Subjective/<topic_id>',views.topicsubjective,name='topicsubjective'),
    path('SubjectiveQue/<question_id>',views.one_subjective_que,name='selected_subjective_que'),
    # delete question
    path('delete_mcq/<question_id>',views.delete_mcq_question,name='delete_mcq_ques'),
    path('delete_subj/<question_id>',views.delete_subj_question,name='delete_subj_ques'),

    # api for post comments
    path('postComment/',views.post_comment,name='post_comment'),
    # comment likes
    path('likes/<id>',views.like_post,name='like_post'),
    path('unlikes/<id>',views.unlike_post,name='unlike_post'),
    # searching
    path('seaching/',views.searching,name='searching'),

    # adding questions
    # subjective
    path('addSubjectivetopic/',views.add_subjective_topic,name='add_subjective_topic'),
    path('addSubjectiveQuestion/',views.add_subjective_question,name='add_subjective_question'),

    # mcq
    path('addMcqTopic/',views.add_mcq_topic,name='add_mcq_topic'),
    path('addMcqQuestion/',views.add_mcq_question,name='add_mcq_question'),
    path('addMcqQuestionOption/',views.add_mcq_option,name='add_mcq_option'),

    # update profile
    path('update-profile/',views.update_profile,name="updateProfile"),

    # test
    path('test-topic/',views.select_topic,name="select-topic"),
    path('test/<topic_id>',views.starttest,name="test"),

    path('contact/',views.contactUs,name="contact"),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
