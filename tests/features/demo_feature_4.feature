Feature: Demo Feature 4

    # Scenario: Test a rest api GET /store_inventory
    #     When test GET get_store_inventory api
    #     Then the response code is equal to 200

    Scenario: Test a rest api GET /store/order/{orderID}
        When test GET get_store_order api
        Then the response code is equal to 200
