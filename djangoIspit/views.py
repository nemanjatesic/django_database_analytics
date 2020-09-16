from .models import User
from django.views.generic import TemplateView


class UserChartView(TemplateView):
    template_name = 'djangoIspit/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        query_set = []
        date_set = set()
        for user in users:
            date_set.add(user.date_as_string())
        for date in date_set:
            number_of_users = 0
            for user in users:
                if user.date_as_string() == date:
                    number_of_users += 1
            query_set.append({'date': date, 'number_of_users': number_of_users})
        query_set.sort(key=lambda a: a['date'])
        context["qs"] = query_set
        return context
