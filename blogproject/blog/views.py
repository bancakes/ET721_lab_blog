from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.
def index(request):
    return render(request, 'index.html')
# listview to get all blog posts 
def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
# detail
def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog/post_detail.html', {'post' : post})
# create a new post 
def post_create(request):
    if request.method == 'POST':  
        form = BlogPostForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('post_list') 
    else:
        form = BlogPostForm() 

    return render(request, 'blog/post_form.html', {'form': form})  
# View/edit existing blog post
def post_edit(request, id):
    post = get_object_or_404(BlogPost, id=id)  
    if request.method == 'POST':  
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():  
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form, 'post': post})
