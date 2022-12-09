*** Settings ***
Library    ../libraries/MySteps.py
Suite Setup    Start WebDriver
Suite Teardown    Close WebDriver
Test Timeout    10s

*** Variables ***
${LOGIN}    katerina_test
${PASSWORD}     katerina_pass


*** Test Cases ***
Log in test
    Click Login Button
    ${check}=    Login Button Is Presented
    Should Be True  ${check}
    Set Up Login And Password   ${LOGIN}    ${PASSWORD}
    ${check}=    Log out button is presented
    Should Be True   ${check}
    ${check}=    Welcome message is presented    ${LOGIN}
    Should Be True  ${check}

Cart test
    Click on Monitors category
    Click on the product with the highest price on the page
    ${product_name_PLP}=     Get Highest Price Product Name
    ${product_price_PLP}=    Get Highest Price Product Price
    ${check}=       products page with is open      ${product_name_PLP}         ${product_price_PLP}
    Should Be True      ${check}

    Click on Add to cart button
    Click on Cart button
    ${bbbb}=    product is successfully added to cart
    Should Be True     ${bbbb}
    ${product_name_cart}=    Get product name text
    ${product_price_cart}=    Get product price text
    Should Be Equal    ${product_name_PLP}  ${product_name_cart}
    Should Be Equal    ${product_price_PLP}  ${product_price_cart}
    [Teardown]    Clean cart

