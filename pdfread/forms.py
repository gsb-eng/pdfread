"""PDF reader forms"""

import os

from collections import OrderedDict
from django import forms
from django.core.exceptions import ValidationError

from PyPDF2 import PdfFileReader
from PyPDF2.utils import PdfReadError

VALID_EXTS = [".pdf"]


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in VALID_EXTS:
        raise ValidationError(u'Only PDF files are allowed')


class PDFReaderForm(forms.Form):

    password = forms.CharField(required=False, widget=forms.PasswordInput)
    pdf_file = forms.FileField()  # validators=[validate_file_extension])

    def __init__(self, *args, **kwargs):
        super(PDFReaderForm, self).__init__(*args, **kwargs)

        # Djnago validates form fields in certain un-predictable order
        # If we need any fields having dependecies on another fields, this
        # re-ordering offields works.
        ordered_fields = ["pdf_file", "password"]

        _ = [
            k for k in self.fields.keys() if k not in ordered_fields] + \
            ordered_fields
        self.fields = OrderedDict((k, self.fields[k]) for k in _)

    def clean_pdf_file(self):
        pdf_file = self.cleaned_data.get("pdf_file")
        if pdf_file:
            try:
                pdf = PdfFileReader(pdf_file)
                self.cleaned_data["is_encrypted"] = pdf.isEncrypted
                self.cleaned_data["pdf"] = pdf
            except PdfReadError:
                raise forms.ValidationError(
                   "Only PDF files are allowed!!"
                )
        else:
            raise forms.ValidationError(
                "No pdf file uploaded!"
            )
        return pdf_file

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if self.cleaned_data.get("is_encrypted"):
            if not password:
                raise  forms.ValidationError(
                    (
                        "PDF file is password protected, please provide "
                        "the password to load the file"
                    )
                )
            else:
                pdf = self.cleaned_data.get("pdf")
                response_code = pdf.decrypt(str(password))
                if response_code == 0:
                    raise forms.ValidationError(
                        "Password is wrong, please enter correct one"
                    )
        return password
