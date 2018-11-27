from django import forms
from crispy_forms.helper import FormHelper


class EventListFormHelper(FormHelper):
    form_id = 'search-form'
    form_class = 'form-inline'
    field_template = 'bootstrap4/layout/inline_field.html'
    field_class = 'col-xs-3'
    label_class = 'col-xs-3'
    form_show_errors = True
    help_text_inline = False
    html5_required = True
    layout = Layout(
                Fieldset(
                    '<input type="text" class="form-control">"Search Events"',
                    InlineField('user'),
                    InlineField('type'),
                    InlineField('duration'),
                    InlineField('title'),
                ),
                FormActions(
                    StrictButton(
                        '<div class="input-group-prepend"></div>"Search"',
                        type='submit',
                        css_class='btn btn-outline-secondary',
                        style='margin-top:10px;'
                    )
                )
    )
