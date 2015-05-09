from django.core.urlresolvers import reverse
from django.conf.urls import url, include
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.forms.models import model_to_dict


class DedalGenericTemplatesMixin(object):
    def get_template_names(self):
        names = super(DedalGenericTemplatesMixin, self).get_template_names()
        names.append('dedal/generic{}.html'.format(self.template_name_suffix))
        return names


class Dedal(object):
    def __init__(self, model, actions):
        self.actions = actions
        self.model = model
        self.model_name = self.model._meta.model_name

    def list(self):
        class View(DedalGenericTemplatesMixin, ListView):
            template_name_suffix = '_list'
            model = self.model

            def get_context_data(self, **kwargs):
                context = super(View, self).get_context_data(**kwargs)
                context['model'] = self.model
                context['verbose_name'] = self.model._meta.verbose_name
                return context

        return View.as_view()

    def read(self):
        class View(DedalGenericTemplatesMixin, DetailView):
            template_name_suffix = '_detail'
            model = self.model

            def get_context_data(self, *args, **kwargs):
                context = super(View, self).get_context_data(*args, **kwargs)
                context['fields'] = model_to_dict(self.object)
                return context
        return View.as_view()

    def update(self):
        model_name = self.model_name

        class View(DedalGenericTemplatesMixin, UpdateView):
            template_name_suffix = '_form'
            model = self.model
            # todo: black list
            fields = self.model._meta.get_all_field_names()

            def get_success_url(self):
                return reverse(
                    '{}_read'.format(model_name), args=(self.object.pk,)
                )
        return View.as_view()

    def create(self):
        model_name = self.model_name

        class View(DedalGenericTemplatesMixin, CreateView):
            template_name_suffix = '_form'
            model = self.model
            # todo: black list
            fields = self.model._meta.get_all_field_names()

            def get_success_url(self):
                return reverse(
                    '{}_read'.format(model_name), args=(self.object.pk,)
                )
        return View.as_view()

    def delete(self):
        model_name = self.model_name

        class View(DedalGenericTemplatesMixin, DeleteView):
            template_name_suffix = '_delete'
            model = self.model
            # todo: black list
            fields = self.model._meta.get_all_field_names()

            def get_success_url(self):
                return reverse('{}_list'.format(model_name))
        return View.as_view()

    @property
    def urls(self):
        return [
            url(
                r'^$',
                self.list(),
                name='{}_list'.format(self.model_name)
            ),
            url(
                r'^create/$',
                self.create(),
                name='{}_create'.format(self.model_name)
            ),
            url(
                r'^(?P<pk>\d+)/$',
                self.read(),
                name='{}_read'.format(self.model_name)
            ),
            url(
                r'^(?P<pk>\d+)/update/$',
                self.update(),
                name='{}_update'.format(self.model_name)
            ),
            url(
                r'^(?P<pk>\d+)/delete/$',
                self.delete(),
                name='{}_delete'.format(self.model_name)
            ),
        ]


class DedalSite(object):
    def __init__(self):
        self._register = {}

    def register(self, model, actions):
        print('register', model, actions)
        self._register[model] = Dedal(model, actions)

    def get_urls(self):
        urlpatterns = []
        for model, dedal in self._register.items():
            urlpatterns += [
                url(r'^{}/'.format(model.__name__.lower()), include(dedal.urls))
            ]
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls()


site = DedalSite()
