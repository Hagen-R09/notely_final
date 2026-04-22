from database import get_db, init_db
import bcrypt

def seed_database():
        """add sample users to the database"""
        init_db()

        conn = get_db

        
    
        sample_entries = [
            ('interesting', 'today was interesting')
        ]