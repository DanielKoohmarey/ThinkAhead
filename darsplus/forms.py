from django import forms
from django.forms.formsets import BaseFormSet
from django.forms.formsets import formset_factory

import datetime
""" reminder looking at PasswordChangeForm, PasswordResetForm Built-in forms for future iterations """
class LoginForm(forms.Form):
	name = forms.CharField(label='Username', max_length=128)
	word = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=128)


# Used in registration.html
class GradForm(forms.Form):
	SEMESTERS = (
		('Fall', 'Fall'),
		('Spring', 'Spring'),
		('Summer', 'Summer'),
	)
	now = datetime.datetime.now()
	currYear = now.year
	
	semester = forms.ChoiceField(choices=SEMESTERS)
	year = forms.ChoiceField(choices=[(x, x) for x in range(currYear, currYear+5)])


# Used in registration.html
class MajorForm(forms.Form):
	college = forms.ChoiceField(choices=((0, 'Please select a college'),))
	major = forms.ChoiceField(choices=((0, 'Please select a college and major'),))


# Used in registration.html
class CourseForm(forms.Form):
	name = forms.CharField(label='Course')

CourseFormSet = formset_factory(CourseForm)