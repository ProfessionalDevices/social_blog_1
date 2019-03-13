from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Review
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"     #<app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"     #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class UserReviewListView(ListView):
    model = Review
    template_name = "blog/user_reviews.html"     #<app>/<model>_<viewtype>.html
    context_object_name = 'reviews'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Review.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    context_object_name = "post"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    context_object_name = "post"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = "post"
    success_url = '/'

    def test_func(self):
        post =self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title', 'content']
    context_object_name = "review"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ReviewListView(ListView):
    model = Review
    template_name = "blog/review_list.html"     #<app>/<model>_<viewtype>.html
    context_object_name = "reviews"
    ordering = ['-date_posted']
    paginate_by = 5

class ReviewDetailView(DetailView):
    model = Review
    context_object_name = "review"

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    context_object_name = "review"
    success_url = '/'

    def test_func(self):
        post =self.get_object()
        if self.request.user == review.author:
            return True
        else:
            return False

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['title', 'content']
    context_object_name = "review"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review =self.get_object()
        if self.request.user == review.author:
            return True
        else:
            return False

class ReviewLastView(ListView):
    model = Review
    template_name = "blog/review_last.html"     #<app>/<model>_<viewtype>.html
    context_object_name = "reviews"
    ordering = ['-date_posted']
    paginate_by = 1

def about(request):
    return render(request, 'blog/about.html')

def search(request):
    if "q" in request.GET:
        querystring = request.GET.get("q")
        print(querystring)
        if len(querystring) == 0:
            return redirect("/search/")
        reviews = Review.objects.filter(content__icontains=querystring)
        posts = Post.objects.filter(content__icontains=querystring)
        users = User.objects.filter(username__icontains=querystring)
        context = {"reviews": reviews, "posts": posts, "users": users}
        return render(request, 'blog/search.html', context)
    else:
        return render(request, 'blog/search.html')
