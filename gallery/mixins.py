from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render, redirect

class ArtistRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:login')
        elif not request.user.is_artist:
            return redirect('gallery:artist-list')
        else:
            return super().dispatch(request, *args, **kwargs)