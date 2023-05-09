from django.http import HttpResponse
from django.shortcuts import redirect, render, resolve_url
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q, Count
from .models import Member, Board, Comment, Champion, Skill, Rune, Vote, Video

# Create your views here.
def home(request):
    signin_ok_user = request.session.get('signin_ok_user')
    contents = Board.objects.annotate(comment_count=Count('board_comment')).order_by('-rdate').values()
    champions = Champion.objects.all().order_by('?').values()
    videos = Video.objects.all().order_by('-id').values()

    paginator = Paginator(contents, '5')
    paginator2 = Paginator(champions, '8')
    paginator3 = Paginator(videos, '3')

    page = int(request.GET.get('page', '1'))
    page_obj = paginator.get_page(page)
    page_obj2 = paginator2.get_page(page)
    page_obj3 = paginator3.get_page(page)
    context = {
        'signin_ok_user': signin_ok_user,
        'page_obj': page_obj,
        'page_obj2': page_obj2,
        'page_obj3': page_obj3,
    }
    return render(request, 'home.html', context)

def signin(request):
    return render(request, 'signin.html')

def signin_ok(request):
    email = request.POST['email']
    pwd = request.POST['pwd']
    try:
        res_data={}
        user = Member.objects.filter(email=email).values()
        user_pwd=user[0]['pwd']
        user_nname=user[0]['nname']
        if user_pwd == pwd:
            request.session['signin_ok_user'] = user_nname
            return redirect('../home')
        else:
            res_data['errormsg']="비밀번호가 틀렸습니다."
            return render(request, 'signin.html',res_data)
    except:
        res_data['errormsg'] = "일치하는 이메일이 없습니다."
        return render(request, 'signin.html', res_data)

def verify_pwd (request):
    return render(request, 'verify_pwd.html')

def verify_pwd_ok(request):
    signin_ok_user = request.session.get('signin_ok_user')
    res_data = {}
    member = Member.objects.get(nname=signin_ok_user)
    pwd = request.POST['pwd']
    if member.pwd == pwd:
        return render(request, 'update_myinfo.html')
    else:
        res_data['check_ok'] = "가입한 비번과 일치하지않습니다"
        return render(request, 'verify_pwd.html', res_data)

def update_ok(request):
    res_data={}
    signin_ok_user = request.session.get('signin_ok_user')
    pwd = request.session.get('pwd')
    member = Member.objects.get(nname=signin_ok_user)
    phone = request.POST['phone']
    pwd1 = request.POST['pwd1']
    pwd2 = request.POST['pwd2']
    member.phone = phone
    if pwd1 == pwd2:
        member.pwd = pwd1
        member.save()
        return redirect('bang:home')
    else:
        res_data['error']='두 비밀번호가 일치하지 않습니다'
        return render(request, 'update_myinfo.html', res_data)



def idfind(request):
    return render(request, 'idfind.html')

def idfind_ok(request):
    name = request.POST['name']
    phone = request.POST['phone']
    try:
        res_data = {}
        member = Member.objects.get(name=name)
        if member is not None:
            if member.phone == phone:  # 이 멤버가 존재할때 해당 이메일과 이름이 동일한지 체크 후 있다면 리턴
                res_data['check_ok'] = '가입하신 이메일은 ' + member.email + ' 입니다.'
                return render(request, 'idfind.html', res_data)
            else:
                res_data['check_ok'] = "가입하신 정보와 휴대폰번호가 일치하지않습니다."
                return render(request, 'idfind.html', res_data)
    except:
        res_data['check_ok'] = "가입이력이 없습니다."
        return render(request, 'idfind.html', res_data)


def pwfind(request):
    return render(request, 'pwfind.html')


def pwfind_ok(request):
    email = request.POST['email']
    name = request.POST['name']
    phone = request.POST['phone']
    try:
        res_data = {}
        member = Member.objects.filter(email=email).values()
        member_name = member[0]['name']
        member_phone = member[0]['phone']
        if member is not None:
            if member_name == name:
                if member_phone == phone:
                    member_email = member[0]['email']
                    request.session['pwfind_ok_member'] = member_email
                    return render(request, 'pwfind_ok.html')
                else:
                    res_data['check_ok'] = "가입하신 정보와 휴대폰번호가 일치하지않습니다."
                    return render(request, 'pwfind.html', res_data)
            else:
                res_data['check_ok'] = "가입하신 정보와 이름이 일치하지않습니다."
                return render(request, 'pwfind.html', res_data)
    except:
        res_data['check_ok'] = "가입이력이 없습니다."
        return render(request, 'pwfind.html', res_data)


def pwfind_submit(request):
    pwfind_member = request.session.get('pwfind_ok_member')
    member = Member.objects.get(email=pwfind_member)
    pwd = request.POST['pwd']
    member.pwd = pwd
    member.save()
    del (request.session['pwfind_ok_member'])
    print("변경완료")
    return redirect('./signin/')

def profile(request):
    signin_ok_user = request.session.get('signin_ok_user')
    contents = Board.objects.filter(nname=signin_ok_user).count()
    comments = Comment.objects.filter(user_id=signin_ok_user).count()
    context = {
        'signin_ok_user':signin_ok_user,
        'contents':contents,
        'comments':comments,
    }
    return render(request, 'profile.html', context)

def signout(request):
    if request.session.get('signin_ok_user'):
        del(request.session['signin_ok_user'])
    return redirect('bang:home')

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render({},request))


def signup_ok(request):
    name = request.POST['name']
    nname = request.POST['nname']
    pwd = request.POST['pwd']
    email = request.POST['email']
    phone1 = request.POST['phone1']
    phone2 = request.POST['phone2']
    phone3 = request.POST['phone3']
    member_nname = Member.objects.filter(nname=nname).count()
    member_email = Member.objects.filter(email=email).count()

    res_data = {}
    if member_nname is int(1):
        res_data['errormsg1'] = "이미 존재하는 닉네임입니다"
        return render(request, 'signup.html', res_data)

    if member_email is int(1):
        res_data['errormsg2'] = "이미 존재하는 이메일입니다"
        return render(request, 'signup.html', res_data)

    phone = (str(phone1 + phone2 + phone3))
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    member = Member(name=name, nname=nname, pwd=pwd, email=email, phone=phone, rdate=nowDatetime)
    member.save()
    return redirect("bang:home")

def board(request):
    signin_ok_user = request.session.get('signin_ok_user')
    contents=Board.objects.annotate(comment_count=Count('board_comment')).order_by('-rdate').values()
    paginator = Paginator(contents, '20')
    page = int(request.GET.get('page', '1'))
    page_obj = paginator.get_page(page)
    context = {
        'signin_ok_user':signin_ok_user,
        'page_obj':page_obj,
    }
    return render(request, 'board.html', context)


def order(request):
    signin_ok_user = request.session.get('signin_ok_user')
    order = request.GET.get('order', '')
    if order=='rank':
        contents=Board.objects.annotate(comment_count=Count('board_comment')).order_by('-lookup').values()
        paginator = Paginator(contents, '20')
        page = int(request.GET.get('page', '1'))
        page_obj = paginator.get_page(page)

        context = {
            'signin_ok_user': signin_ok_user,
            'page_obj': page_obj,
            'page':page,
            'order':order,
        }
        return render(request, 'order.html', context)
    elif order=='new':
        contents=Board.objects.annotate(comment_count=Count('board_comment')).order_by('-rdate').values()
        paginator = Paginator(contents, '20')
        page = int(request.GET.get('page', '1'))
        page_obj = paginator.get_page(page)
        context = {
            'signin_ok_user': signin_ok_user,
            'page_obj': page_obj,
            'page':page,
            'order':order,
        }
        return render(request, 'order.html', context)

    elif order=='vote':
        contents=Board.objects.annotate(comment_count=Count('board_comment')).order_by('-like').values()
        paginator = Paginator(contents, '20')
        page = int(request.GET.get('page', '1'))
        page_obj = paginator.get_page(page)
        context = {
            'signin_ok_user': signin_ok_user,
            'page_obj': page_obj,
            'page':page,
            'order':order,
        }
        return render(request, 'order.html', context)


def boardcategory(request, ccode):
    signin_ok_user = request.session.get('signin_ok_user')
    board = Board.objects.filter(ccode=ccode).annotate(comment_count=Count('board_comment')).order_by('-id').values()
    paginator = Paginator(board, '20')
    page = request.GET.get('page', '1')
    page_obj = paginator.get_page(page)
    if board:
        order = request.GET.get('order', '')
        if order:
            context=orderInCategory(request, order, ccode)
            return render(request, 'boardbycategory.html', context)
        else:
            ccode = board[0]['ccode']
            context = {
                'signin_ok_user': signin_ok_user,
                'page_obj': page_obj,
                'ccode': ccode,
            }
            return render(request, 'boardbycategory.html', context)
    else:
        return redirect('bang:boardbycategory')

def orderInCategory(request, order, ccode):
    signin_ok_user = request.session.get('signin_ok_user')
    if order == 'rank':
        contents = Board.objects.filter(ccode=ccode).annotate(comment_count=Count('board_comment')).order_by('-lookup').values()
        paginator = Paginator(contents, '20')
        page = int(request.GET.get('page', '1'))
        page_obj = paginator.get_page(page)
        comments = Comment.objects.all().order_by('-board_id').values()
        context = {
            'signin_ok_user': signin_ok_user,
            'page_obj': page_obj,
            'page': page,
            'order': order,
            'ccode':ccode,
        }
        return context
    elif order == 'new':
        contents = Board.objects.filter(ccode=ccode).annotate(comment_count=Count('board_comment')).order_by('-rdate').values()
        paginator = Paginator(contents, '20')
        page = int(request.GET.get('page', '1'))
        page_obj = paginator.get_page(page)
        comments = Comment.objects.all().order_by('-board_id').values()
        context = {
            'signin_ok_user': signin_ok_user,
            'page_obj': page_obj,
            'page': page,
            'order': order,
            'ccode': ccode,
        }
        return context

    elif order == 'vote':
        contents = Board.objects.filter(ccode=ccode).annotate(comment_count=Count('board_comment')).order_by('-like').values()
        paginator = Paginator(contents, '20')
        page = int(request.GET.get('page', '1'))
        page_obj = paginator.get_page(page)
        comments = Comment.objects.all().order_by('-board_id').values()
        context = {
            'signin_ok_user': signin_ok_user,
            'page_obj': page_obj,
            'page': page,
            'order': order,
            'ccode': ccode,
        }
        return context

def search(request):
    query = request.GET.get('q', '')
    kw = request.GET.get('kw', '')
    if kw:
        if query == "all":
            context = searchForAll(request, kw, query)
            return render(request, 'query.html', context)
        elif query == "title":
            context = searchForTitle(request, kw, query)
            return render(request, 'query.html', context)
        elif query == "author":
            context = searchForAuthor(request, kw, query)
            return render(request, 'query.html', context)
        elif query == "titleAndContent":
            context = searchForTitleOrContent(request, kw, query)
            return render(request, 'query.html', context)
        elif query == "content":
            context = searchForContent(request, kw, query)
            return render(request, 'query.html', context)
    else:
        return redirect('bang:board')



def searchForAll(request, kw, query):
    signin_ok_user = request.session.get('signin_ok_user')
    board = Board.objects.all().order_by('-id').values()
    q = board.filter(
        Q(title__icontains=kw) | Q(content__icontains=kw) | Q(nname__icontains=kw))
    q = tagFilter(q)
    paginator = Paginator(q, '10')
    page = int(request.GET.get('page', '1'))
    page_obj = paginator.get_page(page)
    if (len(q) != 0):
        context = {
            'signin_ok_user':signin_ok_user,
            'page_obj':page_obj,
            'page':page,
            'kw':kw,
            'query':query,
        }
        return context
import re
def tagFilter(q):
    clean = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    for i in range(len(q)):
        q[i]['content'] = re.sub(clean, "", q[i]['content'])

    #clean_board = re.sub(clean,"",board[i]['content'])
    #cleanBoard.append(clean_board)
    return q

def searchForTitle(request, kw, query):
    signin_ok_user = request.session.get('signin_ok_user')
    board = Board.objects.all().order_by('-id').values()
    q = board.filter(
        Q(title__icontains=kw)).values()
    q = tagFilter(q)
    paginator = Paginator(q, '10')
    page = int(request.GET.get('page', '1'))
    page_obj = paginator.get_page(page)
    if (len(q) != 0):
        context = {
            'signin_ok_user': signin_ok_user,
            'page_obj': page_obj,
            'page': page,
            'kw': kw,
            'query': query,
        }
        return context

def searchForAuthor(request, kw, query):
    signin_ok_user = request.session.get('signin_ok_user')
    board = Board.objects.all().order_by('-id').values()
    q = board.filter(Q(
            nname__icontains=kw)).values()
    q = tagFilter(q)
    paginator = Paginator(q, '10')
    page = int(request.GET.get('page', '1'))
    page_obj = paginator.get_page(page)
    if (len(q) != 0):
        context = {
            'signin_ok_user': signin_ok_user,
            'page_obj': page_obj,
            'page':page,
            'kw':kw,
            'query': query,
        }
        return context

def searchForTitleOrContent(request, kw, query):
    signin_ok_user = request.session.get('signin_ok_user')
    board = Board.objects.all().order_by('-id').values()
    q = board.filter(
        Q(title__icontains=kw) | Q(content__icontains=kw)).values()
    q = tagFilter(q)
    paginator = Paginator(q, '10')
    page = int(request.GET.get('page', '1'))
    page_obj = paginator.get_page(page)
    if (len(q) != 0):
        context = {
            'signin_ok_user': signin_ok_user,
            'page_obj': page_obj,
            'page':page,
            'kw':kw,
            'query': query,
        }
        return context

def searchForContent(request, kw, query):
    signin_ok_user = request.session.get('signin_ok_user')
    board = Board.objects.all().order_by('-id').values()
    q = board.filter(
        Q(content__icontains=kw)).values()
    q = tagFilter(q)
    paginator = Paginator(q, '10')
    page = int(request.GET.get('page', '1'))
    page_obj = paginator.get_page(page)
    if (len(q) != 0):
        context = {
            'signin_ok_user': signin_ok_user,
            'page_obj': page_obj,
            'page':page,
            'kw':kw,
            'query': query,
        }
        return context

def detail(request, id):
    hit = 1
    board = Board.objects.get(id=id)
    board.lookup += hit
    board.save()
    signin_ok_user = request.session.get('signin_ok_user')
    board=  Board.objects.filter(id=id).values()
    id = board[0]['id']
    title = board[0]['title']
    nname = board[0]['nname']
    contents = board[0]['content']
    lookup = board[0]['lookup']
    like= board[0]['like']
    ccode = board[0]['ccode']
    rdate = board[0]['rdate']
    comments = Comment.objects.filter(board_id=id).order_by('created_at').values()
    vote = Vote.objects.filter(voter=signin_ok_user, board=id).values()
    if vote:
        vote = vote[0]
        context= {
            'id': id,
            'signin_ok_user':signin_ok_user,
            'title' : title,
            'nname' : nname,
            'contents' : contents,
            'lookup' : lookup,
            'like' : like,
            'ccode': ccode,
            'rdate': rdate,
            'comments':comments,
            'vote':vote,
        }
        return render(request, 'detail.html', context)
    else:
        context = {
            'id': id,
            'signin_ok_user': signin_ok_user,
            'title': title,
            'nname': nname,
            'contents': contents,
            'lookup': lookup,
            'like': like,
            'ccode': ccode,
            'rdate': rdate,
            'comments': comments,
        }
        return render(request, 'detail.html', context)

def like(request, id):
    thumbsup = 1
    like = request.POST.getlist('like')
    signin_ok_user = request.session.get('signin_ok_user')
    board = Board.objects.get(id=id)
    if like :
        voter = Member.objects.get(nname=signin_ok_user)
        board.like += thumbsup
        board.save()
        vote = Vote(board=board, voter=voter)
        vote.save()
        return redirect('bang:detail', board.id)
    else:
        return redirect('bang:detail', board.id)

from flask import url_for
def comments_create(request,id):
    if request.session.get('signin_ok_user'):
        board =  Board.objects.get(id=id)
        comment_form = request.POST.get('comment')
        if comment_form:
            user = request.session.get('signin_ok_user')
            nname = Member.objects.get(nname=user)
            comment = Comment(comment=comment_form, board=board, user= nname)
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('bang:detail', id=board.id), comment.user_id))
    return redirect('/bang/League_of_Legends/signin')



def comments_delete(request, id, comment_id):
    signin_ok_user= request.session.get('signin_ok_user')
    if signin_ok_user:
        comment = Comment.objects.get(id=comment_id)
        board = Board.objects.get(id=id)
        user = Member.objects.get(nname=signin_ok_user)
        if user == comment.user:
            comment.delete()
    return redirect('{}#comment_{}'.format(resolve_url('bang:detail', id=board.id), comment.user_id))

def write(request):
    return render(request, 'write.html')

def write_ok(request):
    try:
        ccode = request.POST['board-catetory-name']
        title = request.POST['title']
        contents = request.POST['contents']
        signin_ok_user = request.session.get('signin_ok_user')
        nname= Member.objects.get(nname=signin_ok_user)
        nowDateTime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        board = Board(title=title, content=contents, nname=signin_ok_user, rdate=nowDateTime, ccode=ccode, member=nname)
        board.save()
        return redirect('bang:board')
    except:
        res_data={}
        res_data['error']='게시판을 선택해주세요'
        return render(request, 'write.html', res_data)

def articleDelete(request, id):
    signin_ok_user = request.session.get('signin_ok_user')
    nname = Member.objects.get(nname=signin_ok_user)
    board = Board.objects.filter(id=id, nname=nname)
    board.delete()
    return redirect('bang:board')

def articleUpdate(request, id):
    board = Board.objects.get(id=id)
    board.content = request.POST['contents']
    nowDateTime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    board.rdate = nowDateTime
    board.save()
    return redirect('bang:detail', id)

from .championsdata import ChampionsData
import csv
from .models import Champion
def get_champ_data():
    with open('/Users/yhlee/Dropbox/MyJava/Project/6th/bangproject/bang/champions.csv', 'r') as db:
        reader = csv.reader(db)
        list=[]
        for row in reader:
            list.append(Champion(
                name=row[0],
                nname=row[1],
                role=row[2],
                loc=row[3],
                health=row[4],
                recover=row[5],
                attack=row[6],
                defence=row[7],
                resist=row[8],
                aspeed=row[9],
                mspeed=row[10],
            ))
    Champion.objects.bulk_create(list)

def champion(request):
    champions = Champion.objects.all().values()
    context = {
        'champions':champions,
    }
    return render(request, 'champion.html', context)

def ch_details(request, name):
    champions = Champion.objects.all().values()
    champion = Champion.objects.filter(name=name).all().values()
    champ = champion[0]
    context = {
        'champions':champions,
        'champ':champ,
    }
    return render(request, 'ch_details.html', context)

def map(request):
    return render(request, 'map.html')

def howling_abys(request):
    return render(request, 'Howling_Abyss.html')

def summoners_rift(request):
    return render(request, 'Summoners_Rift.html')


def spell(request):
    return render(request, 'spell.html')

def rune(request):
    return render(request, 'rune.html')

def videos(request):
    signin_ok_user = request.session.get('signin_ok_user')
    contents = Video.objects.all().order_by('-id').values()
    paginator = Paginator(contents, '100')
    page = int(request.GET.get('page','1'))
    page_obj = paginator.get_page(page)
    context = {
        'signin_ok_user':signin_ok_user,
        'page_obj':page_obj,
    }
    return render(request, 'videos.html', context)
