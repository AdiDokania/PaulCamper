Feature: Test PaulCamper Application
    Scenario: Verify Search Filters
      Given We Launch the Browser
      Then We verify Page Title
      When We select Body Style as Camper Bus
      And Price Between Euro 25-150
