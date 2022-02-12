def heads(ApiKey: str) -> dict:
    return dict(
    {
        "Authorization": f"Bearer {ApiKey}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
        "Content-Type":"application/json",
        "Accept": "*/*",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "DNT": "1"
    }),dict(
    {
    "Authorization": f"Bearer {ApiKey}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
    "Content-Type":"multipart/form-data",
    "Accept": "*/*",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "DNT": "1"
    })
    
    
