*** Settings ***
Resource  ../../locators/home_page_locators.robot
Resource  ../../locators/add_cart_loc.robot
Library    SeleniumLibrary

*** Keywords ***
Open Product
    [Documentation]  clicking on search icon

    Click Element  ${product_card}
    Scroll Element Into View    ${gender}
    Click Element    ${gender}
    Click Element    ${size}
    Sleep    3s
    Mouse Over    ${quantity}
    Click Element    ${quantity}
    Input Text    ${quantity}    3
    Wait Until Element Is Visible    ${add_to_cart}    10s
    Click Element    ${add_to_cart}

