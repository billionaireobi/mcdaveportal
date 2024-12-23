from typing import Any
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms 
from.models import *
from django.core.validators import EmailValidator
import dns.resolver
from django.core.exceptions import ValidationError
# update password form
class UpdatePasswordForm(SetPasswordForm):
    class Meta:
        model=User
        fields=('new_password1','new_password2')
    
    def __init__(self, *args, **kwargs):
        super(UpdatePasswordForm,self).__init__(*args, **kwargs)
       
        
        self.fields["new_password1"].widget.attrs['class']='form-control form-control-lg'
        self.fields["new_password1"].widget.attrs['placeholder']='password1'
        self.fields["new_password1"].widget.attrs['autocomplete']='off'
        self.fields["new_password1"].widget.attrs['id']='signup-password' 
        self.fields["new_password1"].label='Password'
        self.fields["new_password1"].help_text=( '<ul class="form-text text-muted small">'
            '<li>Your password can\'t be too similar to your other personal information.</li>'
            '<li>Your password must contain at least 8 characters.</li>'
            '<li>Your password can\'t be a commonly used password.</li>'
            '<li>Your password can\'t be entirely numeric.</li>'
            '</ul>')
        
        self.fields["new_password2"].widget.attrs['class']='form-control form-control-lg'
        self.fields["new_password2"].widget.attrs['placeholder']='confirm password'
        self.fields["new_password2"].widget.attrs['autocomplete']='off'
        self.fields["new_password2"].widget.attrs['id']='signup-confirmpassword'
        self.fields["new_password2"].label='Confirm Password'
        self.fields["new_password2"].help_text=('<span class="form-text text-muted">'
            '<small>Enter the same password as before for verification.</small>'
            '</span>')
    
# update profile form
class UpdateUserForm(UserChangeForm):
    # hide password field
    password=None
    # rest of the fields
    first_name=forms.CharField(
        label="First Name",
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg',
                                                                    'placeholder':'First Name',
                                                                    'autocomplete':'off',
                                                                    'id':'update-firstname'}))
    last_name=forms.CharField(
        label="Last Name", 
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg',
                                                                        'placeholder':'Last Name',
                                                                        'autocomplete':'off',
                                                                        'id':'update-lastname'}))
    email=forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg',
                                                                  'placeholder':'Email',
                                                                  'autocomplete':'off',
                                                                  'id':'update-lastname'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email')
    
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm,self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs['class']='form-control form-control-lg'
        self.fields["username"].widget.attrs['placeholder']='User Name'
        self.fields["username"].widget.attrs['autocomplete']='off'
        self.fields["username"].widget.attrs['id']='update-lastname'
        self.fields["username"].label='User Name'
        self.fields["username"].help_text =(
            '<span class="form-text text-muted">'
            '<small>Required. 150 characters or fewer. Only letters, digits, and @/./+/-/_ allowed.</small>'
            '</span>')
        
        self.fields["email"].widget.attrs['class']='form-control form-control-lg'
        self.fields["email"].widget.attrs['placeholder']='Email'
        self.fields["email"].widget.attrs['autocomplete']='off'
        self.fields["email"].widget.attrs['id']='update-email'
        self.fields["email"].label='Email'
        self.fields["email"].help_text =(
            '<span class="form-text text-muted">'
            '<small>Required. 150 characters or fewer. Only letters, digits, and @/./+/-/_ allowed.</small>'
            '</span>')
        
        self.fields["first_name"].widget.attrs['class']='form-control form-control-lg'
        self.fields["first_name"].widget.attrs['placeholder']='First Name'
        self.fields["first_name"].widget.attrs['autocomplete']='off'
        self
    
# registeruser form
class SignUpForm(UserCreationForm):
    first_name=forms.CharField(
        label="First Name",
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg',
                                                                    'placeholder':'First Name',
                                                                    'autocomplete':'off',
                                                                    'id':'signup-firstname'}))
    last_name=forms.CharField(
        label="Last Name", 
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg',
                                                                        'placeholder':'Last Name',
                                                                        'autocomplete':'off',
                                                                        'id':'signup-lastname'}))
    email=forms.EmailField(
        required=True,
        label="Email",
        widget=forms.TextInput(attrs={'class':'form-control form-control-lg',
                                                                  'placeholder':'Email',
                                                                  'autocomplete':'off',
                                                                  'id':'signup-lastname'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
    # user cannot signup with the same email
    def clean_email(self):
        email = self.cleaned_data.get("email")
        domain = email.split('@')[1]
        if User.objects.filter(email=email).exists():
            raise ValidationError("An Account With That Email Already Exists!!")
        
        # Validate email format
        try:
            validator = EmailValidator()
            validator(email)
        except ValidationError:
            raise ValidationError("Invalid email format.")
        # Check if domain has valid MX record
        try:
            dns.resolver.resolve(domain, 'MX')
        except Exception:
            raise ValidationError("Invalid email domain. Please use a valid email address.")
        return email
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs['class']='form-control form-control-lg'
        self.fields["username"].widget.attrs['placeholder']='User Name'
        self.fields["username"].widget.attrs['autocomplete']='off'
        self.fields["username"].widget.attrs['id']='signup-lastname'
        self.fields["username"].label='User Name'
        self.fields["username"].help_text =(
            '<span class="form-text text-muted">'
            '<small>Required. 150 characters or fewer. Only letters, digits, and @/./+/-/_ allowed.</small>'
            '</span>')
        
        self.fields["password1"].widget.attrs['class']='form-control form-control-lg'
        self.fields["password1"].widget.attrs['placeholder']='password1'
        self.fields["password1"].widget.attrs['autocomplete']='off'
        self.fields["password1"].widget.attrs['id']='signup-password' 
        self.fields["password1"].label='Password'
        self.fields["password1"].help_text=( '<ul class="form-text text-muted small">'
            '<li>Your password can\'t be too similar to your other personal information.</li>'
            '<li>Your password must contain at least 8 characters.</li>'
            '<li>Your password can\'t be a commonly used password.</li>'
            '<li>Your password can\'t be entirely numeric.</li>'
            '</ul>')
        
        self.fields["password2"].widget.attrs['class']='form-control form-control-lg'
        self.fields["password2"].widget.attrs['placeholder']='confirm password'
        self.fields["password2"].widget.attrs['autocomplete']='off'
        self.fields["password2"].widget.attrs['id']='signup-confirmpassword'
        self.fields["password2"].label='Confirm Password'
        self.fields["password2"].help_text=('<span class="form-text text-muted">'
            '<small>Enter the same password as before for verification.</small>'
            '</span>')


# crqs data
class AddRecordForm(forms.ModelForm):
    date = forms.DateTimeField(
    required=True,
    widget=forms.DateTimeInput(attrs={
        "placeholder": "Datetime",  # Adjust placeholder text
        "class": "form-control",
        "id": "datetime",           # Adjust ID to reflect the field name
        "type": "datetime-local"          # HTML5 date picker
    }),
    label="Datetime"
    )
    week = forms.CharField(required=True,
        widget=forms.TextInput(attrs={"placeholder": "Week","class": "form-control","id": "week","readonly": "readonly"}),label="Week"
    )
    batch_number = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Batch Number","class": "form-control","id": "BatchNo"}),label="Batch No"
    )
    assessor = forms.ChoiceField(
    required=True,
    choices=[('Assessor 1', 'Assessor 1'), ('Assessor 2', 'Assessor 2')],  # Add actual choices
    widget=forms.Select(attrs={"placeholder": "select assessor","class": "form-control", "id": "assessor"}),
    label="Assessor"
    )
    variant = forms.ChoiceField(
    required=True,
    choices=[('variant 1', 'variant 1'), ('variant 2', 'variant 2')],  # Add actual choices
    widget=forms.Select(attrs={"placeholder": "select variant","class": "form-control", "id": "variant"}),
    label="variant"
    )
    sku = forms.ChoiceField(
    required=True,
    choices=[('sku 1', '500g'), ('sku 2', '1000g')],  # Add actual choices
    widget=forms.Select(attrs={"placeholder": "select sku","class": "form-control", "id": "sku"}),
    label="sku"
    )
    issue_description = forms.ChoiceField(
    required=True,
    choices=[('issue_description 1', 'issue_description 1'), ('issue_description 2', 'issue_description 2')],  # Add actual choices
    widget=forms.Select(attrs={"placeholder": "select issue","class": "form-control", "id": "issue_description"}),
    label="issue description"
    )
    number_of_samples = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={"placeholder": "Number of Samples","class": "form-control","id": "number_of_samples","min": "0"}),label="Number of Samples"
    )
    count_of_issues = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={"placeholder": "Count of Issues","class": "form-control","id": "count_of_issues","min": "0"}),label="Count of Issues"
    )
    score = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={"placeholder": "Score","class": "form-control","id": "score","step": "0.01"}),label="Score"
    )
    temperature = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={"placeholder": "Temperature","class": "form-control","id": "temperature","step": "0.01"}),label="Temperature"
    )
    speed = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={"placeholder": "Speed","class": "form-control","id": "speed","step": "0.01"}),label="Speed"
    )
    parameter = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Parameter","class": "form-control","id": "parameter"}),label="Parameter"
    )
    property = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Property","class": "form-control","id": "property"}),label="Property"
    )
    issue = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={"placeholder": "Issue","class": "form-control","id": "issue","rows": "2"}),label="Issue"
    )
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "Comment","class": "form-control","id": "comment","rows": "2"}),label="Comment"
    )

    class Meta:
        model = CRQSData
        exclude=("user",)

# packing data
class PackRecordForm(forms.ModelForm):
    date = forms.DateTimeField(
    required=True,
    widget=forms.DateTimeInput(attrs={
        "placeholder": "Datetime",  # Adjust placeholder text
        "class": "form-control",
        "id": "packdatetime",           # Adjust ID to reflect the field name
        "type": "datetime-local"          # HTML5 date picker
    }),
    label="Datetime"
    )
    week = forms.CharField(required=True,
        widget=forms.TextInput(attrs={"placeholder": "Week","class": "form-control","id": "packweek","readonly": "readonly"}),label="Week"
    )
    sku = forms.ChoiceField(
    required=True,
    choices=[('sku 1', '500g'), ('sku 2', '1000g')],  # Add actual choices
    widget=forms.Select(attrs={"placeholder": "select sku","class": "form-control", "id": "packsku"}),
    label="sku"
    )                            
    target = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Target","class": "form-control","id": "target"}),label="target"
    )
    achieved = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Achieved","class": "form-control","id": "Achieved"}),label="Achieved"
    )                            
    batch_number = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Batch Number","class": "form-control","id": "packBatchNo"}),label="Batch No"
    )                            
    variant = forms.ChoiceField(
    required=True,
    choices=[('variant 1', 'variant 1'), ('variant 2', 'variant 2')],  # Add actual choices
    widget=forms.Select(attrs={"placeholder": "select variant","class": "form-control", "id": "packvariant"}),
    label="variant"
    )
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "Comment","class": "form-control","id": "packcomment","rows": "2"}),label="Comment"
    )                           
    assessor = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "assessor","class": "form-control","id": "packassessor"}),label="assessor"
    )
    class Meta:
        model = PackingData
        exclude=("user",)  

# vimlemon production

class VimLemonForm(forms.ModelForm):
    # Date field with date picker
    date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date","id": "date-field","class": "form-control"}), label="Date"
    )
    hash=forms.IntegerField(
        widget=forms.NumberInput(attrs={"id": "hash-field","placeholder":"#","class": "form-control"}),
        label="#"
    )

    # Batch Number: Autofilled with "VLE" but editable
    batch_number= forms.CharField(
        initial="VLE008006",
        widget=forms.TextInput(attrs={ "class": "form-control", "id": "batch-no-field"}),
        label="Batch Number",
    )

    # Start time: Autofilled with the current time
    start_time = forms.TimeField(
        # initial=datetime.now().strftime("%H:%M"),
        widget=forms.TimeInput(attrs={"type": "time","class": "form-control", "id": "start-time-field"}),
        label="Start Time",
    )
    stop_time = forms.TimeField(
        widget=forms.TimeInput(attrs={"type": "time", "class": "form-control", "id": "stop-time-field"}), label="Stop Time"
    )

    # Batch Time: Read-only (13 minutes difference)
    batch_time = forms.DecimalField(
        initial=13.00,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"class": "form-control", "id": "batch-time-field"}), label="Batch Time"
    )

    # Whiting Quantity: Autofilled
    whiting_quantity = forms.DecimalField(
        initial=1700.00,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"id": "whiting-qty-field","class": "form-control"}),
        label="Whiting Quantity",
    )

    # Whiting Batch Number: User fills in
    whiting_batch_number = forms.CharField(
        
        widget=forms.TextInput(attrs={"placeholder": "Whiting Batch Number", "class": "form-control", "id": "whiting-batch-no-field"}),
        label="Whiting Batch Number",
    )

    # Magadi Quantity: Autofilled
    magadi_quantity = forms.DecimalField(
        initial=52.090,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"class": "form-control", "id": "magadi-qty-field"}),
        label="Magadi Quantity",
    )

    # Magadi Batch Number: User fills in
    magadi_batch_number = forms.CharField(
        
        widget=forms.TextInput(attrs={"placeholder": "Magadi Batch Number","class": "form-control", "id": "magadi-batch-no-field"}),
        label="Magadi Batch Number",
    )

    # Add fields for remaining data columns, like TCCA, Sulphon, Lime Per, etc.
    tcca_quantity = forms.DecimalField(
        initial=7.090,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"class": "form-control","id": "tcca-qty-field"}),
        label="TCCA Quantity",
    )

    tcca_batch_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control","id":"tcca-batch","placeholder": "TCCA Batch Number"}),
        label="TCCA Batch Number",
    )

    sulphonic_acid_quantity = forms.DecimalField(
        initial=37.760,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"class": "form-control", "id": "sulphonic-qty-field"}),
        label="Sulphonic Quantity",
    )
    sulphonic_acid_batch_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Sulphonic Batch Number","id":"Sulphonic-batch"}),
        label="Sulphonic Batch Number",
    )

    lime_perf_quantity = forms.DecimalField(
        initial=2.156,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"class": "form-control", "id": "lime-per-qty-field"}),
        label="Lime Perf qty",
    )
    lime_perf_batch_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control","placeholder": "lime_per_batch_no", "id": "lime-per-batch-field"}),
        label="lime perf Batch Number",
    )

    batch_size = forms.DecimalField(
        initial=1799.096,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"class": "form-control","id": "batch-size-field"}),
        label="Batch Size",
    )
    pressure=forms.DecimalField(
        initial=6.00,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"class": "form-control", "id": "pressure"}),
        label="pressure",
    )
    done_by = forms.CharField(
        initial="Macharia",
        widget=forms.TextInput(attrs={"class": "form-control", "id": "done-by-field"}),
        label="Done By",
    )

    checked_by = forms.CharField(
        initial="Vincent",
        widget=forms.TextInput(attrs={"class": "form-control","id": "checked-by-field"}),
        label="Checked By",
    )

    verified_by = forms.CharField(
         initial="Dominic",
        widget=forms.TextInput(attrs={"class": "form-control", "id": "verified-by-field"}),
        label="Verified By",
    )
    class Meta:
        model = VimLemonKe
        exclude=("user",) 
        
        
# vim lavender production
class VimLavenderForm(forms.ModelForm):
    # Date field with date picker
    date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date","id": "date-field","class": "form-control"}), label="Date"
    )
    hash=forms.IntegerField(
        widget=forms.NumberInput(attrs={"id": "hash-field","placeholder":"#","class": "form-control"}),
        label="#"
    )

    # Batch Number: Autofilled with "VLE" but editable
    batch_number= forms.CharField(
        initial="VLA007066",
        widget=forms.TextInput(attrs={ "class": "form-control", "id": "batch-no-field"}),
        label="Batch Number",
    )

    # Start time: Autofilled with the current time
    start_time = forms.TimeField(
        # initial=datetime.now().strftime("%H:%M"),
        widget=forms.TimeInput(attrs={"type": "time","class": "form-control", "id": "start-time-field"}),
        label="Start Time",
    )

    # Stop time: Autofilled to 13 minutes after the start time
    # stop_time = forms.TimeField(
    #     initial=(datetime.now() + timedelta(minutes=13)).strftime("%H:%M"),
    #     widget=forms.TimeInput(attrs={"type": "time","id": "stop-time-field","class": "form-control"}),
    #     label="Stop Time",
    # )
    stop_time = forms.TimeField(
        widget=forms.TimeInput(attrs={"type": "time", "class": "form-control", "id": "stop-time-field"}), label="Stop Time"
    )

    # Batch Time: Read-only (13 minutes difference)
    batch_time = forms.DecimalField(
        initial=13.00,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"class": "form-control", "id": "batch-time-field"}), label="Batch Time"
    )

    # Whiting Quantity: Autofilled
    whiting_quantity = forms.DecimalField(
        initial=1700.00,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"id": "whiting-qty-field","class": "form-control"}),
        label="Whiting Quantity",
    )

    # Whiting Batch Number: User fills in
    whiting_batch_number = forms.CharField(
        
        widget=forms.TextInput(attrs={"placeholder": "Whiting Batch Number", "class": "form-control", "id": "whiting-batch-no-field"}),
        label="Whiting Batch Number",
    )

    # Magadi Quantity: Autofilled
    magadi_quantity = forms.DecimalField(
        initial=52.090,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"class": "form-control", "id": "magadi-qty-field"}),
        label="Magadi Quantity",
    )

    # Magadi Batch Number: User fills in
    magadi_batch_number = forms.CharField(
        
        widget=forms.TextInput(attrs={"placeholder": "Magadi Batch Number","class": "form-control", "id": "magadi-batch-no-field"}),
        label="Magadi Batch Number",
    )

    # Add fields for remaining data columns, like TCCA, Sulphon, Lime Per, etc.
    tcca_quantity = forms.DecimalField(
        initial=7.090,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"class": "form-control","id": "tcca-qty-field"}),
        label="TCCA Quantity",
    )

    tcca_batch_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control","id":"tcca-batch","placeholder": "TCCA Batch Number"}),
        label="TCCA Batch Number",
    )

    sulphonic_acid_quantity = forms.DecimalField(
        initial=37.760,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"class": "form-control", "id": "sulphonic-qty-field"}),
        label="Sulphonic Quantity",
    )
    sulphonic_acid_batch_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Sulphonic Batch Number","id":"Sulphonic-batch"}),
        label="Sulphonic Batch Number",
    )
    katio_quantity = forms.DecimalField(
        initial=0.89,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"class": "form-control", "id": "katio_quantity"}),
        label="katio_quantity",
    )
    katio_batch_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control","placeholder": "katio_batch_number", "id": "katio_batch_number"}),
        label="katio_batch_number",
    )
    batch_size = forms.DecimalField(
        initial=1797.74,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"class": "form-control","id": "batch-size-field"}),
        label="Batch Size",
    )
    pressure=forms.DecimalField(
        initial=6.00,
        max_digits=10,
        decimal_places=3,
        widget=forms.NumberInput(attrs={"class": "form-control", "id": "pressure"}),
        label="pressure",
    )
    done_by = forms.CharField(
        initial="Macharia",
        widget=forms.TextInput(attrs={"class": "form-control", "id": "done-by-field"}),
        label="Done By",
    )

    checked_by = forms.CharField(
        initial="Vincent",
        widget=forms.TextInput(attrs={"class": "form-control","id": "checked-by-field"}),
        label="Checked By",
    )

    verified_by = forms.CharField(
         initial="Dominic",
        widget=forms.TextInput(attrs={"class": "form-control", "id": "verified-by-field"}),
        label="Verified By",
    )
    class Meta:
        model = VimLavenderKe
        exclude=("user",) 
        