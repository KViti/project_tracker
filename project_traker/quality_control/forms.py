from django import forms
from django.forms import ModelForm
from .models import BugReport, FeatureRequest

class BugReportForm(ModelForm):
    class Meta:
        model = BugReport
        fields =['title','description','project','task','status', 'priority']
class FeatureRequestForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title','description','project','task','status', 'priority']