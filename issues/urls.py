from django.urls import path
from issues.views import (
    IssueListView,
    IssueDetailView,
    IssueCreateView,
    IssueUpdateView,
    IssueDeleteView,
)

urlpatterns = [
    path("<int:pk>/", IssueDetailView.as_view(), name="issue_detail"),
    path("<int:pk>/edit/", IssueUpdateView.as_view(), name="issue_edit"),
    path("<int:pk>/delete/", IssueDeleteView.as_view(), name="issue_delete"),
    path("new/", IssueCreateView.as_view(), name="issue_new"),
    path("", IssueListView.as_view(), name="issue_list"),
]
