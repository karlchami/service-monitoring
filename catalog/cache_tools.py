from datetime import datetime, timedelta
from functools import wraps
from pytz import timezone, utc
from django.utils.cache import (get_cache_key, learn_cache_key)
from django.utils.cache import patch_cache_control
from django.core.cache import cache



def seconds_until_update():
    """
    Returns seconds until next update.
    """
    # pytz is a bit tricky. Doing everything relative to UTC prevents inconsitencies.
    now_utc = utc.localize(datetime.utcnow())

    now_east = now_utc.astimezone(timezone('US/Eastern'))

    today_noon =  now_east.replace(hour=11, minute=59, second=59)
    today_midnight =  now_east.replace(hour=23, minute=59, second=59)

    # DB updates twice a day: at noon and at midnight
    # The cache will be cleared via a webhook,this is just a failsafe.
    if now_east > today_noon:
        return ((today_midnight-now_east) + timedelta(minutes=30)).seconds

    return ((today_noon-now_east ) + timedelta(minutes=30)).seconds


def custom_cache_page():
    """
    This is a custom cache decorator, similar to Django's native cache_page
    In fact, many of the methods are taken from UpdateCacheMiddleware and FetchFromCacheMiddleware
    This was done to avoid the adding of max-age=someNumber in the response header whilst still allowing for clean and re-usable code.
    This will only cache on the backend until expiry and tell the frontend to never cache the response.

    Read more here on the headers: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control
    """
    def _cache_controller(viewfunc):
        @wraps(viewfunc)
        def _cache_controlled(request, *args, **kw):
            cache_key = get_cache_key(request)
            response = cache.get(cache_key)
            if response is None:
                expire = seconds_until_update()
                response = viewfunc(request, *args, **kw)
                if response.status_code == 200:
                    cache_key = learn_cache_key(request, response)
                    if hasattr(response, 'render') and callable(response.render):
                        response.add_post_render_callback(
                            lambda r: cache.set(cache_key, r, expire)
                        )
                    else:
                        cache.set(cache_key, response, expire)
            patch_cache_control(response, no_store=True)
            return response

        return _cache_controlled

    return _cache_controller
