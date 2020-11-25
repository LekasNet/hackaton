from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        coords = {"x": '55.817577', "y": '37.832180'}
        return render(request, 'index.html', coords)
