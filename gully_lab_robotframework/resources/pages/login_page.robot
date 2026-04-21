*** Settings ***
Resource  ../../locators/login_page_loc.robot
Resource  ../common_resources.robot

*** Keywords ***
Login Credentials
    [Documentation]  Log in page
    [Arguments]  ${email}  ${psswd}

    Input Text    ${email_field}    ${email}
    Log  entering email in email field

    Input Text    ${psswd_field}    ${psswd}
    Log  entering password in password field

    Click Element    ${sign_btn}
    Log  clicking on sign in button

    Sleep  5s

    Page Should Contain   Account
    Log  validating the existence of "Account" in page

    Page Should Contain    Log out
    Log  validating the existence of "Log out" in page

Login Invalid Credentials
    [Documentation]  Log in page
    [Arguments]  ${email}  ${psswd}

    Input Text    ${email_field}    ${email}
    Log  entering email in email field

    Input Text    ${psswd_field}    ${psswd}
    Log  entering password in password field

    Click Element    ${sign_btn}
    Log  clicking on sign in button

    Sleep  5s
    Page Should Contain    Incorrect email or password.