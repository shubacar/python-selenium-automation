# Created by Shuba at 7/22/2022
Feature: Amazon sign in tests
  # Enter feature description here

  Scenario: Verify logged out users see sign in page
    Given User opens the logged out Amazon page
    When User clicks on the orders
    Then Sign in page opens

  Scenario: Verify the user can see sign in popup
   Given Open Amazon page
   When User clicks on the button on sign in popup
   Then Sign in page opens

  Scenario: User can see sign in button
   Given Open Amazon page
   Then Verify signin is clickable
   When Wait for 8 seconds
   Then Verify signin disappears