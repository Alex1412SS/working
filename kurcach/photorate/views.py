from django.shortcuts import render, redirect
from .models import photos, Rating
from.forms import CreatePhotoForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse


def photo_rate(request):
    post = photos.objects.order_by('-ratings')
    return render(request, "photorate/photopage.html", {'post': post})



def create(request):
    if request.method == 'POST':
        form = CreatePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'photorate/create.html', {'form': form, 'img_obj': img_obj})
    form = CreatePhotoForm
    data = {"form": form}
    return render(request, "photorate/create.html", data)


class RatingCreateView(View):
    model = Rating

    def post(self, request, *args, **kwargs):
        article_id = request.POST.get('article_id')
        value = int(request.POST.get('value'))
        user = request.user if request.user.is_authenticated else None

        rating, created = self.model.objects.get_or_create(
            article_id=article_id,
            defaults={'value': value, 'user': user},
        )

        if not created:
            if rating.value == value:
                rating.delete()
                return JsonResponse({'status': 'deleted', 'rating_sum': rating.article.get_sum_rating()})
            else:
                rating.value = value
                rating.user = user
                rating.save()
                return JsonResponse({'status': 'updated', 'rating_sum': rating.article.get_sum_rating()})
        return JsonResponse({'status': 'created', 'rating_sum': rating.article.get_sum_rating()})