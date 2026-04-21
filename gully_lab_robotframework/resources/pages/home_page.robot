*** Settings ***
Library  SeleniumLibrary
#Resource  ../common_resources.robot
Resource  ../../locators/home_page_locators.robot
*** Keywords ***
Log in to application
    [Documentation]  logging in to account
    Click Element    ${account}
#Search in application
#    Click Element    ${search}
Home page
    [Documentation]  redirecting to home page
    Click Element    ${home}