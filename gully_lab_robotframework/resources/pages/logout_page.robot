*** Settings ***
Resource  ../../locators/logout_page_loc.robot
Resource  ../common_resources.robot
Resource  ../../locators/home_page_locators.robot

*** Keywords ***
Logout
    [Documentation]  log out

    Click Element    ${account}

    Click Element    ${logout}