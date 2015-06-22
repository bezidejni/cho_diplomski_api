from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        applications_open = self.request.query_params.get('applications_open', None)
        if applications_open:
            if applications_open.lower() == 'true':
                queryset = queryset.applications_open()
            else:
                queryset = queryset.applications_closed()
        return queryset.order_by('id')
