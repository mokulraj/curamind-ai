from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from appointments.models import Appointment
from django.contrib.auth import get_user_model

User = get_user_model()


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.role == "ADMIN":
            return Response({
                "role": "ADMIN",
                "total_users": User.objects.count(),
                "total_appointments": Appointment.objects.count(),
                "doctors": User.objects.filter(role="DOCTOR").count(),
                "patients": User.objects.filter(role="PATIENT").count(),
            })

        if user.role == "DOCTOR":
            return Response({
                "role": "DOCTOR",
                "your_appointments": Appointment.objects.filter(doctor=user).count(),
                "upcoming": Appointment.objects.filter(
                    doctor=user,
                    status="SCHEDULED"
                ).count(),
            })

        if user.role == "PATIENT":
            return Response({
                "role": "PATIENT",
                "your_appointments": Appointment.objects.filter(patient=user).count(),
                "completed": Appointment.objects.filter(
                    patient=user,
                    status="COMPLETED"
                ).count(),
            })

        return Response({"message": "Invalid role"})