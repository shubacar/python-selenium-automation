# Created by Shuba at 8/7/2022
Feature: Verify Amazon terms and conditions are displayed


  Scenario: User can open and close Amazon Privacy Notice
  Given User open Amazon T&C page
  When Store original windows
  And Click on Amazon Privacy Notice link
  And Switch to the newly opened window
  Then Verify Amazon Privacy Notice page is opened
  And User can close new window and switch back to original
