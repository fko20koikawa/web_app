# seisaku/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    question_title = forms.CharField(label='件名')
    question_detail = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'お名前を入力してください',
            'class': 'form-control'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'メールアドレスを入力してください',
            'class': 'form-control'
        })
        self.fields['question_title'].widget.attrs.update({
            'placeholder': '件名を入力してください。',
            'class': 'form-control'
        })
        self.fields['question_detail'].widget.attrs.update({
            'placeholder': 'お問い合わせ内容を入力してください。',
            'class': 'form-control'
        })
