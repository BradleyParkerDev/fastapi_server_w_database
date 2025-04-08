class UserSessionExpired(Exception):
    def __init__(self,message='User session has expired!!!'):
        super().__init__(message)
