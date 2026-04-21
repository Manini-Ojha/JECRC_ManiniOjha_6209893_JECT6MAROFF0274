*** Settings ***
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/login_page.robot
Resource    ../../resources/pages/home_page.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Variables ***
${EMAIL}  ojhamanini22@gmail.com
${PSSWD}  Eti@2004

*** Test Cases ***
TC001 Login-User
    [Documentation]  Test case for logging in the user
    [Tags]  functional

    Log in to application

    Login Credentials    ${USER_EMAIL}    ${USER_PWD}

TC007 Invalid-Credentials
    [Documentation]  Test case for invalid credentials
    [Tags]  functional

    Log in to application
    Login Invalid Credentials    abcd    efggh
