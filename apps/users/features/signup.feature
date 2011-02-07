Feature: Sign Up
    In order to get involved with Drumbeat
    I want to sign up

    Scenario: User registers
        When I go to the "/register/" URL
        And I fill in "display_name" with "Joe Bloggs"
        And I fill in "username" with "joeb"
        And I fill in "password" with "secret007"
        And I fill in "password_confirm" with "secret007"
        And I fill in "email" with "joeb@example.com"
        And I press "Create Account"
        Then I should see "Congratulations! Your user account was successfully created."
        And I should receive an email at "joeb@example.com" with the subject "Complete Registration"

    Scenario: User does not fill in sign up form correctly
        When I go to the "/register/" URL
        And I press "Create Account"
        Then I should see "There are errors in this form. Please correct them and resubmit."

    Scenario: User enters a username that has been taken
        Given a user exists with username "joeb"
        When I go to the "/register/" URL
        And I fill in "username" with "joeb"
        And I move focus away from the username field
        Then I should see "not available"
