from django.conf import settings


PAGINATE_BY = getattr(settings, "DEDAL_PAGINATE_BY", 10)
