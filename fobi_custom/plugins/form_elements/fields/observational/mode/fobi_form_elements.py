import sys
from fobi.base import FormFieldPlugin, form_element_plugin_registry
from pldp.forms import MODE_BASIC_CHOICES, MODE_DETAILED_CHOICES

from ..widgets import ObservationalWidget
from ..fields import ObservationalField

from .forms import ModeObservationalForm


class ModeObservationalPlugin(FormFieldPlugin):
    """ModeObservationalPlugin."""

    uid = "mode_observational"
    name = "Mode"
    form = ModeObservationalForm
    group = "Observational"  # Group to which the plugin belongs to

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):

        choice_level = 'MODE_{}_CHOICES'.format(self.data.detail_level.upper())
        choices = getattr(sys.modules[__name__], choice_level)

        field_kwargs = {
            'required': self.data.required,
            'label': self.data.label,
            'choices': choices,
            'widget': ObservationalWidget(choices=choices)
        }

        return [(self.data.name, ObservationalField, field_kwargs)]


form_element_plugin_registry.register(ModeObservationalPlugin)
