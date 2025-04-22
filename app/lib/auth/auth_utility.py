from fastapi import Request, Response
from .auth_helpers import AuthSessionHelper, AuthTokenHelper
from app.lib.exc import UserSessionExpired
from datetime import datetime, timedelta, timezone

class AuthUtility():
    def __init__(self):
        self.session = AuthSessionHelper()
        self.token = AuthTokenHelper()
 
    # Create Guest Session
    def create_guest_session_and_token(self):
        guest_session = self.session.create_user_session()

        # Use the expiration time from the database (already set to UTC)
        # Ensure expiration_time is a string before conversion
        expiration_time = guest_session['expiration_time']
        
        if isinstance(expiration_time, str):  # Convert if it's a string
            expiration_time = datetime.fromisoformat(expiration_time)
        
        # Ensure it's timezone-aware
        expiration_time = expiration_time.replace(tzinfo=timezone.utc)
        
        token_exp = int(expiration_time.timestamp())  # Convert to Unix timestamp

        token_payload = {
            "session_type": "guest",
            "session_id": guest_session['session_id'],
            "start_time": guest_session['start_time'],
            "exp": token_exp            
        }
        print(f"session expiration_time: {guest_session["expiration_time"]}")
        guest_session_token = self.token.generate_session_token(token_payload)
        return {"token": guest_session_token, "payload": token_payload}

    # Middleware 
    async def authorize_user(self, request: Request, call_next):

        print("\nAuthorization Middleware!!!")

        # Retrieve session token from the request
        session_token = request.cookies.get("session_cookie")
        guest_session_data = None  # Ensure it's always defined

        # If a session token is present, attempt to decode it
        if session_token:
            print(f"\nsession_token:\n{session_token}\n")
            try:
                decoded_token = self.token.verify_session_token(session_token)
                if decoded_token:
                    try:
                        # Check if session exists in the database
                        found_session = self.session.get_user_session(decoded_token['session_id'])
                        print(f"session_type: {decoded_token['session_type']}")
                        print(f"user_id: {decoded_token.get(' user_id') or 'N/A'}")
                        print(f"session_id: {decoded_token['session_id']}")
                        print(f"start_time: {decoded_token['start_time']}")
                        print(f"exp: {decoded_token['exp']}\n")
                        request.state.session_data = decoded_token                              
                    except UserSessionExpired as e:
                        print(f"Session Expired: {e}\n")
                        print("Deleting user session and token...")
                        self.session.delete_user_session(decoded_token['session_id'])
                        session_token = None

            except (ValueError, Exception) as e:
                print(f"Error: {e}\n")
                session_token = None

        # If there's no valid session token
        if not session_token:
            print("session_token not found or invalid...")
            guest_session_data = self.create_guest_session_and_token()
            session_token = guest_session_data['token']
            request.state.session_data = guest_session_data['payload']

        response = await call_next(request) 

        # Only set a session cookie if a new session was created
        if guest_session_data:
            response.set_cookie(
                key="session_cookie",
                value=session_token,
                httponly=True,
                path="/",
                samesite="Lax",
                max_age=60*60*24*7  # 7 days
            )

        return response
 