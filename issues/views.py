from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from issues.models import Issue
from issues.forms import IssueForm
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


class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = "issues/issue_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.editor == self.request.user


class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issue
    template_name = "issues/issue_delete.html"
    success_url = reverse_lazy("issue_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm
    template_name = "issues/issue_new.html"

    def form_valid(self, form):
        form.instance.editor = self.request.user
        return super().form_valid(form)
