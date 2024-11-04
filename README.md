You have 3 options:
- https://spaceconverter.blogspot.com (may not work)
- [spaceconverter.html](https://raw.githubusercontent.com/mortyobnoxious/TWspaceDynamic/main/spaceconverter.html) (download and open with a browser)
- [TWspaceDynamic.py](https://raw.githubusercontent.com/mortyobnoxious/TWspaceDynamic/main/TWspaceDynamic.py) (requires Python)

# TWspaceDynamic
#### Twitter Space Dynamic URL to Playlist URL

This converts `dynamic_playlist` URL to "`playlist url`" so that you can listen Twitter Space even if it's not recorded.

1. Paste dynamic_playlist [^1] URL as in below:

`https://prod-fastly-eu-central-1.video.pscp.tv/Transcoding/v1/hls/*****/non_transcode/eu-central-1/periscope-replay-direct-prod-eu-central-1-public/audio-space/dynamic_playlist.m3u8?type=live`

2. Get playable [^2] playlist url as in below:

`https://prod-fastly-eu-central-1.video.pscp.tv/Transcoding/v1/hls/*****/non_transcode/eu-central-1/periscope-replay-direct-prod-eu-central-1-public/audio-space/playlist_*****.m3u8?type=replay`

[^1]: You have to get this URL while Twitter Space is live. You can use IDM or some browser extension like [The Stream Detector](https://addons.mozilla.org/en-US/firefox/addon/hls-stream-detector/) that catches media. Or you can use [getSpaceData.py](https://raw.githubusercontent.com/mortyobnoxious/TWspaceDynamic/main/getSpaceData.py) file.
[^2]: You can paste this url to media players like VLC, MPV and listen or you can dowload it with a download manager.

# getSpaceData
You can also get `dynamic_playlist` url for live spaces or `master url` for recorded spaces using python file below:
- [getSpaceData.py](https://raw.githubusercontent.com/mortyobnoxious/TWspaceDynamic/main/getSpaceData.py) (requires Python)

## Steps

### 1. Get `ct0` and `auth_token`
- Open Twitter in your browser.
- Open Developer Tools:
  - Windows: `F12` or `Ctrl + Shift + I`
  - Mac: `Cmd + Option + I`
- Go to the **Application** tab (or **Storage** tab) and navigate to **Cookies** for the Twitter domain.
- Locate cookies named `ct0` and `auth_token`. Copy their values.

### 2. Run the Code
- Once you’ve got `ct0`, `auth_token`, and `Space_URL`, run the script.
- When prompted, enter the values for `ct0`, `auth_token`, and the URL of the Twitter Space you want to access, like `https://twitter.com/i/spaces/XXXXXXXXX` or `https://x.com/i/spaces/XXXXXXXXX`.
- If everything's set correctly, it will give you a `dynamic_playlist` or `master url` for the audio stream of the specified Twitter Space.
