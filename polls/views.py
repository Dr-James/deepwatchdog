from django.http import HttpResponse
from polls.models import Picture, User


# Create your views here.
def index(request):
    return HttpResponse("Hey DWD, you're at the polls index.")


def picture(request, picture_id):
    image = Picture.objects.get(id=picture_id)
    return HttpResponse(image.picture.url)


#user_id is actually the number of the picture, which is why we must calculate the correct id of the user of that picture.
def user(request, user_id):
    response = "%s is the User of Picture %s."
    user_id_for_image = Picture.objects.get(id=user_id).user.id
    username = User.objects.get(id=user_id_for_image).username
    return HttpResponse(response % (username, user_id))
