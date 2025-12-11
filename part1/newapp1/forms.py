from django import forms
from . models import StudentModel
class StudentForm(forms.ModelForm):
    
    class Meta:
        model=StudentModel
        fields = '__all__'
        labels={
            'roll':'Enter your roll',
            'name':'Enter your name',
            'father_name':'Enter your father name',
            'address':'Enter your address',
        }
        widgets={
            
            'name':forms.TextInput(attrs={'class':'btn-primary'}),
       }
      
        help_texts={
            'name':'This field is required',

        }
        error_messages={
            'name':{
                'required':'Please enter your name'
            }
        }
