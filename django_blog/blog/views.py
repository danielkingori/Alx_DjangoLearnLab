from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .models import Post, Comment
from .forms import CustomUserCreationForm, PostForm, CommentForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form .is_valid():
            user = form.save()
            role = form.cleaned_data.get("role")
            if role == "creator":
                creator_group = Group.objects.get(name="creator")
                user.groups.add(creator_group)
            elif role == "reader":
                creator_group = Group.objects.get(name="reader")
                user.groups.add(creator_group)
            login(request, user)
            return redirect("ListView")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form":form})


def ListView(request):
    posts = Post.objects.all()
    return render(request, "blog/posts.html", {"posts":posts})


def DetailView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post.html", {"post":post})



@login_required
@permission_required("blog.create",raise_exception=True)
def CreateView(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.author = request.user
            posts.save()
            return redirect("ListView")
    else:
        form = PostForm()
    return render(request, "blog/create_post.html",{"form":form})
@login_required
@permission_required("blog.edit",raise_exception=True)
def UpdateView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("ListView")
    else:
        form = PostForm(instance=post)
    return render(request, "blog/edit_post.html", {"form":form})
@login_required
@permission_required("blog.delete",raise_exception=True)
def DeleteView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("ListView")
    return render(request, "blog/delete_post.html",{"post":post})



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can edit the post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can delete the post
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.post.get_absolute_url()

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.post.get_absolute_url()
  
