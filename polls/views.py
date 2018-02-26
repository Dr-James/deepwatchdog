from django.http import HttpResponse
from polls.models import Picture

# Create your views here.
def index(request):
    return HttpResponse("Hey DWD, you're at the polls index.")

def picture(request, picture_id):
    response = "You're looking at the page of picture %s:."
    image = Picture.objects.get(id=picture_id)
    return HttpResponse(response % picture_id, render(image.picture))
    #media/media/media/anakinhappy_y9obbgD.png


def user(request, user_id):
    response = "You're looking at the page of user %s."
    return HttpResponse(response % user_id)