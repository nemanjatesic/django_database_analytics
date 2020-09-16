from .models import User, Post, Comment
from django.views.generic import TemplateView
from django.shortcuts import render


def home(request):
    return render(request, 'djangoIspit/home.html')


class UserChartView(TemplateView):
    template_name = 'djangoIspit/userChart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_from = self.request.GET.get('from', '')
        date_to = self.request.GET.get('to', '')
        date_from = date_from[0:10] if len(date_from) > 0 else ''
        date_to = date_to[0:10] if len(date_to) > 0 else ''
        users = User.objects.all()
        query_set = []
        date_set = set()
        for user in users:
            date_set.add(user.date_as_string())
        for date in date_set:
            if len(date_from) > 0 and date < date_from:
                continue
            if len(date_to) > 0 and date > date_to:
                continue
            number_of_users = 0
            for user in users:
                if user.date_as_string() == date:
                    number_of_users += 1
            query_set.append({'date': date, 'number_of_users': number_of_users})
        query_set.sort(key=lambda a: a['date'])
        context["qs"] = query_set
        context["char_type"] = self.request.GET.get('chartType', 'bar')
        return context


class PostChartView(TemplateView):
    template_name = 'djangoIspit/postChart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_from = self.request.GET.get('from', '')
        date_to = self.request.GET.get('to', '')
        username = self.request.GET.get('username', '')
        mustHavePic = self.request.GET.get('onlyPics', 'off')
        mustHavePic = True if mustHavePic == 'on' else False
        date_from = date_from[0:10] if len(date_from) > 0 else ''
        date_to = date_to[0:10] if len(date_to) > 0 else ''
        posts = Post.objects.all()
        query_set = []
        date_set = set()
        for post in posts:
            date_set.add(post.date_as_string())
        for date in date_set:
            if len(date_from) > 0 and date < date_from:
                continue
            if len(date_to) > 0 and date > date_to:
                continue
            number_of_users = 0
            for post in posts:
                if post.creator != username and len(username) > 0:
                    continue
                if mustHavePic and len(post.imageurl) == 0:
                    continue
                if post.date_as_string() == date:
                    number_of_users += 1
            if number_of_users > 0:
                query_set.append({'date': date, 'number_of_users': number_of_users})
        query_set.sort(key=lambda a: a['date'])
        context["qs"] = query_set
        context["char_type"] = self.request.GET.get('chartType', 'bar')
        return context


class CommentChartView(TemplateView):
    template_name = 'djangoIspit/commentChart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_from = self.request.GET.get('from', '')
        date_to = self.request.GET.get('to', '')
        username = self.request.GET.get('username', '')
        date_from = date_from[0:10] if len(date_from) > 0 else ''
        date_to = date_to[0:10] if len(date_to) > 0 else ''
        posts = Comment.objects.all()
        query_set = []
        date_set = set()
        for post in posts:
            date_set.add(post.date_as_string())
        for date in date_set:
            if len(date_from) > 0 and date < date_from:
                continue
            if len(date_to) > 0 and date > date_to:
                continue
            number_of_users = 0
            for post in posts:
                if post.creator != username and len(username) > 0:
                    continue
                if post.date_as_string() == date:
                    number_of_users += 1
            if number_of_users > 0:
                query_set.append({'date': date, 'number_of_users': number_of_users})
        query_set.sort(key=lambda a: a['date'])
        context["qs"] = query_set
        context["char_type"] = self.request.GET.get('chartType', 'bar')
        return context
