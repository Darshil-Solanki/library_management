from django import forms
from django.contrib.auth.models import User
from django.contrib.auth. forms import UserCreationForm
from fee.models import Userdata
class UserRegistrationForm(UserCreationForm):
    fullname=forms.CharField(label = "Fullname:", max_length=35) 
    email=forms.EmailField(label = "Email:")
    contact=forms.IntegerField(label = "Contact:")
    class Meta():
        model = User
        fields = ('username', 'fullname', 'email', 'contact')
        def save(self, commit=True):
            user = super(UserRegistrationForm, self).save(commit=False)
            first_name, last_name = self.cleaned_data["fullname"].split()
            user.first_name = first_name
            user.last_name = last_name
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user
        def errors():
            a="Some error occured"
            return a
class Userdataform(forms.ModelForm):
	def save(self, commit=True):
		userdata = super(Userdataform, self).save(commit=False)
		userdata.fullname = self.cleaned_data["fullname"]
		userdata.contact = self.cleaned_data["contact"]
		userdata.email = self.cleaned_data["email"]
		if commit:
			userdata.save()
		return userdata
	class Meta():
		model= Userdata
		fields = "__all__"
		widgets = {
			'profile_pic': forms.FileInput(attrs={'accept': 'image/*'}),
		}