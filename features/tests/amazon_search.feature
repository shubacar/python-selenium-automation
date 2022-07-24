# Created by Shwetha at 7/15/2022
Feature: Amazon product search tests
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for Mugs
    Then Verify mugs are shown