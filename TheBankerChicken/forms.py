from django import forms
from TheBankerChicken.models import Account


class AccountForm(forms.ModelForm):
	class Meta:
		model = Account