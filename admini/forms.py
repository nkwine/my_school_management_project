from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import User,teacher, secretary,student,bursar,dos,management
from django.db import transaction

sex =(
     ( 'female','F'),
    ('male','M')
    )
types=(
        ('tearcher','tearcher'),
        ('student','student'),
        ('secretary','secretary'),
        ('bursar','bursar'),
        ('dos','dos'),
        ('head','head')
           )

class userf(UserCreationForm):
    first_name =forms.CharField(label='First name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}))
    last_name =forms.CharField(label='Last name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}))
    type= forms.CharField(label='Usertype',widget=forms.Select(attrs={'class':'form-control'},choices=types))
    image =forms.ImageField( required=False)
    class Meta(UserCreationForm.Meta):
        model =User
        fields = ('first_name','last_name','type','image','username')
class teacher_regf(forms.ModelForm):
    department=forms.CharField(label='Department',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'department'}))
    email =forms.EmailField(label='Email adress',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email adress'}))
    contact =forms.CharField(label='Contact',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'contact'}))
    gender=forms.CharField(label='Gender',widget=forms.RadioSelect(choices=sex))
    class Meta:
        model =teacher
        fields = '__all__'
        exclude=["user"]
class admin_regf(forms.ModelForm):    
    email =forms.EmailField(label='Email adress',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email adress'}))
    contact =forms.CharField(label='Contact',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'contact'}))
    class Meta:
        model =management
        fields = '__all__'
        exclude=["user"]
class secretary_regf(forms.ModelForm):    
    email =forms.EmailField(label='Email adress',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email adress'}))
    contact =forms.CharField(label='Contact',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'contact'}))
    class Meta:
        model =secretary
        fields = '__all__'
        exclude=["user"]
class bursar_regf(forms.ModelForm):    
    email =forms.EmailField(label='Email adress',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email adress'}))
    contact =forms.CharField(label='Contact',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'contact'}))
    class Meta:
        model =bursar
        fields = '__all__'
        exclude=["user"]
class dos_regf(forms.ModelForm):    
    email =forms.EmailField(label='Email adress',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email adress'}))
    contact =forms.CharField(label='Contact',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'contact'}))
    class Meta:
        model =dos
        fields = '__all__'
        exclude=["user"]