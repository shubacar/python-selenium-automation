# Created by Shuba at 7/15/2022
Feature: Amazon product search tests
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for Mugs
    Then Verify "Mugs" are shown


  Scenario: User can add a product to cart
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

  Scenario: Verify user can see language options
    Given Open Amazon page
    When Hover over language options
    Then Spanish option is present

  Scenario: Verify user can select a department
    Given Open Amazon page
    When User selects department by alias appliances
    And Search for Refrigerator
    Then Verify appliances department is selected

  Scenario: Verify user can see new arrivals
    Given Open Amazon product page
    When Hover over new arrivals
    Then Boys option is present
