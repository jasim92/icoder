from django.shortcuts import render, redirect
from .models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.
def blogHome(request):
    allPost = Post.objects.all()
    context = {'allPost':allPost}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context = {'post':post, 'comments':comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, 'blog/blogPost.html',context)

def postComments(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comments = BlogComment(comment=comment, user=user, post=post)
            comments.save()
            messages.success(request, 'Your Comment has been posted Successfully')
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comments = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comments.save()
            messages.success(request, 'Your reply has been posted Successfully')
                  
        
    return redirect(f"/blog/{post.slug}")
        

