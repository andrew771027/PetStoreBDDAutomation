

class PetStoreEndpointMixin:

    def post_pet(self, payload):
        '''
        Add a new pet to the store
        '''
        return self.post(path='/v2/path', json=payload)

    def get_store_inventory(self):
        '''
        Returns pet inventories by status
        '''
        return self.get(path='/v2/store/inventory')
