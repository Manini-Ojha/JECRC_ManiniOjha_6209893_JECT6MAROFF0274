*** Settings ***
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/search_product_catalog.robot
Resource  ../../resources/pages/add_to_cart_page.robot
Resource  ../../resources/pages/home_page.robot
Resource  ../../resources/pages/login_page.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Variables ***
${SEARCH_PRODUCT}  barfi burgundy

*** Test Cases ***
TC004 Add product to cart
    Log in to application
    Login Credentials    ${USER_EMAIL}    ${USER_PWD}
    Home page
    Search Product    ${SEARCH_PRODUCT}
    Open Product
