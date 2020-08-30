from django.shortcuts import render
from django.utils import timezone
from .models import Post, CVItem
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CVForm, NewCVForm
from django.shortcuts import redirect


# Create your views here.
def home_page(request):
    return render(request, 'blog/home_page.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else: 
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def show_cv(request):
    cv = CVItem.objects.all()
    return render(request, 'blog/show_cv.html', {'cv': cv})

def edit_cv(request, pk):
    CVItem.objects.get(pk=pk)
    cv_section = get_object_or_404(CVItem, pk=pk)
    if request.method == "POST":
        form = CVForm(request.POST, instance=cv_section)
        if form.is_valid():
            cv_section = form.save(commit=False)
            cv_section.save()
            return redirect('show_cv')
    else:
        form = CVForm(instance=cv_section)
    return render(request, 'blog/edit_cv.html', {'form' : form, 'cv_section' : cv_section})

def add_cv(request):
    if request.method == "POST":
        form = NewCVForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('show_cv')
    else: 
        form = NewCVForm()
    return render(request, 'blog/add_cv.html', {'form': form})
