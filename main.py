from concurrent.futures import ThreadPoolExecutor
from requests           import Session
from time               import time


from lib.constants import *
from lib.theme     import Colors

class CMSDetect(Session):
    """Module can be used for anything."""
    def __init__(self: object, domain: str = 'http://google.com') -> None:
        super().__init__() 
    
        self._domain: str  = domain
        
        self.results: list = []
        self.headers: dict = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        
    #############################################################
    """Property methods."""
    @property
    def domain(self: object) -> str:
        return self._domain
    
    @domain.setter
    def domain(self: object, domain: str) -> None:
        if not isinstance(domain, str):
            raise TypeError

        self._domain: str = self.check_url(domain)
        
    #############################################################
    """Static methods."""
        
    @staticmethod
    def check_url(domain: str) -> str:
        """
        Detects if a URL is passed and only selects the domain.
        
            Returns: The domain
        """
        # Look for http(s)://www. and http(s)://
        for prefix in HTTP_PREFIXS:
            for extra_prefix in ('//','://www'):
                if (swap := f'{prefix}{extra_prefix}') in domain:
                    domain: str = domain.partition(swap)[2]
                    

                
        if '/' in domain:
            domain: str = domain.partition('/')[0]
            
        return domain
        
        
    @staticmethod
    def detect(resp: str) -> str:
        """
        Detect the CMS with specific strings
        
            Returns: CMS name
        """
        for category in DETECTION:
            if [string for string in DETECTION[category] if string in resp]:
                return category
    #############################################################
    """Main methods."""
        
    def send_request(self, url: str) -> None: 
        """
        Send request to the URL and grab the content
        
            Returns: None
        
        """
        try:
            cms: str = self.detect(self.get(
                url     = url,
                timeout = 5
            ).text)
            
            if cms and not cms in self.results:
                self.results.append(cms)
        except:
            return
                       
                
    def get_results(self: object) -> None:
        """
        Execute the module:
        
            Returns: None
        """
        self.results.clear()
        
        with ThreadPoolExecutor(max_workers=800) as executor:
            for endpoint in ENDPOINTS:
                 for prefix in HTTP_PREFIXS:
                     executor.submit(
                          self.send_request,
                          f"{prefix}://{self.domain}{endpoint}",
                     )
                
                
session: object = CMSDetect()  
print(f'\x1bc{Colors.BANNER}')       
if __name__ == '__main__':  
    while 1:
        session.domain: str = input(f'{Colors.WHITE}URL:{Colors.ORANGE} ')
        print(f'{Colors.WHITE}Finding CMS...')
        
        # Check how long it takes.
        start: int = time()
        session.get_results()
        
        if not session.results:
            print(f'{Colors.RED}• {Colors.WHITE}Failed to find CMS.\n')
            continue
            
        print(f' {Colors.LIME}• {Colors.LIGHTPINK}{f", ".join(session.results)}{Colors.WHITE}')
            
        print(f'\n{Colors.WHITE}Execution speed: {Colors.PINK}{time() - start} {Colors.WHITE}seconds.\n') 
                
    
