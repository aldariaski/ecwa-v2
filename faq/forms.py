from django import forms

class Question(forms.Form):
    fields = ["pertanyaan"]
    error_messages = { "required": "masih kosong"}
    format_pesan = {"placeholder":"Masukkan pertanyaan dari Anda", "class" : "align-items-center justify-content-center form-control"}
    pertanyaan = forms.CharField(required = True, widget=forms.Textarea(attrs=format_pesan))