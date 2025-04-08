import os
import jwt
import time
from jwt import ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

# Load environment varibles 
load_dotenv()
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

class AuthTokenHelper:
    def __init__(self):
        self.jwt_secret_key = JWT_SECRET_KEY
        if not self.jwt_secret_key:
            raise ValueError("JWT_SECRET_KEY environment variable not set!!!")
        
    def generate_session_token(self, session_payload):
        print(f"token exp:{session_payload['exp']}")
        # Create token
        session_token = jwt.encode(session_payload, self.jwt_secret_key, algorithm="HS256")

        user_id = session_payload.get('user_id', None)
        if user_id:
            print(f"authenticated_session_token:\n{session_token}")
        else:
            print(f"guest_session_token:\n{session_token}")
        return session_token
    
    def verify_session_token(self, session_token):
        try:
            system_time = time.time()  # Get current Unix timestamp
            decoded_token = jwt.decode(session_token, self.jwt_secret_key, algorithms=["HS256"])
            
            print(f"\nDecoded Token Exp: {decoded_token['exp']}")
            print(f"Current System Unix Time: {system_time}")
            print(f"Time Difference (Exp - Now): {decoded_token['exp'] - system_time} seconds\n")
            
            return decoded_token

        except ExpiredSignatureError as e:
            print("Token has expired!!!")
            print(f"Error: {e}")            
            raise ValueError("Token expired!")
        except InvalidTokenError as e:
            print("Invalid token!!!")
            print(f"Error: {e}")
            return e