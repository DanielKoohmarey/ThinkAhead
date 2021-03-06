from django import forms
from django.forms.formsets import formset_factory
from django.forms.util import ErrorList
import datetime

""" reminder looking at PasswordChangeForm, PasswordResetForm Built-in forms for future iterations """
class LoginForm(forms.Form):
	username = forms.CharField(max_length=128, label='Username',
		widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(max_length=128, label='Password',
		widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


# Used in registration.html
class EmailForm(forms.Form):
	email = forms.EmailField()


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
 
	def __init__(self, *args, **kwargs):
		super(MajorForm, self).__init__(*args, **kwargs)
		"""
		output = ()
		index = 0
		from models import getCollegesToMajors
		for college in getCollegesToMajors():
			output += ((index,college),)
			index += 1		
		#self.fields['college'] = forms.ChoiceField(choices=output,initial=1)

		from models import Colleges
		majorList = Colleges.getMajorsInCollege(kwargs['initial']['college'])
		output = ()
		index = 0
		for major in majorList:
			output += ((index,major),)
			index += 1

		print output
		self.fields['major'] = forms.ChoiceField(choices=output)
		#self.fields['college'].initial = self.instance.object_id
		"""

	def errors(self):
		"""Check if value has been updated from default"""
		college = self['college'].value()
  		major = self['major'].value()
		if college == "0":
			return ErrorList([u"College and Major must be selected"])
		elif major == "-1":
			return ErrorList([u"Major must be selected."]) 
		else:
			return False

# Used in registration.html
class CourseForm(forms.Form):
	name = forms.CharField(label='Course')

CourseFormSet = formset_factory(CourseForm)
