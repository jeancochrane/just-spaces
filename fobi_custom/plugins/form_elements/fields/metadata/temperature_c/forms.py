from django import forms
from django.utils.translation import ugettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme

theme = get_theme(request=None, as_instance=True)


class TemperatureCForm(forms.Form, BaseFormFieldPluginForm):
    """TemperatureCForm."""

    plugin_data_fields = [
        ("label", "What is the current temperature, in degrees Celcius?"),
        ("name", "name"),
        ("help_text", ""),
        ("required", False),
    ]

    label = forms.CharField(label="Label",
                            required=True)

    name = forms.CharField(required=True, widget=forms.widgets.HiddenInput())

    help_text = forms.CharField(label=_("Help text"),
                                required=False,
                                widget=forms.widgets.Textarea(
                                attrs={'class': theme.form_element_html_class})
                                )

    required = forms.BooleanField(label="Required",
                                  required=False)
