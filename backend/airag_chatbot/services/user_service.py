from fastapi import Depends, HTTPException, status

async def user_sign_up_service():
    try:
        
        return True
    
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                             detail=f"An error occured during signup {str(e)}")