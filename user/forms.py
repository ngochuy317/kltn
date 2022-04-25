from django import forms

class CustomUserForm(forms.Form):
    SEX_CHOICES = [
        ('Nam','Nam'),
        ('Nữ','Nữ'),
        ('Khác','Khác'),
    ]
    username = forms.CharField(label='Tên đăng nhập', max_length=100)
    fullname = forms.CharField(label='Tên', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    phone_number = forms.CharField(label='Số điện thoại', max_length=100)
    address = forms.CharField(label='Địa chỉ', max_length=100)
    sex = forms.ChoiceField(label='Giới tính', choices=SEX_CHOICES, widget=forms.RadioSelect)
    dob = forms.DateField(label='Ngày sinh')

    def selected_genders_labels(self):
        return [label for value, label in self.fields['sex'].choices if value in self['sex'].value()]
