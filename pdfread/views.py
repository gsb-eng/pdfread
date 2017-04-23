"""PDF read process views"""

from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render

from pdfread.forms import PDFReaderForm


class PDFReader(View):

    """PDF Reader view"""

    def get(self, request):
        
        return render(
            request,
            'pdf_reader.tpl',
            {"form": PDFReaderForm}
        )

    def post(self, request):
        success = failure = ""
        form = PDFReaderForm(request.POST, request.FILES)
        if form.is_valid():
            success = "File successfully decrypted!"
        else:
            failure = "In correct password, please try with correct password"
        return render(
            request,
            'pdf_reader.tpl',
            {'success': success, "failure": failure, "form": form}
        )
