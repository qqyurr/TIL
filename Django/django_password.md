# 0917 django

https://docs.djangoproject.com/en/3.1/ref/contrib/messages/

from django.contrib import messages

messages.add_message(request, messages.SUCCESS,'회원가입 성공!')

```python
def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
```

```python
class PasswordChangeForm(SetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """
    error_messages = {
        **SetPasswordForm.error_messages,
        'password_incorrect': _("Your old password was entered incorrectly. Please enter it again."),
    }
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )

    field_order = ['old_password', 'new_password1', 'new_password2']

    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password

```

#### 비밀번호 변경

PasswordChangeForm 이용

```python
@login_required
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save() # 새로운 패스워드 저장
            update_session_auth_hash(request, user) # 암호 변경 시 세션 무효화 방지
            # request 객체에서 메시지 추가하기
            messages.add_message(request, messages.SUCCESS,'비밀번호 변경 성공!!')
            return redirect('accounts:user_list')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/password.html', context)
```

