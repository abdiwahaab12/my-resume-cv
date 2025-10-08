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
    
    # Don't set DATABASE_URL - let the app use its default SQLite configuration
    
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
