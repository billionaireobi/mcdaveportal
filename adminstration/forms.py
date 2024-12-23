# from django import forms
# from .models import Event

# class EventForm(forms.ModelForm):
#     title=forms.CharField(
#         label="title",
#         max_length=100,
#         widget=forms.TextInput(attrs={'class':'form-control form-control-lg',
#                                                                     'placeholder':'title',
#                                                                     'autocomplete':'off',
#                                                                     'id':'title'}))
#     description=forms.CharField(
#         label="description",
#         max_length=100,
#         widget=forms.TextInput(attrs={'class':'form-control form-control-lg',
#                                                                     'placeholder':'description',
#                                                                     'autocomplete':'off',
#                                                                     'id':'description'}))
#     start = forms.DateTimeField(
#     required=True,
#     widget=forms.DateTimeInput(attrs={
#         "placeholder": "start",  # Adjust placeholder text
#         "class": "form-control",
#         "id": "start",           # Adjust ID to reflect the field name
#         "type": "datetime-local"          # HTML5 date picker
#     }),
#     label="start"
#     )
#     end = forms.DateTimeField(
#     required=True,
#     widget=forms.DateTimeInput(attrs={
#         "placeholder": "end",  # Adjust placeholder text
#         "class": "form-control",
#         "id": "end",           # Adjust ID to reflect the field name
#         "type": "datetime-local"          # HTML5 date picker
#     }),
#     label="end"
#     )
#     class Meta:
#         model = Event
#         fields = ['title', 'description', 'start', 'end', '']
        
