import requests

space_url = input("Enter the Twitter Space URL: ").strip()
ct0 = input("Enter your 'ct0' cookie value: ").strip()
auth_token = input("Enter your 'auth_token' cookie value: ").strip()

def get_guest():
    headers = {"authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"}
    return requests.post("https://api.x.com/1.1/guest/activate.json", headers=headers, timeout=30).json().get("guest_token")

def fetch_space_data(id, ct0, auth):
    params = {
        "variables": (
            "{"
            f'"id": "{id}",'
            '"isMetatagsQuery": true,'
            '"withSuperFollowsUserFields": true,'
            '"withDownvotePerspective": false,'
            '"withReactionsMetadata": false,'
            '"withReactionsPerspective": false,'
            '"withSuperFollowsTweetFields": true,'
            '"withReplays": true'
            "}"
        ),
        "features": (
            "{"
            '"spaces_2022_h2_clipping": true,'
            '"spaces_2022_h2_spaces_communities": true,'
            '"responsive_web_twitter_blue_verified_badge_is_enabled": true,'
            '"verified_phone_label_enabled": false,'
            '"view_counts_public_visibility_enabled": true,'
            '"longform_notetweets_consumption_enabled": false,'
            '"tweetypie_unmention_optimization_enabled": true,'
            '"responsive_web_uc_gql_enabled": true,'
            '"vibe_api_enabled": true,'
            '"responsive_web_edit_tweet_api_enabled": true,'
            '"graphql_is_translatable_rweb_tweet_is_translatable_enabled": true,'
            '"view_counts_everywhere_api_enabled": true,'
            '"standardized_nudges_misinfo": true,'
            '"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": false,'
            '"responsive_web_graphql_timeline_navigation_enabled": true,'
            '"interactive_text_enabled": true,'
            '"responsive_web_text_conversations_enabled": false,'
            '"responsive_web_enhance_cards_enabled": false'
            "}"
        ),
    }
    headers = {
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "x-csrf-token": ct0,
    }
    cookies = {'ct0': ct0, 'auth_token': auth}
    return requests.get("https://api.x.com/graphql/xjTKygiBMpX44KU8ywLohQ/AudioSpaceById", params=params, headers=headers, cookies=cookies).json()['data']['audioSpace']['metadata']

def get_stream_url(id, ct0, auth):
    space = fetch_space_data(id, ct0, auth)
    if space["state"] == "Ended" and not space["is_space_available_for_replay"]:
        raise Exception("[ERROR] Space ended, no replay.")

    headers = {"authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA", "cookie": f"auth_token={auth}"}
    media_key = space["media_key"]
    response = requests.get(f"https://x.com/i/api/1.1/live_video_stream/status/{media_key}", headers=headers, timeout=30)
    location = response.json()["source"]["location"]
    prefix = "Master URL: " if "type=replay" in location else "Dynamic URL: "
    return prefix + response.json()["source"]["location"]

if space_url.startswith(("https://x.com/i/spaces/", "https://twitter.com/i/spaces/")):
    space_id = space_url.rsplit('/', 1)[-1]
    try:
        print(get_stream_url(space_id, ct0, auth_token))
    except Exception as e:
        print(e)
else:
    print("[ERROR] Invalid URL")
