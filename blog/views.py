# _*_ coding:utf-8 _*_

from django.shortcuts import render,HttpResponse,redirect,reverse,HttpResponseRedirect
from django.views import View
from .forms import *
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate,login


class ProView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            if request.method.lower()=='post':
                for k,v in request.POST.items():
                    if v=='submit':
                        handler = getattr(self, k, self.http_method_not_allowed)
                    else:
                        handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class LoginView(View):
    def get(self,request):
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        return render(request,'login.html')

    def post(self,request):
        username=request.POST.get('username',None)
        password=request.POST.get('password',None)
        try:
            user=authenticate(request,username=username,password=password)
        except:
            user=None
        if user is not None:
            login(request,user)
            request.session['is_login'] = True
            request.session['user_id'] = str(user.id)
            request.session['user_name'] = str(user)
            return HttpResponseRedirect(request.session['login_from'])
        else:
            return HttpResponse(u'密码不对或者不存在')


def pageGenerate(fullList,pagenum,urltype,type,currpage):
    pageObj=Paginator(fullList,pagenum)
    totalPage=pageObj.num_pages
    pageitems=pageObj.page(currpage).object_list
    #上下页标签
    if pageObj.page(currpage).has_next():
        next_page=currpage+1
    else:
        next_page=0
    if pageObj.page(currpage).has_previous():
        previous_page=currpage-1
    else:
        previous_page=0

    #数字页,前后各2页
    pageresult=[]
    link={-2:currpage-2,-1:currpage-1,0:currpage,1:totalPage-currpage-1,2:totalPage-currpage-2}
    for k,v in link.items():
        if v>0:
            pageresult.append(currpage+k)

    if pageresult[0]==2:
        pageresult=[1]+pageresult
    elif pageresult[0]>2:
        pageresult=[1,0]+pageresult
    if pageresult[len(pageresult)-1]+1==totalPage:
        pageresult=pageresult+[totalPage]
    elif pageresult[len(pageresult)-1]+1<totalPage:
        pageresult = pageresult + [0,totalPage]

    pagerelease={'pageitems':pageitems,'urltype':urltype,'type':type,'currpage':currpage,'previous_page':previous_page,'pageresult':pageresult,'next_page':next_page}
    return pagerelease


class ArticleView(ProView):
    # @method_decorator(login_required(login_url='login/'))
    def get(self,request,id):
        obj=ArticleSheet.objects.get(id=id)
        comments=CommentSheet.objects.filter(article_id=id)
        return render(request, 'article.html', {'obj':obj, 'comments':comments})

    # @method_decorator(login_required(login_url='login/'))
    def CommentBotton(self,request,id):
        data={
            'comment':request.POST.get('comment'),
            'article':id,
        }
        obj=CommentForm(data)
        if obj.is_valid():
            obj.save()
            obj = ArticleSheet.objects.get(id=id)
            comments = CommentSheet.objects.filter(article_id=id)
            return render(request, 'article.html', {'obj': obj, 'comments': comments})
        return HttpResponse('comment failed')


class PostView(View):
    def get(self,request):
        obj = PostForm()
        return render(request, 'post.html', {'obj':obj})

    # @method_decorator(login_required(login_url='login/'))
    def post(self,request):
        TagSheet.objects.get_or_create(tag=request.POST.get('tag'))
        data={
            'title':request.POST.get('title'),
            'content':request.POST.get('content'),
            'tag':request.POST.get('tag'),
            'type':request.POST.get('type'),
        }
        obj=PostForm(data)
        if obj.is_valid():
            obj.save()
            return HttpResponse('successful')
        else:
            TagSheet.objects.filter(tag=request.POST.get('tag')).delete()
            return HttpResponse('failed')


class ListView(View):
    # @method_decorator(login_required(login_url='login/'))
    def get(self,request,urltype,type,page):
        articles = ArticleSheet.objects.filter(type=type)
        return render(request,'list.html',pageGenerate(articles,10,urltype,type,page))


class IndexView(View):
    def get(self,request):
        types=TypeSheet.objects.all()
        tags=TagSheet.objects.all()
        articles=ArticleSheet.objects.all()[:20]
        context={
            'types':types,
            'tags':tags,
            'articles':articles,
        }
        return render(request, 'index.html', context)


