Feature: Sign in
    In order to maintain a personal identity
    I want to sign in

Scenario: User signs in successfully
    Given a user exists with username: "joeb", password: "secret007"
    And I go to the "/login/" URL
    When I fill in "username" with "joeb"
    And I fill in "password" with "secret007"
    And I press "Sign In"
    Then the page title should be "Mozilla Drumbeat | Your Dashboard"

Scenario: User attempts to sign in with invalid details
    Given I go to the "/login/" URL
    When I fill in "username" with ""
    And I fill in "password" with ""
    And I press "Sign In"
    And I should see "Incorrect email or password."
