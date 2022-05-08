from app.models import Classes


def classes(request):
    return {"classes": Classes.objects.all()}