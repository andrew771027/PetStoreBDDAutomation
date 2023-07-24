Feature: The first feature

    @fixture.foo
    Scenario: The first scenario
        Given Hello World1
        When Hello1
    
    Scenario: The second scenario
        When Hello1
    
    Scenario: The third scenario
        Given test request
    
    Scenario: The fourth scenario
        Given Number is 1
        When show number from context

    Scenario: The fifth scsneario
        Given Number is 2
        When run nested step