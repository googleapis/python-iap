# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from collections import OrderedDict
import functools
import re
from typing import Dict, Mapping, Optional, Sequence, Tuple, Type, Union

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore
import pkg_resources

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore

from google.cloud.iap_v1.services.identity_aware_proxy_admin_service import pagers
from google.cloud.iap_v1.types import service

from .client import IdentityAwareProxyAdminServiceClient
from .transports.base import (
    DEFAULT_CLIENT_INFO,
    IdentityAwareProxyAdminServiceTransport,
)
from .transports.grpc_asyncio import IdentityAwareProxyAdminServiceGrpcAsyncIOTransport


class IdentityAwareProxyAdminServiceAsyncClient:
    """APIs for Identity-Aware Proxy Admin configurations."""

    _client: IdentityAwareProxyAdminServiceClient

    DEFAULT_ENDPOINT = IdentityAwareProxyAdminServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = IdentityAwareProxyAdminServiceClient.DEFAULT_MTLS_ENDPOINT

    tunnel_dest_group_path = staticmethod(
        IdentityAwareProxyAdminServiceClient.tunnel_dest_group_path
    )
    parse_tunnel_dest_group_path = staticmethod(
        IdentityAwareProxyAdminServiceClient.parse_tunnel_dest_group_path
    )
    tunnel_location_path = staticmethod(
        IdentityAwareProxyAdminServiceClient.tunnel_location_path
    )
    parse_tunnel_location_path = staticmethod(
        IdentityAwareProxyAdminServiceClient.parse_tunnel_location_path
    )
    common_billing_account_path = staticmethod(
        IdentityAwareProxyAdminServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        IdentityAwareProxyAdminServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        IdentityAwareProxyAdminServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        IdentityAwareProxyAdminServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        IdentityAwareProxyAdminServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        IdentityAwareProxyAdminServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        IdentityAwareProxyAdminServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        IdentityAwareProxyAdminServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        IdentityAwareProxyAdminServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        IdentityAwareProxyAdminServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            IdentityAwareProxyAdminServiceAsyncClient: The constructed client.
        """
        return IdentityAwareProxyAdminServiceClient.from_service_account_info.__func__(IdentityAwareProxyAdminServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            IdentityAwareProxyAdminServiceAsyncClient: The constructed client.
        """
        return IdentityAwareProxyAdminServiceClient.from_service_account_file.__func__(IdentityAwareProxyAdminServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return IdentityAwareProxyAdminServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> IdentityAwareProxyAdminServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            IdentityAwareProxyAdminServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(IdentityAwareProxyAdminServiceClient).get_transport_class,
        type(IdentityAwareProxyAdminServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, IdentityAwareProxyAdminServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the identity aware proxy admin service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.IdentityAwareProxyAdminServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = IdentityAwareProxyAdminServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def set_iam_policy(
        self,
        request: Union[iam_policy_pb2.SetIamPolicyRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policy_pb2.Policy:
        r"""Sets the access control policy for an Identity-Aware Proxy
        protected resource. Replaces any existing policy. More
        information about managing access via IAP can be found at:
        https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api

        .. code-block:: python

            from google.cloud import iap_v1
            from google.iam.v1 import iam_policy_pb2  # type: ignore

            async def sample_set_iam_policy():
                # Create a client
                client = iap_v1.IdentityAwareProxyAdminServiceAsyncClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.SetIamPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = await client.set_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]):
                The request object. Request message for `SetIamPolicy`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.iam.v1.policy_pb2.Policy:
                An Identity and Access Management (IAM) policy, which specifies access
                   controls for Google Cloud resources.

                   A Policy is a collection of bindings. A binding binds
                   one or more members, or principals, to a single role.
                   Principals can be user accounts, service accounts,
                   Google groups, and domains (such as G Suite). A role
                   is a named list of permissions; each role can be an
                   IAM predefined role or a user-created custom role.

                   For some types of Google Cloud resources, a binding
                   can also specify a condition, which is a logical
                   expression that allows access to a resource only if
                   the expression evaluates to true. A condition can add
                   constraints based on attributes of the request, the
                   resource, or both. To learn which resources support
                   conditions in their IAM policies, see the [IAM
                   documentation](\ https://cloud.google.com/iam/help/conditions/resource-policies).

                   **JSON example:**

                      {
                         "bindings": [
                            {
                               "role":
                               "roles/resourcemanager.organizationAdmin",
                               "members": [ "user:mike@example.com",
                               "group:admins@example.com",
                               "domain:google.com",
                               "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                               ]

                            }, { "role":
                            "roles/resourcemanager.organizationViewer",
                            "members": [ "user:eve@example.com" ],
                            "condition": { "title": "expirable access",
                            "description": "Does not grant access after
                            Sep 2020", "expression": "request.time <
                            timestamp('2020-10-01T00:00:00.000Z')", } }

                         ], "etag": "BwWWja0YfJA=", "version": 3

                      }

                   **YAML example:**

                      bindings: - members: - user:\ mike@example.com -
                      group:\ admins@example.com - domain:google.com -
                      serviceAccount:\ my-project-id@appspot.gserviceaccount.com
                      role: roles/resourcemanager.organizationAdmin -
                      members: - user:\ eve@example.com role:
                      roles/resourcemanager.organizationViewer
                      condition: title: expirable access description:
                      Does not grant access after Sep 2020 expression:
                      request.time <
                      timestamp('2020-10-01T00:00:00.000Z') etag:
                      BwWWja0YfJA= version: 3

                   For a description of IAM and its features, see the
                   [IAM
                   documentation](\ https://cloud.google.com/iam/docs/).

        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.SetIamPolicyRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_iam_policy,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_iam_policy(
        self,
        request: Union[iam_policy_pb2.GetIamPolicyRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policy_pb2.Policy:
        r"""Gets the access control policy for an Identity-Aware Proxy
        protected resource. More information about managing access via
        IAP can be found at:
        https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api

        .. code-block:: python

            from google.cloud import iap_v1
            from google.iam.v1 import iam_policy_pb2  # type: ignore

            async def sample_get_iam_policy():
                # Create a client
                client = iap_v1.IdentityAwareProxyAdminServiceAsyncClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.GetIamPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = await client.get_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]):
                The request object. Request message for `GetIamPolicy`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.iam.v1.policy_pb2.Policy:
                An Identity and Access Management (IAM) policy, which specifies access
                   controls for Google Cloud resources.

                   A Policy is a collection of bindings. A binding binds
                   one or more members, or principals, to a single role.
                   Principals can be user accounts, service accounts,
                   Google groups, and domains (such as G Suite). A role
                   is a named list of permissions; each role can be an
                   IAM predefined role or a user-created custom role.

                   For some types of Google Cloud resources, a binding
                   can also specify a condition, which is a logical
                   expression that allows access to a resource only if
                   the expression evaluates to true. A condition can add
                   constraints based on attributes of the request, the
                   resource, or both. To learn which resources support
                   conditions in their IAM policies, see the [IAM
                   documentation](\ https://cloud.google.com/iam/help/conditions/resource-policies).

                   **JSON example:**

                      {
                         "bindings": [
                            {
                               "role":
                               "roles/resourcemanager.organizationAdmin",
                               "members": [ "user:mike@example.com",
                               "group:admins@example.com",
                               "domain:google.com",
                               "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                               ]

                            }, { "role":
                            "roles/resourcemanager.organizationViewer",
                            "members": [ "user:eve@example.com" ],
                            "condition": { "title": "expirable access",
                            "description": "Does not grant access after
                            Sep 2020", "expression": "request.time <
                            timestamp('2020-10-01T00:00:00.000Z')", } }

                         ], "etag": "BwWWja0YfJA=", "version": 3

                      }

                   **YAML example:**

                      bindings: - members: - user:\ mike@example.com -
                      group:\ admins@example.com - domain:google.com -
                      serviceAccount:\ my-project-id@appspot.gserviceaccount.com
                      role: roles/resourcemanager.organizationAdmin -
                      members: - user:\ eve@example.com role:
                      roles/resourcemanager.organizationViewer
                      condition: title: expirable access description:
                      Does not grant access after Sep 2020 expression:
                      request.time <
                      timestamp('2020-10-01T00:00:00.000Z') etag:
                      BwWWja0YfJA= version: 3

                   For a description of IAM and its features, see the
                   [IAM
                   documentation](\ https://cloud.google.com/iam/docs/).

        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.GetIamPolicyRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_iam_policy,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def test_iam_permissions(
        self,
        request: Union[iam_policy_pb2.TestIamPermissionsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        r"""Returns permissions that a caller has on the Identity-Aware
        Proxy protected resource. More information about managing access
        via IAP can be found at:
        https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api

        .. code-block:: python

            from google.cloud import iap_v1
            from google.iam.v1 import iam_policy_pb2  # type: ignore

            async def sample_test_iam_permissions():
                # Create a client
                client = iap_v1.IdentityAwareProxyAdminServiceAsyncClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.TestIamPermissionsRequest(
                    resource="resource_value",
                    permissions=['permissions_value_1', 'permissions_value_2'],
                )

                # Make the request
                response = await client.test_iam_permissions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]):
                The request object. Request message for
                `TestIamPermissions` method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse:
                Response message for TestIamPermissions method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.TestIamPermissionsRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.test_iam_permissions,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_iap_settings(
        self,
        request: Union[service.GetIapSettingsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.IapSettings:
        r"""Gets the IAP settings on a particular IAP protected
        resource.

        .. code-block:: python

            from google.cloud import iap_v1

            async def sample_get_iap_settings():
                # Create a client
                client = iap_v1.IdentityAwareProxyAdminServiceAsyncClient()

                # Initialize request argument(s)
                request = iap_v1.GetIapSettingsRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_iap_settings(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.iap_v1.types.GetIapSettingsRequest, dict]):
                The request object. The request sent to GetIapSettings.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iap_v1.types.IapSettings:
                The IAP configurable settings.
        """
        # Create or coerce a protobuf request object.
        request = service.GetIapSettingsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_iap_settings,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_iap_settings(
        self,
        request: Union[service.UpdateIapSettingsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.IapSettings:
        r"""Updates the IAP settings on a particular IAP protected resource.
        It replaces all fields unless the ``update_mask`` is set.

        .. code-block:: python

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

        Args:
            request (Union[google.cloud.iap_v1.types.UpdateIapSettingsRequest, dict]):
                The request object. The request sent to
                UpdateIapSettings.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iap_v1.types.IapSettings:
                The IAP configurable settings.
        """
        # Create or coerce a protobuf request object.
        request = service.UpdateIapSettingsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_iap_settings,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("iap_settings.name", request.iap_settings.name),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_tunnel_dest_groups(
        self,
        request: Union[service.ListTunnelDestGroupsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListTunnelDestGroupsAsyncPager:
        r"""Lists the existing TunnelDestGroups. To group across all
        locations, use a ``-`` as the location ID. For example:
        ``/v1/projects/123/iap_tunnel/locations/-/destGroups``

        .. code-block:: python

            from google.cloud import iap_v1

            async def sample_list_tunnel_dest_groups():
                # Create a client
                client = iap_v1.IdentityAwareProxyAdminServiceAsyncClient()

                # Initialize request argument(s)
                request = iap_v1.ListTunnelDestGroupsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_tunnel_dest_groups(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.iap_v1.types.ListTunnelDestGroupsRequest, dict]):
                The request object. The request to ListTunnelDestGroups.
            parent (:class:`str`):
                Required. Google Cloud Project ID and location. In the
                following format:
                ``projects/{project_number/id}/iap_tunnel/locations/{location}``.
                A ``-`` can be used for the location to group across all
                locations.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iap_v1.services.identity_aware_proxy_admin_service.pagers.ListTunnelDestGroupsAsyncPager:
                The response from
                ListTunnelDestGroups.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.ListTunnelDestGroupsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_tunnel_dest_groups,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListTunnelDestGroupsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_tunnel_dest_group(
        self,
        request: Union[service.CreateTunnelDestGroupRequest, dict] = None,
        *,
        parent: str = None,
        tunnel_dest_group: service.TunnelDestGroup = None,
        tunnel_dest_group_id: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.TunnelDestGroup:
        r"""Creates a new TunnelDestGroup.

        .. code-block:: python

            from google.cloud import iap_v1

            async def sample_create_tunnel_dest_group():
                # Create a client
                client = iap_v1.IdentityAwareProxyAdminServiceAsyncClient()

                # Initialize request argument(s)
                tunnel_dest_group = iap_v1.TunnelDestGroup()
                tunnel_dest_group.name = "name_value"

                request = iap_v1.CreateTunnelDestGroupRequest(
                    parent="parent_value",
                    tunnel_dest_group=tunnel_dest_group,
                    tunnel_dest_group_id="tunnel_dest_group_id_value",
                )

                # Make the request
                response = await client.create_tunnel_dest_group(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.iap_v1.types.CreateTunnelDestGroupRequest, dict]):
                The request object. The request to
                CreateTunnelDestGroup.
            parent (:class:`str`):
                Required. Google Cloud Project ID and location. In the
                following format:
                ``projects/{project_number/id}/iap_tunnel/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tunnel_dest_group (:class:`google.cloud.iap_v1.types.TunnelDestGroup`):
                Required. The TunnelDestGroup to
                create.

                This corresponds to the ``tunnel_dest_group`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tunnel_dest_group_id (:class:`str`):
                Required. The ID to use for the TunnelDestGroup, which
                becomes the final component of the resource name.

                This value must be 4-63 characters, and valid characters
                are ``[a-z][0-9]-``.

                This corresponds to the ``tunnel_dest_group_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iap_v1.types.TunnelDestGroup:
                A TunnelDestGroup.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, tunnel_dest_group, tunnel_dest_group_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.CreateTunnelDestGroupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if tunnel_dest_group is not None:
            request.tunnel_dest_group = tunnel_dest_group
        if tunnel_dest_group_id is not None:
            request.tunnel_dest_group_id = tunnel_dest_group_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_tunnel_dest_group,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_tunnel_dest_group(
        self,
        request: Union[service.GetTunnelDestGroupRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.TunnelDestGroup:
        r"""Retrieves an existing TunnelDestGroup.

        .. code-block:: python

            from google.cloud import iap_v1

            async def sample_get_tunnel_dest_group():
                # Create a client
                client = iap_v1.IdentityAwareProxyAdminServiceAsyncClient()

                # Initialize request argument(s)
                request = iap_v1.GetTunnelDestGroupRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_tunnel_dest_group(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.iap_v1.types.GetTunnelDestGroupRequest, dict]):
                The request object. The request to GetTunnelDestGroup.
            name (:class:`str`):
                Required. Name of the TunnelDestGroup to be fetched. In
                the following format:
                ``projects/{project_number/id}/iap_tunnel/locations/{location}/destGroups/{dest_group}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iap_v1.types.TunnelDestGroup:
                A TunnelDestGroup.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetTunnelDestGroupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_tunnel_dest_group,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_tunnel_dest_group(
        self,
        request: Union[service.DeleteTunnelDestGroupRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a TunnelDestGroup.

        .. code-block:: python

            from google.cloud import iap_v1

            async def sample_delete_tunnel_dest_group():
                # Create a client
                client = iap_v1.IdentityAwareProxyAdminServiceAsyncClient()

                # Initialize request argument(s)
                request = iap_v1.DeleteTunnelDestGroupRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_tunnel_dest_group(request=request)

        Args:
            request (Union[google.cloud.iap_v1.types.DeleteTunnelDestGroupRequest, dict]):
                The request object. The request to
                DeleteTunnelDestGroup.
            name (:class:`str`):
                Required. Name of the TunnelDestGroup to delete. In the
                following format:
                ``projects/{project_number/id}/iap_tunnel/locations/{location}/destGroups/{dest_group}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.DeleteTunnelDestGroupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_tunnel_dest_group,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def update_tunnel_dest_group(
        self,
        request: Union[service.UpdateTunnelDestGroupRequest, dict] = None,
        *,
        tunnel_dest_group: service.TunnelDestGroup = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.TunnelDestGroup:
        r"""Updates a TunnelDestGroup.

        .. code-block:: python

            from google.cloud import iap_v1

            async def sample_update_tunnel_dest_group():
                # Create a client
                client = iap_v1.IdentityAwareProxyAdminServiceAsyncClient()

                # Initialize request argument(s)
                tunnel_dest_group = iap_v1.TunnelDestGroup()
                tunnel_dest_group.name = "name_value"

                request = iap_v1.UpdateTunnelDestGroupRequest(
                    tunnel_dest_group=tunnel_dest_group,
                )

                # Make the request
                response = await client.update_tunnel_dest_group(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.iap_v1.types.UpdateTunnelDestGroupRequest, dict]):
                The request object. The request to
                UpdateTunnelDestGroup.
            tunnel_dest_group (:class:`google.cloud.iap_v1.types.TunnelDestGroup`):
                Required. The new values for the
                TunnelDestGroup.

                This corresponds to the ``tunnel_dest_group`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                A field mask that specifies which IAP
                settings to update. If omitted, then all
                of the settings are updated. See
                https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iap_v1.types.TunnelDestGroup:
                A TunnelDestGroup.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([tunnel_dest_group, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.UpdateTunnelDestGroupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if tunnel_dest_group is not None:
            request.tunnel_dest_group = tunnel_dest_group
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_tunnel_dest_group,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("tunnel_dest_group.name", request.tunnel_dest_group.name),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-iap",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("IdentityAwareProxyAdminServiceAsyncClient",)
