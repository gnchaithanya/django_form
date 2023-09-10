from django import forms

class StudentForms(forms.Form):
    Sname=forms.CharField(max_length=100)
    Sid=forms.IntegerField()
    Semail=forms.EmailField()