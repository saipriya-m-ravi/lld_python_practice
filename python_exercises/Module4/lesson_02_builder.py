"""
Lesson 4.2 - Builder

Step 1: Fill in the remaining setter methods and build().
Step 2: Construct a request using ONLY the fluent chain -- no positional
        HttpRequest(...) call anywhere in your __main__ code.
Step 3: Prove build()'s validation works -- call .build() on a builder
        that never had set_url() called, and confirm it raises cleanly.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class HttpRequest:
    method: str
    url: str
    headers: dict
    query_params: dict
    body: dict | None
    timeout: float


class HttpRequestBuilder:
    def __init__(self):
        self._method = "GET"
        self._url = None          # required -- must be set before build()
        self._headers = {}
        self._query_params = {}
        self._body = None
        self._timeout = 30.0

    def set_url(self, url: str) -> "HttpRequestBuilder":
        self._url = url
        return self

    # TODO: set_method(self, method: str) -> "HttpRequestBuilder"
    #   set self._method, return self
    def set_method(self, method: str) -> "HttpRequestBuilder":
        self._method = method
        return self

    # TODO: add_header(self, key: str, value: str) -> "HttpRequestBuilder"
    #   self._headers[key] = value, return self
    def add_header(self, key: str, value: str) -> "HttpRequestBuilder":
        self._headers[key] = value
        return self

    # TODO: add_query_param(self, key: str, value: str) -> "HttpRequestBuilder"
    #   self._query_params[key] = value, return self
    def add_query_param(self, key: str, value: str) -> "HttpRequestBuilder":
        self._query_params[key] = value
        return self    

    # TODO: set_body(self, body: dict) -> "HttpRequestBuilder"
    #   set self._body, return self
    def set_body(self, body: dict) -> "HttpRequestBuilder":
        self._body = body
        return self
    
    # TODO: set_timeout(self, seconds: float) -> "HttpRequestBuilder"
    #   set self._timeout, return self
    def set_timeout(self, seconds: float) -> "HttpRequestBuilder":
        self._timeout = seconds
        return self
    
    # TODO: build(self) -> HttpRequest
    #   if self._url is None: raise ValueError("url is required")
    #   otherwise construct and return an HttpRequest from all the
    #   builder's current _fields
    def build(self) -> "HttpRequest":
        if self._url is None:
            raise ValueError("url is required")
        
        return HttpRequest(
            self._method,
            self._url,
            self._headers,
            self._query_params,
            self._body,
            self._timeout
        )


if __name__ == "__main__":
    request = (
        HttpRequestBuilder()
        .set_url("https://api.example.com/books")
        .set_method("POST")
        .add_header("content-Type", "application/json")
        .add_query_param("limit", "10")
        .set_body({"title": "Dune"})
        .build()
    )
    print(request)
    # TODO: build a full request via chaining:
    #   HttpRequestBuilder().set_url(...).set_method("POST")
    #       .add_header("Content-Type", "application/json")
    #       .add_query_param("limit", "10")
    #       .set_body({"title": "Dune"})
    #       .build()
    #   print the resulting HttpRequest
    try:
        request = (
            HttpRequestBuilder()
            .set_method("POST")
            .add_header("content-Type", "application/json")
            .add_query_param("limit", "10")
            .set_body({"title": "Dune"})
            .build()
        )
    except ValueError as e:
        print(e)
    # TODO: try HttpRequestBuilder().build() (no url set) in a
    #   try/except -- confirm ValueError is raised, print the message
