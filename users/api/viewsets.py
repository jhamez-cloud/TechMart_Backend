from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from users.serializers import UserProfileSerializer #pylint:disable=e0401
from users.models import UserProfile #pylint:disable=e0401

class UserProfileViewset(ModelViewSet):
    '''Documentation String'''
    permission_classes = [AllowAny]

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['firebase_uid']

    @action(detail=False, methods=['patch'], url_path='update-by-uid')
    def update_by_uid(self, request):
        '''Documentation String'''
        uid = request.data.get('firebase_uid')

        try:
            user = UserProfile.objects.get(firebase_uid=uid)
        except UserProfile.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
