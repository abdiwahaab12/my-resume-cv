#!/usr/bin/env python3
"""
Database migration script to add the 'read' column to the Message table
This script handles both local and production database migrations
"""
import os
import sys
import sqlite3
from app import app, db

def migrate_database():
    """Add the read column to the Message table if it doesn't exist"""
    print("🔄 Starting database migration...")
    
    try:
        with app.app_context():
            # Get the database path
            db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')
            
            if not os.path.exists(db_path):
                print(f"📁 Creating database at: {db_path}")
                # Create the database directory if it doesn't exist
                os.makedirs(os.path.dirname(db_path), exist_ok=True)
                # Create all tables
                db.create_all()
                print("✅ Database and tables created successfully!")
                
                # Only create admin user and sample data if this is a completely new database
                print("🔧 Setting up initial data...")
                from database_setup import create_admin_user, create_sample_data
                create_admin_user()
                create_sample_data()
                print("✅ Initial data setup completed!")
                return True
            
            print(f"📁 Database found at: {db_path}")
            
            # Connect to the database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Check if the read column already exists
            cursor.execute("PRAGMA table_info(message)")
            columns = [column[1] for column in cursor.fetchall()]
            
            if 'read' in columns:
                print("✅ Column 'read' already exists in the message table")
                conn.close()
                return True
            
            print("🔧 Adding 'read' column to message table...")
            
            # Add the read column with default value False
            cursor.execute("ALTER TABLE message ADD COLUMN read BOOLEAN DEFAULT 0")
            
            # Update existing messages to have read=False (they should already be False by default)
            cursor.execute("UPDATE message SET read = 0 WHERE read IS NULL")
            
            # Commit the changes
            conn.commit()
            conn.close()
            
            print("✅ Successfully added 'read' column to the message table")
            
            # Test the migration
            print("🧪 Testing migration...")
            from app import Message
            unread_count = Message.query.filter_by(read=False).count()
            total_count = Message.query.count()
            print(f"📊 Total messages: {total_count}")
            print(f"📊 Unread messages: {unread_count}")
            
            return True
            
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False

def main():
    """Main function to run the migration"""
    print("🚀 Database Migration Script")
    print("=" * 50)
    
    success = migrate_database()
    
    if success:
        print("\n✅ Migration completed successfully!")
        print("🎉 Your application should now work without errors!")
    else:
        print("\n❌ Migration failed!")
        print("Please check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
