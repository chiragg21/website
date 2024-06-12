from django import forms

class FabricNameForm(forms.Form):
    fabric_name = forms.CharField(label='Fabric Name', max_length=255)



class FabricQueryForm(forms.Form):
    fabric_name = forms.CharField(label='Fabric Name', max_length=255)
    query_type = forms.ChoiceField(label='Query Type', choices=[
        ('inventory', 'Inventory'),
        ('vendors', 'Vendors'),
        ('saleprice', 'Sale Price')
    ])