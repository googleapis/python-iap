# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateIapSettings
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-iap


# [START iap_generated_iap_v1_IdentityAwareProxyAdminService_UpdateIapSettings_async]
from google.cloud import iap_v1


async def sample_update_iap_settings():
    # Create a client
    client = iap_v1.IdentityAwareProxyAdminServiceAsyncClient()

    # Initialize request argument(s)
    iap_settings = iap_v1.IapSettings()
    iap_settings.name = "name_value"

    request = iap_v1.UpdateIapSettingsRequest(
        iap_settings=iap_settings,
    )

    # Make the request
    response = await client.update_iap_settings(request=request)

    # Handle the response
    print(response)

# [END iap_generated_iap_v1_IdentityAwareProxyAdminService_UpdateIapSettings_async]
