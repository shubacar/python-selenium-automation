# Created by Shuba at 7/23/2022
Feature:  Amazon cart verification

  Scenario: User verifies cart is empty
   Given User opens the logged out Amazon page
   When User clicks on the cart icon
    Then Verifies that the cart is empty

