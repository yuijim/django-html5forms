Django HTML5Forms
=================

Django HTML5Forms is a little piece of code, that allows to take advantage of the new HTML5 input types. It also contains few templates for quick form rendering.

Usage
-----

Subclass either HTML5Form or HTML5ModelForm and let it do the rest ;). Alternatively, take a look at widgets.py.

**Warning:** Validators defined in the Model fields are not automatically transferred - if you need validators (min/max) you need to specify them in the HTML5ModelForm class again.

License
-------

django-html5forms is distributed under New BSD License.
