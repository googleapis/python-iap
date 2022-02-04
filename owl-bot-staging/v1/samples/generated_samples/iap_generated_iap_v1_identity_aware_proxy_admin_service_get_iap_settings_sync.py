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
# Snippet for GetIapSettings
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-iap


# [START iap_generated_iap_v1_IdentityAwareProxyAdminService_GetIapSettings_sync]
from google.cloud import iap_v1


def sample_get_iap_settings():
    # Create a client
    client = iap_v1.IdentityAwareProxyAdminServiceClient()

    # Initialize request argument(s)
    request = iap_v1.GetIapSettingsRequest(
        name="name_value",
    )

    # Make the request
    response = client.get_iap_settings(request=request)

    # Handle response
    print(response)

# [END iap_generated_iap_v1_IdentityAwareProxyAdminService_GetIapSettings_sync]
