from django.contrib.auth.hashers import check_password
from django.shortcuts import render,redirect,get_object_or_404
from Application.templatetags import get_dict
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

from random import sample,randint
from django.core.paginator import Paginator

from .models import NewUser
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method=='POST':
        f_name=request.POST['full-name']
        e_mail=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        if NewUser.objects.filter(username=username):
            messages.warning(request,"Username Already exists!!")
            return render(request,'signup.html')
        if NewUser.objects.filter(email=e_mail):
            messages.warning(request,'Email already registred')
            return render(request,'signup.html')
        else:
            newuser=NewUser.objects.create_user(username=username,email=e_mail,password=password,first_name=f_name.strip())
            newuser.save()
            messages.success(request,"You Account has been succesfully created")
            return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Bad Credential!')
            return redirect('signin')
    return render(request,'loginpage.html')

@login_required
def signout(request):
    logout(request)
    messages.success(request,'You are successfully logout')
    return redirect('signin')

@login_required
def user_profile(request):
    user=request.user
    mcq_questions=McqQuestion.objects.filter(user=user)
    subjective_question=SubjectiveQuestion.objects.filter(user=user)
    context={
        'user':user,
        'mcq_questions':mcq_questions,
        'subjective_question':subjective_question
    }
    return render(request,'profilepage.html',context)

@login_required
def homepage(request):
    mcqquestions=McqQuestion.objects.all().order_by('-id').values()[:15]
    all_subjective_questions=SubjectiveQuestion.objects.all().order_by('-id').values()[:15]
    context={
        'mcqquestions':mcqquestions,
        'subjectiveQuestion':all_subjective_questions
    }
    return render(request,'homepage.html',context)

# mcq parts
@login_required
def allmcq(request):
    topics=McqTopic.objects.all()    
    p=Paginator(McqQuestion.objects.all().order_by('-id'),15)
    page=request.GET.get('page')
    questions=p.get_page(page)
    context={
        'topics':topics,
        'questions':questions,
    }
    return render(request,'allmcq.html',context)

@login_required
def topicmcq(request,topic_id):
    p=Paginator(McqQuestion.objects.filter(mcq_topic_id=topic_id).order_by('-id'),15)
    page=request.GET.get('page')
    questions=p.get_page(page)
    topics=McqTopic.objects.all()
    topic_names=McqTopic.objects.filter(id=topic_id)
    topic_name=''
    for name in topic_names:
        topic_name=name
    context={
        'topics':topics,
        'questions':questions,
        'topic_name':topic_name
    }
    return render(request,'topicMCQ.html',context)

# Subjective Parts
@login_required
def subjective_questions(request):
    p=Paginator(SubjectiveQuestion.objects.all().order_by('-id'),15)
    page=request.GET.get('page')
    questions=p.get_page(page)
    subj_topics=SubjectiveTopic.objects.all()
    context={
        'questions':questions,
        'topics':subj_topics
    }
    return render(request,'allsubjectiveQue.html',context)

@login_required
def topicsubjective(request,topic_id):
    p=Paginator(SubjectiveQuestion.objects.filter(topic_id=topic_id).order_by('-id'),15)
    page=request.GET.get('page')
    questions=p.get_page(page)
    subj_topics=SubjectiveTopic.objects.all()
    topic_names=SubjectiveTopic.objects.filter(id=topic_id)
    topic_name=''
    for name in topic_names:
        topic_name=name
    context={
        'questions':questions,
        'topics':subj_topics,
        'topic_name':topic_name
    }
    return render(request,'topicSubjQuestion.html',context)

@login_required
def one_subjective_que(request,question_id):
    subj_topics=SubjectiveTopic.objects.all()
    questionquery=SubjectiveQuestion.objects.filter(id=question_id)
    comments=Question_Comment.objects.filter(sub_question_id=question_id,parent=None)
    replies=Question_Comment.objects.filter(sub_question_id=question_id).exclude(parent=None)
    question=''
    for q in questionquery:
        question=q
    
    replyDict={}
    for reply in replies:
        if reply.parent.id not in replyDict.keys():
            replyDict[reply.parent.id]=[reply]
        else:
            replyDict[reply.parent.id].append(reply)
    context={
        'topics':subj_topics,
        'question':question,
        'comments':comments,
        'replyDict':replyDict
    }
    return render(request,'OneSubjectiveQue.html',context)


@login_required
def post_comment(request):
    if request.method=='POST':
        user=request.user
        questionId=request.POST.get("questionID")
        sub_question=SubjectiveQuestion.objects.get(id=questionId)
        comment_text=request.POST.get('comment')
        commentID=request.POST.get('commentID')
        if commentID=="":
            comment=Question_Comment(user=user,comment=comment_text,sub_question=sub_question)
        else:
            parent=Question_Comment.objects.get(id=commentID)
            comment=Question_Comment(user=user,comment=comment_text,sub_question=sub_question,parent=parent)
        comment.save()
    return redirect(f'/SubjectiveQue/{sub_question.id}')

@login_required
def like_post(request,id):
    comment=get_object_or_404(Question_Comment,id=request.POST.get('comment_id'))
    
    question=Question_Comment.objects.filter(sub_question=comment.sub_question)[0]
    question_id=SubjectiveQuestion.objects.get(subjective_question=question)
    comment.likes.add(request.user)
    return HttpResponseRedirect(reverse('selected_subjective_que',args=[str(question_id.id)]))

@login_required
def unlike_post(request,id):
    comment=get_object_or_404(Question_Comment,id=request.POST.get('comment_id'))
    
    question=Question_Comment.objects.filter(sub_question=comment.sub_question)[0]
    question_id=SubjectiveQuestion.objects.get(subjective_question=question)
    comment.likes.remove(request.user)
    return HttpResponseRedirect(reverse('selected_subjective_que',args=[str(question_id.id)]))


@login_required
def delete_mcq_question(request,question_id):
    question=McqQuestion.objects.get(id=question_id)
    question.delete()
    return redirect('profile')

@login_required
def delete_subj_question(request,question_id):
    question=SubjectiveQuestion.objects.get(id=question_id)
    question.delete()
    return redirect('profile')

@login_required
def searching(request):
    searched_data=""
    if request.method=='POST':
        searched_data=request.POST.get('searched_data')
    mcq_topics=McqTopic.objects.filter(mcq_topic__icontains=searched_data).order_by('id')
    subjective_topics=SubjectiveTopic.objects.filter(subj_topic__icontains=searched_data).order_by('id')
    mcq_questions=McqQuestion.objects.filter(mcq_question__icontains=searched_data).order_by('id')
    subjective_questions=SubjectiveQuestion.objects.filter(subj_question__icontains=searched_data).order_by('id')
    context={
        'keyword':searched_data,
        'mcq_topics':mcq_topics,
        'subjective_topics':subjective_topics,
        'mcq_questions':mcq_questions,
        'subjective_questions':subjective_questions
    }
    return render(request,'searched.html',context)

# adding questions
# add subjective question
@login_required
def add_subjective_topic(request):
    current_user=request.user
    if request.method=='POST':
        topic=request.POST.get('topic')
        user_num_topic=current_user.user_subj_topic.all()
        if len(user_num_topic)>4:
            messages.error(request,'Cannot Add More, Already Added To The Limit')
            return redirect('profile')
        if SubjectiveTopic.objects.filter(subj_topic=topic):
            messages.error(request,'Topic Already Added')
            return redirect('add_subjective_question')
        else:
            new_topic=SubjectiveTopic.objects.create(user=current_user,subj_topic=topic)
            new_topic.save()
    return redirect('add_subjective_question')

@login_required
def add_subjective_question(request):
    subjective_topics=SubjectiveTopic.objects.all()
    context={
        'subjective_topics':subjective_topics
    }
    current_user=request.user
    if request.method=='POST':
        topic=request.POST.get('subtopic')
        question=request.POST.get('subjectivequestion')
        user_Allquestions=current_user.user_subj_question.all()
        if len(user_Allquestions)>4:
            messages.info(request,'Cannot Add More, Already Added To The Limit')
            return redirect('profile')
        if SubjectiveQuestion.objects.filter(subj_question=question):
            messages.error(request,'Question Already Added')
            return redirect('profile')
        else:
            topic_id=SubjectiveTopic.objects.filter(subj_topic=topic)[0]
            new_sub_que=SubjectiveQuestion.objects.create(user=current_user,topic_id=topic_id.id,subj_question=question)
            new_sub_que.save()
            return redirect('profile')
    return render(request,'add_subj_question.html',context)

# add mcq question
@login_required
def add_mcq_topic(request):
    current_user=request.user
    if request.method=='POST':
        topic=request.POST.get('topic')
        user_Alltopic=current_user.user_mcq_topic.all()
        if len(user_Alltopic)>4:
            messages.error(request,'Cannot Add More, Already Added To The Limit')
            return redirect('profile')
        if McqTopic.objects.filter(mcq_topic=topic):
            messages.error(request,'Topic Already Added')
            return redirect('add_mcq_question')
        else:
            new_topic=McqTopic.objects.create(user=current_user,mcq_topic=topic)
            new_topic.save()
            return redirect('add_mcq_question')

@login_required
def add_mcq_question(request):
    mcq_topics=McqTopic.objects.all()
    mcq_questions=McqQuestion.objects.all()
    context={
        'mcq_topics':mcq_topics,
        'mcq_questions':mcq_questions
    }
    curr_user=request.user
    if request.method=='POST':
        topic=request.POST.get('topic')
        question=request.POST.get('mcqquestion')
        user_Allmcq=curr_user.user_mcq_question.all()
        if len(user_Allmcq)>4:
            messages.error(request,'Cannot Add More, Already Added To The Limit')
            return redirect('profile')
        if McqQuestion.objects.filter(mcq_question=question):
            messages.error(request,'Question Already Added')
            return redirect('profile')
        else:
            topic_id=McqTopic.objects.filter(mcq_topic=topic)[0]
            new_mcq_que=McqQuestion.objects.create(user=curr_user,mcq_topic_id=topic_id.id,mcq_question=question)
            new_mcq_que.save()
            return redirect('add_mcq_question')
    return render(request,'add_mcq_question.html',context)

@login_required
def add_mcq_option(request):
    if request.method=='POST':
        question=request.POST.get('question')
        option=request.POST.get('mcqqueOption')      
        ques_id=McqQuestion.objects.filter(mcq_question=question)[0]        
        allquestionOption=QuestionOption.objects.filter(mcq_question_id=ques_id.id)
        if QuestionOption.objects.filter(mcq_question_id=ques_id.id,option=option):
            messages.error(request,'Option Already Added for this Question')
            return redirect('add_mcq_question')
        if len(allquestionOption)>6:
            messages.error(request,'Cannot Add More, Already Added To The Limit, Need to add Correct Option')
            return redirect('add_mcq_question')
        new_option=QuestionOption.objects.create(mcq_question_id=ques_id.id,option=option)
        is_correctopt=request.POST.get('iscrrt')  
        if is_correctopt:
            new_option.is_correct=is_correctopt
        new_option.save()
        return redirect('add_mcq_question')

@login_required
def update_profile(request):
    curr_user=request.user
    prof=curr_user.profession
    context={
        'user':curr_user,
        'prof':prof
    }
    if request.method=='POST':
        f_name=request.POST['fullname']
        phn_number=request.POST['number']
        profession=request.POST.get('prof')
        confirm_pass=request.POST.get('confirm_password')
        address=request.POST.get('address')
        if check_password(confirm_pass,curr_user.password):       
            updateuser=NewUser.objects.get(id=curr_user.id)
            updateuser.first_name=f_name            
            updateuser.mobile_number=phn_number
            updateuser.profession=profession
            updateuser.address=address
            if request.POST['DOB']:
                updateuser.date_of_birth=request.POST['DOB']
            if request.POST.get('password'):
                updateuser.set_password=request.POST.get('password')
            if len(request.FILES)!=0:
                updateuser.photo=request.FILES['profilepic']
            updateuser.save()
            messages.success(request,"Profile Updated")
            return redirect('profile')
        else:
            messages.warning(request,'old Password Not Matched')
            return redirect('updateProfile')
    return render(request,'updateprofile.html',context)


# mcq test part
# selection topic for test
@login_required
def select_topic(request):
    topics=McqTopic.objects.all()
    context={
        'topics':topics
    }
    if request.method=='POST':
        topic=request.POST.get('topic')
        return redirect('test',topic_id=topic)
    return render(request,'select_test_topic.html',context)

@login_required
def starttest(request,topic_id):
    questions=McqQuestion.objects.filter(mcq_topic_id=topic_id)
    try:
        questions=sample(list(questions),10)
    except:
        questions=sample(list(questions),randint(1,len(list(questions))))
    if request.method=='POST':
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            select_opt=request.POST.get(q.mcq_question)
            options=QuestionOption.objects.filter(mcq_question=q)
            is_crrt=''
            for opt in options:
                if opt.is_correct:
                    is_crrt=opt
            if str(is_crrt)==str(select_opt):
                correct+=1
            else:
                wrong+=1
        try:
            percent = (correct/len(questions))*100
        except:
            percent=0
        context = {
            'time': request.POST.get('timer')[7:],
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'result.html',context)
    context={
        'questions':questions,
        'topic_id':topic_id
    }
    return render(request,'testpage.html',context)

def contactUs(request):
    user=request.user
    context={
        'user':user
    }
    if request.method=="POST":
        message=request.POST.get('message')
        username=request.POST.get('username')
        mobile_number=request.POST.get('number')
        email=request.POST.get('email')
        newmsg=Contact(user=user,mobile_number=mobile_number,username=username,email=email,message=message)
        newmsg.save()
        messages.success(request,'Message Sent')
        return redirect('profile')
    return render(request,'contactus.html',context)