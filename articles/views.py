from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from articles.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "articles/article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"


class ArticleCreateView(CreateView):
    model = Article
    template_name = "articles/article_new.html"
    fields = (
        "title",
        "subtitle",
        "body",
        "issue",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "articles/article_edit.html"
    fields = (
        "title",
        "subtitle",
        "body",
        "issue",
    )


class ArticleDeleteView(DetailView):
    model = Article
    template_name = "articles/article_delete.html"
