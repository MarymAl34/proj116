# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    # ترجمة رسالة عدم تطابق كلمتي المرور
    error_messages = {
        'password_mismatch': _('كلمتا المرور غير متطابقتين.'),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # إزالة التعليمات وتحسين المظهر العام لكل حقل
        for field_name, field in self.fields.items():
            field.help_text = ''
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': ''
            })

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
        labels = {
            'username': _('اسم المستخدم'),
            'email': _('البريد الإلكتروني'),
            'phone_number': _('رقم الجوال'),
            'password1': _('كلمة المرور'),
            'password2': _('تأكيد كلمة المرور'),
        }
        help_texts = {
            'username': '',
            'email': '',
            'phone_number': '',
            'password1': '',
            'password2': '',
        }
        error_messages = {
            'username': {
                'unique': _('اسم المستخدم مستخدم بالفعل.'),
            },
            'email': {
                'unique': _('البريد الإلكتروني مستخدم بالفعل.'),
            },
        }
