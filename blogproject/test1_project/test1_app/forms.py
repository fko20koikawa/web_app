from django import forms

class Test1AppForm(forms.Form):
    name = forms.CharField(label='お名前')
    tell = forms.CharField(label='電話番号')
    email = forms.EmailField(label='Mail')
    address = forms.CharField(label='住所')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = '名前を入力'
        self.fields['name'].widget.attrs['class'] = 'form-control'

        self.fields['tell'].widget.attrs['placeholder'] = '電話番号を入力'
        self.fields['tell'].widget.attrs['class'] = 'form-control'
        
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        
        self.fields['address'].widget.attrs['placeholder'] = '住所を入力'
        self.fields['address'].widget.attrs['class'] = 'form-control'
