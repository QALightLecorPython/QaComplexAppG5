class CreatePostPageConsts:
    TITLE_FIELD_XPATH = ".//input[@id='post-title']"
    BODY_FIELD_XPATH = ".//textarea[@id='post-body']"
    CREATE_POST_BUTTON_XPATH = ".//button[@class='btn btn-primary']"
    SUCCESS_MESSAGE_XPATH = ".//div[@class='alert alert-success text-center']"
    SUCCESS_MESSAGE_TEXT = "New post successfully created."
    UNIQUE_POST_CHECKBOX_XPATH = ".//input[@name='uniquePost']"
    VISIBILITY_LIST_XPATH = ".//select[@id='select1']"
    OPTION_ALL_USERS = "All Users"
    OPTION_GROUP_MESSAGE = "Group Message"
    OPTION_ONE_PERSON = "One Person"
    VISIBILITY_SELECTION_XPATH = ".//option[@value='{option}']"
    CREATED_TITLE_XPATH = ".//h2"
    CREATED_VISIBILITY_VALUE_XPATH = ".//u"
    IS_POST_UNIQUE_XPATH = ".//p[contains(text(), 'Is this post unique?')]"
    CREATED_BODY_CONTENT_XPATH = (
        ".//div[@class='body-content']/p[contains(text(), '{body}')]"
    )
    PROFILE_LINK_XPATH = ".//a[@href='/profile/{username}']"
