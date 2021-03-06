from django import forms
from django.utils.translation import ugettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme
from pldp.forms import SURVEY_TIME_CHARACTER_CHOICES


theme = get_theme(request=None, as_instance=True)


class TimeCharacterForm(forms.Form, BaseFormFieldPluginForm):
    """TimeCharacterForm."""

    plugin_data_fields = [
        ("label", "Did anything out of the ordinary take place at the time of the survey count?"),
        ("name", "name"),
        ("default", ""),
        ("help_text", ""),
        ("required", False),
    ]

    label = forms.CharField(label="Label",
                            required=True,
                            )

    name = forms.CharField(required=True, widget=forms.widgets.HiddenInput())

    default = forms.ChoiceField(choices=SURVEY_TIME_CHARACTER_CHOICES,
                                help_text="This will be the default, but users will be "
                                "able to change this selection when running "
                                "the survey.",
                                widget=forms.widgets.Select(
                                    attrs={'class': theme.form_element_html_class}
                                ))

    help_text = forms.CharField(
        label=_("Help text"),
        required=False,
        widget=forms.widgets.Textarea(
            attrs={'class': theme.form_element_html_class}
        )
    )

    required = forms.BooleanField(label="Required", required=False)
