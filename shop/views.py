from django.shortcuts import render
from .models import *
import io
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.contrib.auth.models import User
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .models import UserProfile


def home(request):
    users = User.objects.all()
    return render(request, 'home.html', locals())


def generate_user_profile_pdf(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Header
    styles = getSampleStyleSheet()
    header_text = Paragraph("User Profile Print Form", styles['Title'])
    elements.append(header_text)

    # Add a space
    elements.append(Spacer(1, 20))

    # User details
    user_details = [
        Paragraph(f"Username: {user.username}", styles['Normal']),
        Paragraph(f"First Name: {user.first_name}", styles['Normal']),
        Paragraph(f"Last Name: {user.last_name}", styles['Normal']),
        Paragraph(f"Email: {user.email}", styles['Normal']),
        Paragraph(f"Bio: {user_profile.bio}", styles['Normal']),
    ]

    elements.extend(user_details)

    # Add a space
    elements.append(Spacer(1, 20))

    # Educational Details
    edu_data = [
        ["Degree", "Institution", "Year"],
        ["Bachelor's", "University 1", "2020"],
        ["Master's", "University 2", "2022"],
        # Add more rows as needed
    ]

    edu_table = Table(edu_data)
    edu_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)),
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
    ]))

    elements.append(edu_table)

    doc.build(elements)
    buffer.seek(0)

    response = FileResponse(buffer)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = f'attachment; filename="{user}.pdf"'
    return response