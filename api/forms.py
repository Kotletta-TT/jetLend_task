from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Investor


class InvestorCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Investor
        fields = ('username', 'email')


class InvestorChangeForm(UserChangeForm):
    class Meta:
        model = Investor
        fields = ('username', 'email')
