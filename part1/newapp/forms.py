from django import forms
class SampleForm(forms.Form):
    name = forms.CharField(label='User Name')
    email = forms.EmailField(label='User Email')
    age = forms.IntegerField(label='User Age')
    weight = forms.FloatField(label='User Weight')
    balance = forms.DecimalField(label='Account Balance')
    check=forms.BooleanField(label='Accept Terms')
    birth_date = forms.DateField(label='Birth Date')   
    appointment_time = forms.DateTimeField(label='Appointment Time')