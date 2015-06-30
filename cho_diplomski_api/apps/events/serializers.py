from rest_framework import serializers
from users.models import User
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
        repr['invitation_count'] = User.objects.count()
        repr['accepted_count'] = instance.invitations.filter(status=EventInvitation.STATUS.accepted).count()
        repr['rejected_count'] = instance.invitations.filter(status=EventInvitation.STATUS.rejected).count()
        return repr

    def to_internal_value(self, data):
        super(EventSerializer, self).to_internal_value(data)
        if 'invitation_status' in data and data['invitation_status'] in EventInvitation.STATUS:
            user = self.context['request'].user
            event = self.instance
            try:
                invitation = EventInvitation.objects.get(event=event, user=user)
                invitation.status = data['invitation_status']
                invitation.save()
            except EventInvitation.DoesNotExist:
                EventInvitation.objects.create(event=event, user=user, status=data['invitation_status'])
        return data
