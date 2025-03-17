from urllib.parse import urlparse
import tldextract

list_of_domains_to_remove = set(
    [
        "youtube.com",
        "twitter.com",
        "instagram.com",
        "tiktok.com",
        "facebook.com",
        "linkedin.com",
        "pinterest.com",
        "reddit.com",
        "tumblr.com",
        "flickr.com",
        "vimeo.com",
        "wikipedia.org",
        "wikileaks.org",
    ]
)


def has_path(url):
    """
    Check if the URL has a path component.
    NOTE: only works for URLs; does not work for domain names

    Returns:
        bool: True if URL has a non-empty path, False otherwise
    """
    parsed_url = urlparse(url)
    path = parsed_url.path.replace("/", "")
    return path != ""


def extract_suffix(url):
    """
    Extract the top-level domain suffix from the URL.

    Returns:
        str: The top-level domain suffix (e.g. 'com', 'org', 'co.uk')
    """
    extracted = tldextract.extract(url)
    suffix = extracted.suffix
    return suffix


def extract_domain(url):
    """
    Extract the domain from the URL.

    Returns:
        str: The domain (e.g. 'example.com')
    """
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    return domain
