*** Settings ***
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/logout_page.robot
Resource    ../../resources/pages/home_page.robot
Resource    ../../resources/pages/login_page.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application
*** Test Cases ***
TC002 Logout-User
    [Documentation]  Test case for logging out of account
    [Tags]  functional

    Log in to application
    Login Credentials    ${USER_EMAIL}    ${USER_PWD}

    Logout