from django import forms
class SampleForm(forms.Form):
    name = forms.CharField(label='Full Name',initial="Rahim",help_text="Total length must be 70 char",required=False,widget=forms.Textarea(attrs={'id':'text_area','class':'class1 class 2','placeholder':'Enter your name'}))
    email = forms.EmailField(label='User Email')
    age = forms.CharField(label='User Age',widget=forms.NumberInput)
    # weight = forms.FloatField(label='User Weight')
    # balance = forms.DecimalField(label='Account Balance')
    check=forms.BooleanField(label='Accept Terms')
    birth_date = forms.CharField(label='Birth Date',widget=forms.DateInput(attrs={'type':'date'}))   
    appointment_time = forms.CharField(label='Appointment Time',widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES=[('s', 'small'), ('m', 'medium'), ('l', 'large')]
    size=forms.ChoiceField(choices=CHOICES, label='Size',widget=forms.RadioSelect)
    MEAL=[('b', 'breakfast'), ('l', 'lunch'), ('d', 'dinner')] 
    meal_preference=forms.MultipleChoiceField(choices=MEAL, label='Meal Preference',widget=forms.CheckboxSelectMultiple)
class StudentData(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'placeholder': 'Full name'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'placeholder': 'your@email.com'}))
    def clean_name(self):
        valname=self.cleaned_data['name']
        if len(valname)<10:
            raise forms.ValidationError("Enter your name at least 10 char")
        return valname  
    def clean_email(self):
        valemail=self.cleaned_data['email']
        if '.com' not in valemail:
            raise forms.ValidationError("email should have be .com")
        return valemail

