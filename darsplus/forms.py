from django import forms

import datetime

class LoginForm(forms.Form):
	name = forms.CharField(label='Username')
	word = forms.CharField(label='Password', widget=forms.PasswordInput(), required=False)


class RegForm(forms.Form):
	SEMESTERS = (
		(1, 'Freshman'),
		(2, 'Spring'),
		(3, 'Summer'),
	)
	now = datetime.datetime.now()
	year = now.year
	
	semester = forms.ChoiceField(choices=SEMESTERS)
	years = forms.ChoiceField(choices=[(x, x) for x in range(year, year+5)])