from django.views.generic import TemplateView

from issues.models import Issue
from articles.models import Article


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context["latest_daily_issue"] = self.get_latest_issue("DAILY")
        context["latest_weekly_issue"] = self.get_latest_issue("WEEKLY")
        context["latest_monthly_issue"] = self.get_latest_issue("MONTHLY")
        return context

    def get_latest_issue(self, edition):
        issues = Issue.objects.filter(edition=edition).order_by("pk").reverse()
        if issues.exists():
            latest_issue = issues[0]
        else:
            return {}

        articles = Article.objects.filter(issue=latest_issue).order_by("pk").reverse()
        latest_articles = articles[:3] if len(articles) >= 4 else articles

        return {
            "issue": latest_issue,
            "articles": latest_articles,
        }


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class ProfilePageView(TemplateView):
    template_name = "pages/profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        context["articles"] = Article.objects.filter(author=self.request.user)
        return context
