# Created by Shuba at 7/22/2022
Feature: Amazon sign in tests
  # Enter feature description here

  Scenario: Verify logged out users see sign in page
    Given User opens the logged out Amazon page
    When User clicks on the cart
    Then Sign in page opens


