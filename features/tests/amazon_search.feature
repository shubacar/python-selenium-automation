# Created by Shwetha at 7/15/2022
Feature: Amazon product search tests
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for Mugs
    Then Verify "Mugs" are shown


  Scenario: User can search for a product and add it
    Given Open Amazon page
    When Search for Contigo water bottles 24oz
    And Click on the first product
    And Click on the cart button
    And User clicks on the cart icon
    Then Verify the cart has 1 item
            |
Scenario: Verify whether footer links are present
  Given Open Amazon page
  Then Whether 38 footer links are shown

  Scenario: Verify bestseller links are present
    Given Open Amazon page
    When Click on bestsellers
    Then Verify 5 bestsellers are shown
