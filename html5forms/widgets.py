from django.forms import widgets

#refreshing old widgets
class DateInputHTML5(widgets.DateInput):
    input_type = 'date'
    
class DateTimeInputHTML5(widgets.DateTimeInput):
    input_type = 'datetime'
    
class TimeInputHTML5(widgets.TimeInput):
    input_type = 'time'

#new widgets
class EmailInputHTML5(widgets.Input):
    input_type = 'email'

class URLInputHTML5(widgets.Input):
    input_type = 'url'

class NumberInputHTML5(widgets.Input):
    input_type = 'number'
    format = '%d'     # '14.3'

    def __init__(self, attrs=None, format=None):
        super(NumberInputHTML5, self).__init__(attrs)
        if format:
            self.format = format

    def _format_value(self, value):
        return self.format % (int(float(value)), )

    def _has_changed(self, initial, data):
        return self._format_value(initial) != self._format_value(data)
    
class RangeInputHTML5(NumberInputHTML5):
    input_type = 'range'
    
class SearchInputHTML5(widgets.Input):
    input_type = 'search'
    

