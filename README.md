# Django Advanced Search

Django admin mixin for advanced search inspired by sentry, github and discord search

## Screenshot

![Screenshot](https://raw.githubusercontent.com/sandbox-pokhara/django-advanced-search/master/screenshot.png)

## Installation

```
pip install django-advanced-search
```

## Usage

```python
from django_advanced_search import AdvancedSearchMixin


class MyAdmin(AdvancedSearchMixin, admin.ModelAdmin):
    advanced_search_fields = [
        "id",
        "champion__name",
        "tier",
        "value",
    ]
```
