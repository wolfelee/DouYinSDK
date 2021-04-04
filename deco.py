
import requests

def register(api):
    def fixer(func):
        def wrapper(self,*args,**kwargs):
            params = func(self,*args,**kwargs)
            if params is None:
                params = {}
            url = self.host + api
            params.update({
                'token':self.token
            })
            response = requests.get(url,params=params)
            return response.json()
        return wrapper
    return fixer