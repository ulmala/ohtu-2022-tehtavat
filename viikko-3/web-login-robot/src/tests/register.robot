*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page And Click Register Link

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallekalle
    Set Password  kalle123
    Set PasswordConfirmation  kalle123
    Register User
    Register Should Succeed


Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  asdasd123
    Set PasswordConfirmation  asdasd123
    Register User
    Register Should Fail With Message  Username must be at least 3 characters long


Register With Valid Username And Too Short Password
    Set Username  asdasdasd
    Set Password  1
    Set PasswordConfirmation  1
    Register User
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  asdasdasdasd
    Set Password  asd123456
    Set PasswordConfirmation  asd123457
    Register User
    Register Should Fail With Message  Password and password confirmation does not match

Login After Successful Registration
    Set Username  asdasd
    Set Password  asdpw123
    Set PasswordConfirmation  asdpw123
    Register User
    Register Should Succeed
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  asdasd
    Set Password  asdpw123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  a
    Set Password  1
    Set PasswordConfirmation  1
    Register User
    Click Link  Login
    Set Username  a
    Set Password  1
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Go To Home Page And Click Register Link
    Go To Home Page
    Click Link  Register new user

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PasswordConfirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register User
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}