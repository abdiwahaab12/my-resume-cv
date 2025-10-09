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
    
    # Run database migration
    print("🔄 Running database migration...")
    try:
        from migrate_database import migrate_database
        if migrate_database():
            print("✅ Database migration completed successfully!")
        else:
            print("❌ Database migration failed!")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Migration error: {e}")
        sys.exit(1)
    
    # Import and run the app
    from app import app
    
    # Get port from environment (for Railway/Render)
    port = int(os.environ.get('PORT', 5000))
    
    print(f"🌍 Starting server on port {port}")
    print("📱 Your resume website is now live!")
    print("🔧 Admin panel: /admin (username: admin, password: admin123)")
    
    app.run(host='0.0.0.0', port=port, debug=False)

if __name__ == '__main__':
    main()
