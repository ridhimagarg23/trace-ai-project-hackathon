"""URL checker"""

from urllib.parse import urlparse


class URLChecker:
    """
    Performs lightweight URL inspection.
    """

    # Well-known shortening services abused to disguise malicious links.
    SHORTENERS = {
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "goo.gl",
        "rb.gy",
        "ow.ly",
        "is.gd",
        "cutt.ly"
    }

    @classmethod
    def analyze(cls, url: str) -> dict:
        """
        Inspect one URL string.

        Parameters
        ----------
        url : str
            A URL or bare domain, e.g. ``"http://login.sbi-verify.co.in/x"``.

        Returns
        -------
        dict
            ``{"url", "domain", "https", "shortened", "subdomain_count"}``
            where ``subdomain_count`` counts labels left of the registrable
            domain (2 labels are assumed: ``name.tld``); for
            ``"login.sbi-verify.co.in"`` it returns 2.

        Example
        -------
        >>> URLChecker.analyze("http://bit.ly/abc")
        {'url': 'http://bit.ly/abc', 'domain': 'bit.ly', 'https': False, 'shortened': True, 'subdomain_count': 0}
        """

        parsed = urlparse(url)

        domain = parsed.netloc.lower()

        return {
            "url": url,
            "domain": domain,
            "https": parsed.scheme == "https",
            "shortened": domain in cls.SHORTENERS,
            "subdomain_count": max(len(domain.split(".")) - 2, 0),
        }
