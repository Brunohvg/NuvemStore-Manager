from django import forms


class CommentForm(forms.Form):
    user_email = forms.EmailField(
        label="Email", required=True, initial="example@example.com"
    )
    user_password = forms.CharField(
        label="Password", widget=forms.PasswordInput(), required=True
    )
