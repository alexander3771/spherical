from django.views.generic import TemplateView


class Landing(TemplateView):
    template_name = 'landing/index.html'
