*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://sauce-demo.myshopify.com/account/login
*** Test Cases ***
Login
    Open Browser  ${url}  chrome
    Login Success  pwd=iamironman  email=cheeseburger@gmail.com
*** Keywords ***
Login Success
    [Arguments]  ${email}  ${pwd}
    Input Text    id=customer_email    ${email}
    Input Text    id=customer_password    ${pwd}
