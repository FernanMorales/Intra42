from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from models import *
from intra.views import get_ctx
from django.template import RequestContext


def main(request):
    user_ctx = get_ctx(request)
    forums = Category.objects.all()
    return render_to_response("list.html", dict(forums=forums, user=request.user, user_is_logged_in=user_ctx),
                              context_instance = RequestContext(request))


def sub_category(request, c_name):
    cid = Category.objects.filter(title=c_name)
    sc = SubCategory.objects.filter(c_id=cid)
    return render_to_response("subcategorys.html", add_csrf(request, sc=sc, c_name=c_name))


def thread(request, c_name, sc_name):
    cid = Category.objects.filter(title=c_name)
    sc = SubCategory.objects.filter(c_id=cid)
    threads = Thread.objects.filter(sc_id=sc)

    return render_to_response("threads.html", add_csrf(request, sc=sc_name, threads=threads, c=c_name))

def post(request, c_name, sc_name, t_name):
    thread = Thread.objects.filter(title=t_name)
    posts = Post.objects.filter(thread=thread)
    comments = Comment.objects.filter(post=posts)
    return render_to_response("posts.html", add_csrf(request, c=c_name, sc=sc_name, t=t_name, posts=posts,
                                                          comments=comments))

def reply(request, c_name, sc_name, t_name):
    body = request.POST.get("body")
    creator = request.user
    t = Thread.objects.get(title=t_name)
    post = Post(creator=creator, body=body, thread=t)
    post.save()
    url = "/forum/" + c_name + '/' + sc_name + '/' + t_name
    return HttpResponseRedirect(url)

def create(request, c, sc):
    return render_to_response("create.html", add_csrf(request, c=c, sc=sc))

def create_thread(request, c_name, sc_name):
    body = request.POST.get("body")
    title = request.POST.get("title")
    creator = request.user
    sc = SubCategory.objects.get(title=sc_name)
    thread = Thread(sc_id=sc, title=title, creator=creator)
    thread.save()
    t = Thread.objects.get(title=title)
    post = Post(creator=creator, body=body, thread=t)
    post.save()
    url = "/forum/" + c_name + '/' + sc_name + '/' + t.title
    return HttpResponseRedirect(url)

def add_csrf(request, **kwargs):
    user_ctx = get_ctx(request)
    d = dict(user_is_logged_in=user_ctx, **kwargs)
    d.update(csrf(request))
    return d
