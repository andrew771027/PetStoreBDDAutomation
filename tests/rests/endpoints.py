class PetStoreEndpointMixin:
    def post_pet(self, payload):
        """
        Add a new pet to the store
        """
        return self.post(path="/pet", json=payload)

    def get_store_inventory(self):
        """
        Returns pet inventories by status
        """
        return self.get(path="/store/inventory")

    def get_store_order(self, uri_params: dict = None, params: dict = None):
        """
        Returns Find purchase order by ID
        """
        return self.get(
            path="/store/order/{orderId}", uri_params=uri_params, params=params
        )
