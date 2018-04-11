from django.forms import ModelForm
from portal.models import Phone

# define Phone class ModelForm
class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = ['phonenum']
