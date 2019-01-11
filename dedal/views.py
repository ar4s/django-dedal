from django.db.models.fields import Field
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    TemplateView
)
from django.forms.models import model_to_dict

from dedal.conf import PAGINATE_BY
from dedal.compat import reverse


class DedalBaseMixin(object):
    action_name = None
    model = None
    site = None

    @property
    def model_name(self):
        return self.model._meta.model_name

    def get_template_names(self):
        names = super().get_template_names()
        names.append('dedal/generic_{}.html'.format(self.action_name))
        return names

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model'] = self.model
        context['models'] = self.site.registered_models
        return context


class ModelListView(DedalBaseMixin, TemplateView):
    template_name = 'dedal/generic_model_list.html'


class DedalListView(DedalBaseMixin, ListView):
    paginate_by = PAGINATE_BY


class DedalReadView(DedalBaseMixin, DetailView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['fields'] = model_to_dict(self.object)
        return context


class DedalModelFormMixin(object):
    @property
    def fields(self):
        # TODO: blacklist, editable from field
        return [
            field.name
            for field in self.model._meta.get_fields()
            if isinstance(field, Field)
        ]


class DedalUpdateView(
    DedalModelFormMixin,
    DedalBaseMixin,
    UpdateView
):
    def get_form_class(self):
        return super().get_form_class()

    def get_success_url(self):
        return reverse(
            '{}:read'.format(
                self.model_name
            ), args=(self.object.pk,)
        )


class DedalCreateView(
    DedalModelFormMixin,
    DedalBaseMixin,
    CreateView
):
    def get_success_url(self):
        return reverse(
            '{}:read'.format(
                self.model_name
            ), args=(self.object.pk,)
        )


class DedalDeleteView(
    DedalModelFormMixin,
    DedalBaseMixin,
    DeleteView
):
    action_name = None
    model = None

    def get_success_url(self):
        return reverse('{}:list'.format(self.model_name))
