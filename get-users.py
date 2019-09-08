#!/usr/bin/env python

import os
from requests_oauthlib import OAuth1Session
import oauthlib

client_key = os.environ['INDIGITOUS_CLIENT_KEY']
client_secret = os.environ['INDIGITOUS_CLIENT_SECRET']

request_token_url = "https://indigitous.org/oauth1/request"

oauth = OAuth1Session(client_key, client_secret=client_secret)
fetch_response = oauth.fetch_request_token(request_token_url)

resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

base_authorization_url = "https://indigitous.org/oauth1/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
input("Please go here: {}, authorize, then export it as environment variable INDIGITOUS_VERIFIER and press enter".format(authorization_url))

verifier = os.environ['INDIGITOUS_VERIFIER']

access_token_url = "https://indigitous.org/oauth1/access"

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret,
                          verifier=verifier)
oauth_tokens = oauth.fetch_access_token(access_token_url)
resource_owner_key = oauth_tokens.get('oauth_token')
resource_owner_secret = oauth_tokens.get('oauth_token_secret')
resource_owner_key, resource_owner_secret

protected_url = "https://indigitous.org/wp-json/wp/v2/users/"

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret,
                          signature_type=oauthlib.oauth1.SIGNATURE_TYPE_QUERY)
r = oauth.get(protected_url)
print(json.dumps(r.json(), indent=2))
