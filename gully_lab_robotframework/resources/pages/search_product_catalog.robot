*** Settings ***
Resource  ../../locators/search_locators.robot
Resource  ../common_resources.robot
Resource  ../../locators/home_page_locators.robot

*** Keywords ***
Search Product
    [Documentation]  clicking on search icon
    [Arguments]  ${product_name}

    Click Element    ${search_icon}

    Input Text    ${search_input}    ${product_name}

    Press Keys    ${search_input}    ENTER
Search Non-existing Product
    [Documentation]  clicking on search icon
    [Arguments]  ${product_name}

    Click Element    ${search_icon}

    Input Text    ${search_input}    ${product_name}

    Press Keys    ${search_input}    ENTER
    
    Page Should Contain    No results found