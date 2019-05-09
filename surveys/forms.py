from django import forms
from pldp.models import Agency, Location, Study, Survey

from fobi_custom.plugins.form_elements.fields import types as fobi_types
from .models import SurveyFormEntry, SurveyChart


class CreateAgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = '__all__'


class CreateLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class StudyCreateForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }


class SurveyCreateForm(forms.ModelForm):
    class Meta:
        model = SurveyFormEntry
        fields = ['user', 'name', 'study', 'location', 'type']


class SurveyChartForm(forms.ModelForm):
    class Meta:
        model = SurveyChart
        fields = ['short_description', 'order', 'primary_source']
        widgets = {
            'order': forms.HiddenInput(),
            'primary_source': forms.Select()
        }

    def __init__(self, *args, form_entry, **kwargs):
        self.form_entry = SurveyFormEntry.objects.get(id=form_entry)
        super().__init__(*args, **kwargs)
        survey = Survey.objects.filter(form_id=form_entry)[0]
        choices = [(component.name, component.label) for component in survey.components
                   if component.type in fobi_types.ALL_VALID_TYPES]
        choices = [('', '-----')] + choices  # Offer a null choice
        self.fields['primary_source'].widget.choices = choices
