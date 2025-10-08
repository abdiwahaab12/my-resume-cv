#!/usr/bin/env python3
"""
Simple deployment script for Flask resume website
"""
import os
import sys

def main():
    print("🚀 Starting Flask Resume Website...")
    
    # Set environment variables if not set
    if not os.environ.get('SECRET_KEY'):
        os.environ['SECRET_KEY'] = 'my-super-secret-key-12345-abdiwahab-resume-website-2025'
    
    # Force unset DATABASE_URL to use SQLite
    if 'DATABASE_URL' in os.environ:
        print(f"🔍 Removing invalid DATABASE_URL: {os.environ.get('DATABASE_URL')}")
        del os.environ['DATABASE_URL']
    
    print("🔍 Using SQLite database configuration")
    
    # Import and run the app
    from app import app, db, User
    from werkzeug.security import generate_password_hash
    
    # Initialize database and create admin user if needed
    with app.app_context():
        try:
            db.create_all()
            # Check if admin user exists, if not create it
            admin_user = User.query.filter_by(username='admin').first()
            if not admin_user:
                admin_user = User(
                    username='admin',
                    email='admin@example.com',
                    password_hash=generate_password_hash('admin123')
                )
                db.session.add(admin_user)
                db.session.commit()
                print("✅ Admin user created successfully")
            else:
                print("✅ Admin user already exists")
        except Exception as e:
            print(f"⚠️ Database initialization warning: {e}")
    
    # Get port from environment (for Railway/Render)
    port = int(os.environ.get('PORT', 5000))
    
    print(f"🌍 Starting server on port {port}")
    print("📱 Your resume website is now live!")
    print("🔧 Admin panel: /admin (username: admin, password: admin123)")
    
    app.run(host='0.0.0.0', port=port, debug=False)

if __name__ == '__main__':
    main()
