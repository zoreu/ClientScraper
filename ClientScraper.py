import requests
import logging

# Configurando o logger
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)
logger = logging.getLogger(__name__)

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
PROXY = 'https://webproxy.liyao.blog/'

class cfscraper:
    session = requests.Session()
    
    @classmethod
    def get(cls, url, headers={}, timeout=None, allow_redirects=True, cookies={}):
        sess = cls.session
        if not headers:
            headers = {'User-Agent': USER_AGENT}
        try:
            res = sess.get(url, headers=headers, cookies=cookies, allow_redirects=allow_redirects, timeout=timeout)
            res.raise_for_status()            
            return res
        except requests.exceptions.HTTPError as err:
            if err.response.status_code in [403, 503]:
                proxy_url = PROXY + url
                try:
                    res = sess.get(proxy_url, headers=headers, cookies=cookies, allow_redirects=allow_redirects, timeout=timeout)
                    res.raise_for_status()            
                    return res
                except requests.exceptions.HTTPError as err:
                    if err.response.status_code == 403:
                        logger.error("Erro 403: Access denied")
                    elif err.response.status_code == 503:
                        logger.error("Erro 503: Service unavailable.")
                    else:
                        logger.error(f"HTTP error occurred: {err}")
            else:
                logger.error(f"HTTP error occurred: {err}")
        except Exception as e:
            proxy_url = PROXY + url
            try:
                res = sess.get(proxy_url, headers=headers, cookies=cookies, allow_redirects=allow_redirects, timeout=timeout)
                res.raise_for_status()            
                return res  # Retorna a resposta aqui também
            except requests.exceptions.HTTPError as err:
                if err.response.status_code == 403:
                    logger.error("Erro 403: Access denied")
                elif err.response.status_code == 503:
                    logger.error("Erro 503: Service unavailable.")
                else:
                    logger.error(f"HTTP error occurred: {err}")
            except Exception as e:
                logger.error(f"HTTP error occurred: {e}")        
        return None  # Retorna None em caso de erro

    @classmethod
    def post(cls, url, headers={}, timeout=None, data=None, json=None, allow_redirects=True):
        sess = cls.session
        if not headers:
            headers = {'User-Agent': USER_AGENT}
        try:
            if data:
                res = sess.post(url,headers=headers, data=data, allow_redirects=allow_redirects, timeout=timeout)
            else:
                res = sess.post(url,headers=headers, json=json, allow_redirects=allow_redirects, timeout=timeout)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as err:
            if err.response.status_code in [403, 503]:
                proxy_url = PROXY + url
                try:
                    if data:
                        res = sess.post(proxy_url, headers=headers, data=data, allow_redirects=allow_redirects, timeout=timeout)
                    else:
                        res = sess.post(proxy_url, headers=headers, json=json, allow_redirects=allow_redirects, timeout=timeout)
                    res.raise_for_status()            
                    return res
                except requests.exceptions.HTTPError as err:
                    if err.response.status_code == 403:
                        logger.error("Erro 403: Access denied")
                    elif err.response.status_code == 503:
                        logger.error("Erro 503: Service unavailable.")
                    else:
                        logger.error(f"HTTP error occurred: {err}")
            else:
                logger.error(f"HTTP error occurred: {err}")
        except Exception as e:
            try:
                if data:
                    res = sess.post(proxy_url, headers=headers, data=data, allow_redirects=allow_redirects, timeout=timeout)
                else:
                    res = sess.post(proxy_url, headers=headers, json=json, allow_redirects=allow_redirects, timeout=timeout)
                res.raise_for_status()            
                return res
            except requests.exceptions.HTTPError as err:
                if err.response.status_code == 403:
                    logger.error("Erro 403: Access denied")
                elif err.response.status_code == 503:
                    logger.error("Erro 503: Service unavailable.")
                else:
                    logger.error(f"HTTP error occurred: {err}")
            except Exception as e:
                logger.error(f"HTTP error occurred: {e}") 
                                

