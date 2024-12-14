from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, PasswordInput


# Registration form

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        # Mark email field as required
        self.fields['email'].required = True

    # Email validation
    def clean_email(self):
        email = self.cleaned_data.get("email")

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email already exists.')

        # Validate email length
        if len(email) >= 350:
            raise forms.ValidationError('Your email is too long.')

        return email

    # Override save method to ensure email is saved
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data.get('email')  # Save email to user
        if commit:
            user.save()
        return user
    

# Login form

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Update form

class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password2']


    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        # Mark fields as required
        self.fields['username'].required = True
        self.fields['email'].required = True

    
    # Email validation
    def clean_email(self):
        email = self.cleaned_data.get("email")

        # Check if email already exists
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This email already exists.')

        # Validate email length
        if len(email) >= 350:
            raise forms.ValidationError('Your email is too long.')
        
        return email