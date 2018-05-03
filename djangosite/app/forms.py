from django.forms import ModelForm
form app.models import Moment

class MomentForm(ModelForm):
    class Mata:
        models = Moment
        fields = '__all__'