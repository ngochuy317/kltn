from django import forms
from .models import CustomUser

class CustomUserForm(forms.Form):
    SEX_CHOICES = [
        ('Nam','Nam'),
        ('Nữ','Nữ'),
        ('Khác','Khác'),
    ]
    username = forms.CharField(label='Tên đăng nhập', max_length=100, required=False)
    fullname = forms.CharField(label='Tên', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    phone_number = forms.CharField(label='Số điện thoại', max_length=100)
    address = forms.CharField(label='Địa chỉ', max_length=100)
    sex = forms.ChoiceField(label='Giới tính', choices=SEX_CHOICES, widget=forms.RadioSelect)
    dob = forms.DateField(label='Ngày sinh')
    avatar = forms.ImageField()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        
    def save(self, commit=True):
        user = CustomUser.objects.filter(username=self.request.user.username).first()
        user.fullname = self.cleaned_data.get("fullname")
        user.email = self.cleaned_data.get("email")
        user.phone_number = self.cleaned_data.get("phone_number")
        user.address = self.cleaned_data.get("address")
        user.sex = self.cleaned_data.get("sex")
        user.dob = self.cleaned_data.get("dob")
        user.avatar = self.cleaned_data.get("avatar")
        user.save()
