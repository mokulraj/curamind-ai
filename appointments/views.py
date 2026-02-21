from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Admin sees everything
        if user.role == "ADMIN":
            return Appointment.objects.all()

        # Doctor sees their appointments
        if user.role == "DOCTOR":
            return Appointment.objects.filter(doctor=user)

        # Patient sees their appointments
        if user.role == "PATIENT":
            return Appointment.objects.filter(patient=user)

        return Appointment.objects.none()