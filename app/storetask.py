from lightparser import LightParser


class StoreTask:
    def similar(self, kwargs):
        apps = LightParser().extract(
            kwargs['similar_clp'], 'en_US', kwargs['country']
        )
        return apps
