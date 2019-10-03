from .shortcuts import get_current_usersettings
from django.utils.deprecation import MiddlewareMixin


class CurrentUserSettingsMiddleware(MiddlewareMixin):
    """
    Middleware that sets `usersettings` attribute to request object.
    """

    def process_request(self, request):
        request.usersettings = get_current_usersettings()
