*** Settings ***
Resource  ../../resources/pages/home_page.robot
Resource  ../../resources/pages/search_product_catalog.robot
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/login_page.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Variables ***
${SEARCH_PRODUCT}  barfi burgundy

*** Test Cases ***
TC003 Search product
    [Documentation]  Test case for searching a product
    [Tags]  functional

    Log in to application
    Sleep    20s
    Login Credentials  ${USER_EMAIL}  ${USER_PWD}

    Home page

    Search Product  ${SEARCH_PRODUCT}

TC008 Search non-existing product
    [Documentation]  Test case for searching non existing product
    [Tags]  functional

    Log in to application
    Sleep    20s
    Login Credentials    ${USER_EMAIL}    ${USER_PWD}

    Home page

    Search Non-existing Product    abc
