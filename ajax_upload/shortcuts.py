import json

from django.http import HttpResponse, HttpResponseBadRequest

from ajax_upload.forms import UploadedFileForm


def upload_file(request):
    form = UploadedFileForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        uploaded_file = form.save()
        data = {
            'path': uploaded_file.file.url,
        }
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponseBadRequest(json.dumps({'errors': form.errors}))
