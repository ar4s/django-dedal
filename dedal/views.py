from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from django.forms.models import model_to_dict


class DedalBaseMixin(object):
    action_name = None
    model = None

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
        context['verbose_name'] = self.model._meta.verbose_name
        return context


class DedalListView(DedalBaseMixin, ListView):
    pass


class DedalReadView(DedalBaseMixin, DetailView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['fields'] = model_to_dict(self.object)
        return context


class DedalModelFormMixin(object):
    @property
    def fields(self):
        # TODO: blacklist, editable from field
        return self.model._meta.get_all_field_names()


class DedalUpdateView(
    DedalModelFormMixin,
    DedalBaseMixin,
    UpdateView
):
    def get_form_class(self):
        return super().get_form_class()

    def get_success_url(self):
        return reverse(
            '{}_read'.format(
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
            '{}_read'.format(
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
        return reverse('{}_list'.format(self.model_name))
