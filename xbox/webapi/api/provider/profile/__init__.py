"""
Profile

Get Userprofiles by XUID or Gamertag
"""
from typing import List

from xbox.webapi.api.provider.baseprovider import BaseProvider
from xbox.webapi.api.provider.profile.models import ProfileResponse, ProfileSettings


class ProfileProvider(BaseProvider):
    PROFILE_URL = "https://profile.xboxlive.com"
    HEADERS_PROFILE = {"x-xbl-contract-version": "2"}
    SEPARATOR = ","

    async def get_profiles(self, xuid_list: List) -> ProfileResponse:
        """
        Get profile info for list of xuids

        Args:
            xuid_list (list): List of xuids

        Returns:
            :class:`aiohttp.ClientResponse`: HTTP Response
        """
        post_data = {
            "settings": [
                ProfileSettings.GAME_DISPLAY_NAME,
                ProfileSettings.APP_DISPLAY_NAME,
                ProfileSettings.APP_DISPLAYPIC_RAW,
                ProfileSettings.GAMERSCORE,
                ProfileSettings.GAMERTAG,
                ProfileSettings.GAME_DISPLAYPIC_RAW,
                ProfileSettings.ACCOUNT_TIER,
                ProfileSettings.TENURE_LEVEL,
                ProfileSettings.XBOX_ONE_REP,
                ProfileSettings.PREFERRED_COLOR,
                ProfileSettings.LOCATION,
                ProfileSettings.BIOGRAPHY,
                ProfileSettings.WATERMARKS,
                ProfileSettings.REAL_NAME,
            ],
            "userIds": [int(xuid) for xuid in xuid_list],
        }
        url = self.PROFILE_URL + "/users/batch/profile/settings"
        return await self.client.session.post(
            url, json=post_data, headers=self.HEADERS_PROFILE
        )

    async def get_profile_by_xuid(self, target_xuid: int) -> ProfileResponse:
        """
        Get Userprofile by xuid

        Args:
            target_xuid: XUID to get profile for

        Returns:
            :class:`aiohttp.ClientResponse`: HTTP Response
        """
        url = self.PROFILE_URL + f"/users/xuid({target_xuid})/profile/settings"
        params = {
            "settings": self.SEPARATOR.join(
                [
                    ProfileSettings.APP_DISPLAY_NAME,
                    ProfileSettings.GAMERSCORE,
                    ProfileSettings.GAMERTAG,
                    ProfileSettings.PUBLIC_GAMERPIC,
                    ProfileSettings.XBOX_ONE_REP,
                ]
            )
        }
        return await self.client.session.get(
            url, params=params, headers=self.HEADERS_PROFILE
        )

    async def get_profile_by_gamertag(self, gamertag: str) -> ProfileResponse:
        """
        Get Userprofile by gamertag

        Args:
            gamertag: Gamertag to get profile for

        Returns:
            :class:`aiohttp.ClientResponse`: HTTP Response
        """
        url = self.PROFILE_URL + f"/users/gt({gamertag})/profile/settings"
        params = {
            "settings": self.SEPARATOR.join(
                [
                    ProfileSettings.APP_DISPLAY_NAME,
                    ProfileSettings.GAMERSCORE,
                    ProfileSettings.GAMERTAG,
                    ProfileSettings.PUBLIC_GAMERPIC,
                    ProfileSettings.XBOX_ONE_REP,
                ]
            )
        }
        return await self.client.session.get(
            url, params=params, headers=self.HEADERS_PROFILE
        )
