from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class HomeView(View):
    # get post update delete
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'home/index.html', context)