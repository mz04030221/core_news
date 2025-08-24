from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from issues.models import Issue
from articles.models import Article


class IssueListView(ListView):
    model = Issue
    template_name = "issue/issue_list.html"


class IssueDetailView(DetailView):
    model = Issue
    template_name = "issues/issue_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.filter(issue__pk=self.kwargs["pk"])
        return context


class IssueUpdateView(UpdateView):
    model = Issue
    fields = (
        "title",
        "edition",
    )
    template_name = "issues/issue_edit.html"


class IssueDeleteView(DeleteView):
    model = Issue
    template_name = "issues/issue_delete.html"
    success_url = reverse_lazy("issue_list")


class IssueCreateView(CreateView):
    model = Issue
    template_name = "issues/issue_new.html"
    fields = (
        "title",
        "edition",
    )

    def form_valid(self, form):
        form.instance.editor = self.request.user
        return super().form_valid(form)
