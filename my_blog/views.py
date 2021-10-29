from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from taggit.models import Tag
from .models import Post, Comment
from .forms import CommentForm, SearchForm

# Create your views here.
# def list_view(request): 
#     posts = Post.objects.all()

#     return render(request, 'my_blog/list_view.html', {'posts': posts})
class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'my_blog/list_view.html'

    

def detail_view(request, year, month, day, post): 
    post = get_object_or_404(Post, slug = post, status = 'published', publish__year = year, publish__month = month, publish__day = day)
    comments = post.comments.filter(active = True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = post
            new_comment.save()
    else:
        views = post.get_view_count()
        post.increment_view_count()
        comment_form = CommentForm()
    return render(request, 'my_blog/detail_view.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form, 'view_count': views})

def search_view(request): 
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body')
            search_query = SearchQuery(query)
            results = Post.objects.annotate(search = search_vector, rank = SearchRank(search_vector, search_query)).filter(search = search_query).order_by('-rank')
    return render(request, 'my_blog/search_view.html', {'form': form, 'query': query, 'results': results})