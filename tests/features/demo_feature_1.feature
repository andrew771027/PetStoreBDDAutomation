Feature: Demo Feature 1
    Demo the syntax of BDD

    Scenario: Use Given, When, Then sytax to compose a simple test case
        Given This is Given statement
        When This is When statement
        Then This is Then statement
    
    Scenario: Use general step sytax to compose a simple test case
        Given This is Given statement start from step
        When This is When statement start from step
        Then This is Then statement start from step
    
    Scenario: User parameter syntax to compose a simple test case
        Given Set Number to 1
        When Set Number to 2
        Then Set Number to 3

    Scenario: User context syntax to compose a simple test case
        Given Set a storage to context
        When Set Number to 1 and store to storage[number]
        When Get Number from storage[number]
    
    Scenario: User nested syntax to compose a simple test case
        Given This is the root statement


    

