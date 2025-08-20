from django.contrib import admin
from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "subtitle",
        "author",
        "issue",
    ]


admin.site.register(Article, ArticleAdmin)
