#!/usr/bin/env python3
"""
Update education with Abdiwahab's complete educational background
"""

import sys
import os
from datetime import datetime, date
import json

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, Education

def update_education():
    """Update education with complete background"""
    print("Updating education...")
    
    with app.app_context():
        # Clear existing education
        Education.query.delete()
        
        # Add Complete Education Background
        educations_data = [
            {
                'degree': 'Bachelor of Computer Science',
                'institution': 'Jomhuria University',
                'location': 'Mogadishu, Somalia',
                'start_date': date(2021, 9, 1),
                'end_date': date(2025, 6, 1),
                'current': False,
                'description': 'Comprehensive computer science education with focus on software development, programming, database management, and system design.',
                'gpa': 3.5
            },
            {
                'degree': 'Diploma in Accounting',
                'institution': 'Al-Imra University',
                'location': 'Mogadishu, Somalia',
                'start_date': date(2023, 9, 1),
                'end_date': date(2024, 6, 1),
                'current': False,
                'description': 'Professional accounting and financial management training covering financial reporting, tax preparation, and business accounting principles.',
                'gpa': 3.7
            },
            {
                'degree': 'Primary and Secondary Education',
                'institution': 'Al Anwaar Primary and Secondary School',
                'location': 'Dhame Yasin Cartan, Somalia',
                'start_date': date(2016, 9, 1),
                'end_date': date(2020, 6, 1),
                'current': False,
                'description': 'Complete primary and secondary education foundation covering core subjects including mathematics, science, languages, and social studies.',
                'gpa': 3.8
            }
        ]
        
        for edu_data in educations_data:
            education = Education(**edu_data)
            db.session.add(education)
        
        db.session.commit()
        print("✅ Education updated successfully!")
        print("\n📋 Your Educational Background:")
        for edu in educations_data:
            print(f"  • {edu['degree']}")
            print(f"    {edu['institution']} ({edu['start_date'].year} - {edu['end_date'].year})")
            print(f"    Location: {edu['location']}")
            print(f"    GPA: {edu['gpa']}")
            print()

if __name__ == '__main__':
    update_education()
