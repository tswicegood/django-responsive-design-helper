from django.views.generic import TemplateView


class ResponsiveTestView(TemplateView):
    template_name = "responsive_design_helper/all.html"

    def get_context_data(self, **kwargs):
        context = super(ResponsiveTestView, self).get_context_data(**kwargs)
        url_to_test = self.request.build_absolute_uri()[0:-len("responsive/")]
        context["url_to_test"] = url_to_test
        return context
