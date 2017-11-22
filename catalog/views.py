from django.shortcuts import render

# Create your views here.

from .models import Post, Author, BlogComment
from django.contrib.auth.models import User


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_posts = Post.objects.all().count()
    # Available books (status = 'a')
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_posts': num_posts, 'num_authors': num_authors},
    )


from django.views import generic
from django.shortcuts import get_object_or_404


class PostListView(generic.ListView):
    model = Post
    paginate_by = 1


class PostDetailView(generic.DetailView):
    model = Post


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login.
    """
    model = BlogComment
    fields = ['content', ]

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        form.instance.author = self.request.user
        # Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Post, pk=self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk'], })