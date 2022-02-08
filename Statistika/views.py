from django.shortcuts import render
from django.views import View

from .models import Stats


class StatsView(View):
    def get(self, request):
        stats = Stats.objects.all()
        return render(request, 'statistika.html', {"stats": stats})
