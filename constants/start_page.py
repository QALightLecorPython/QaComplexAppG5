class StartPageConstants:
    # Sign In
    SIGN_IN_USERNAME_FIELD_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_TEXT = 'Sign In'
    SIGN_IN_BUTTON_XPATH = f".//button[text()='{SIGN_IN_BUTTON_TEXT}']"
    SIGN_IN_LOGIN_ERROR_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_IN_LOGIN_ERROR_TEXT = "Invalid username / pasword"

    # Sign Up
    SIGN_UP_USERNAME_FIELD_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_FIELD_XPATH = ".//input[@id='email-register']"
    SIGN_UP_PASSWORD_FIELD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"
