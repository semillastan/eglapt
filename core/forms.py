from django import forms
from registration.forms import RegistrationFormUniqueEmail
from django.forms.extras.widgets import SelectDateWidget
from datetime import date
from django.contrib.auth.models import User
from core.models import *

year  = date.today().year
YEARS = range(year-16, year-100, -1)

class GameForm(forms.ModelForm):
    class Meta:
	model = Game
	fields = ('name','description','date_created','public')

class GameLevelForm(forms.ModelForm):
    class Meta:
	model = GameLevel
	fields = ('level','difficulty','max_score','max_playing_time_value', 'max_playing_time_unit')

class APTForm(forms.ModelForm):
    class Meta:
	model = APT
	fields = ('date_played','total_score','playing_time')
