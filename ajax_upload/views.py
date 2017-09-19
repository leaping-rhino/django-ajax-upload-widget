from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ajax_upload import shortcuts


@csrf_exempt
@require_POST
def upload(request):
    return shortcuts.upload_file(request)
