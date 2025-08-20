from django.contrib import admin
from issues.models import Issue


class IssueAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "title",
        "editor",
    ]


admin.site.register(Issue, IssueAdmin)
