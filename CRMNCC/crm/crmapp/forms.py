from django import forms

from .models import opportunity,customer,staff,suggestion,order,service


class opportunityForm(forms.ModelForm):

    class Meta:
        model = opportunity
        fields = ('lms','opportunityno','customer', 'service','noofservices','authorized','coordinates',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class opportunitycForm(forms.ModelForm):

    class Meta:
        model = opportunity
        fields = ('lms','opportunityno', 'service','noofservices',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class customerForm(forms.ModelForm):

    class Meta:
        model = customer
        fields = ('customername','cr','activity','no_of_employees', 'branches','district','street','phone','email','current_services','notes',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }



class staffForm(forms.ModelForm):

    class Meta:
        model = staff
        fields = ('staffname','staff_id','joindate','employeejobtitle',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class suggestionForm(forms.ModelForm):

    class Meta:
        model = suggestion
        fields = ('requesttext','completion',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class orderForm(forms.ModelForm):

    class Meta:
        model = order
        fields = ('opportunity','orderno','accountno','service','cabinetno','circuitno','dealcategory',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class orderoForm(forms.ModelForm):

    class Meta:
        model = order
        fields = ('orderno','accountno','service',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class orderdoubleForm(forms.ModelForm):

    class Meta:
        model = order
        fields = ('orderno',)

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'textinputclass'}),
        #     'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        # }

class serviceForm(forms.ModelForm):

    class Meta:
        model = service
        fields = ('servicename','servicecategory','ncc_id','catalogue_id','nrc','mrc','commission',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
