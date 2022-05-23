# from django.db.models import F
# from hitcount.views import HitCountMixin
# from hitcount.utils import get_hitcount_model



# def update_object_views(request, object):
#     context = {}
#     hit_count = get_hitcount_model().objects.get_for_object(object)
#     hits = hit_count.hits
#     hitcontext = context["hitcount"] = {"pk": hit_count.pk}
#     hit_count_response = HitCountMixin.hit_count(request, hit_count)

#     if hit_count_response.hit_counted:
#         hits = F('hits') + 1 # Race condition fixed here
#         hitcontext["hitcounted"] = hit_count_response.hit_counted
#         hitcontext["hit_message"] = hit_count_response.hit_message
#         hitcontext["total_hits"] = hits


