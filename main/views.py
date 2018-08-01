from django.views.generic import View, ListView, DetailView
from django.shortcuts import render
from .models import Site

# Create your views here.
class IndexView(View):
    template_name = 'main/index.html'

    # display blank form
    def get(self, request):
        return render(request, self.template_name, None)


class Portfolio(ListView):
    template_name = 'main/portfolio.html'
    context_object_name = 'sites'

    def get_queryset(self):
        return Site.objects.all()

class SiteDetail(DetailView):
    model = Site
    template_name = 'main/sitedetail.html'