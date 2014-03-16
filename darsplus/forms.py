from django import forms
from django.forms.formsets import formset_factory

import datetime
""" reminder looking at PasswordChangeForm, PasswordResetForm Built-in forms for future iterations """
class LoginForm(forms.Form):
	username = forms.CharField(max_length=128, label='Username',
		widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(max_length=128, label='Password',
		widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


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
	college = forms.ChoiceField(choices=((0, "Please select a college"),))
	major = forms.ChoiceField(choices=((0, "Please select a college and major"),))
 
	def validate(self, value):
		"""Check if value has been updated from default"""
		college = self.cleaned_data['college']
  		major = self.cleaned_data['major']
		if college == "Please select a college":
			raise forms.ValidationError("College must be selected.")
		if major == "Please select a college and major":
			raise forms.ValidationError("Major must be selected.")     

# Used in registration.html
class CourseForm(forms.Form):
	name = forms.CharField(label='Course')

CourseFormSet = formset_factory(CourseForm)
