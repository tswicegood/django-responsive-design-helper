from django.views.generic import TemplateView


class ResponsiveTestView(TemplateView):
    template_name = "responsive_design_helper/%s.html"

    def get_template_names(self, **kwargs):
        t = self.kwargs.get('type', 'all') or 'all'
        return self.template_name % t

    def get_context_data(self, **kwargs):
        context = super(ResponsiveTestView, self).get_context_data(**kwargs)
        url = self.request.build_absolute_uri()
        context["url_to_test"] = url[0:url.rindex("responsive")]
        return context
