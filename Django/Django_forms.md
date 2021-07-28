# Django forms

> app 폴더에서 forms.py에 작성

```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
```

> views.py

```python
from .forms import AritlceForm
```

```python
def new(request):
    form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html',context)
```

> new.html

```python
{{ form }}
{{ form.as_p }}
```

