from app.database.models import UserSession 
from app.database.db import DB
from app.lib.exc import UserSessionExpired
from app.lib.logger import get_logger
from sqlalchemy.exc import NoResultFound
from datetime import datetime, timezone

class AuthSessionHelper:
    def __init__(self):
        self.user_logger = get_logger("user")

    # Create Session
    def create_user_session(self, user_id=None):
        db = DB()
        db.initialize()
        try:
            # Create a new user_session
            user_session = UserSession(user_id=user_id)

            # Add and commit the new session to the database
            db.session.add(user_session)
            db.session.commit()

            # Extract the data from the committed user_session
            session_data = {
                "user_id": str(user_session.user_id) if user_session.user_id else "", # Blank if guest_session
                "session_id": str(user_session.session_id),
                "start_time": user_session.start_time.isoformat(),
                "expiration_time": user_session.expiration_time.isoformat()
            }
            if user_id:
                print("\nAuthenticated user session created!!!\n")
            else:
                print("\nGuest user session created!!!\n")
        finally:
            db.close()
        
        return session_data
    
    # Get Session
    def get_user_session(self,session_id):
        db = DB()
        db.initialize()
        try:
            found_session = db.session.query(UserSession).filter_by(session_id=session_id).one()
            expiration_time = found_session.expiration_time
      
            # Ensure expiration_time is timezone-aware
            if expiration_time.tzinfo is None:
                expiration_time = expiration_time.replace(tzinfo=timezone.utc)

            now = datetime.now(timezone.utc)  # Always use timezone-aware datetime
            is_expired = expiration_time < now
            
            if is_expired:
                db.session.delete(found_session)
                db.session.commit()
                db.close()
                raise UserSessionExpired
            return found_session
        except NoResultFound as e:
            raise ValueError(e)
        finally:
            db.close()

    # Delete Session
    def delete_user_session(self, session_id):
        db = DB()
        db.initialize()
        try:
            # Query the session and delete it
            session_to_delete = db.session.query(UserSession).filter_by(session_id=session_id).one()
            db.session.delete(session_to_delete)
            db.session.commit()
            db.close()
            return True
        except NoResultFound:
            return False