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
    CHOICES=[('s', 'small'), ('m', 'medium'), ('l', 'large')]
    size=forms.ChoiceField(choices=CHOICES, label='Size')
    MEAL=[('b', 'breakfast'), ('l', 'lunch'), ('d', 'dinner')] 
    meal_preference=forms.MultipleChoiceField(choices=MEAL, label='Meal Preference')
