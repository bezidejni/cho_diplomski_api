from rest_framework import serializers
from .models import Event, EventInvitation


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'location', 'start', 'end', 'application_deadline')

    def to_representation(self, instance):
        repr = super(EventSerializer, self).to_representation(instance)
        try:
            invitation = instance.invitations.get(user=self.context['request'].user)
        except EventInvitation.DoesNotExist:
            invitation = None
        repr['invitation_status'] = invitation.status if invitation else 'pending'
        return repr
