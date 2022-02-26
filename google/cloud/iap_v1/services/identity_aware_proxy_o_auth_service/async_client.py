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
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.cloud.iap_v1.services.identity_aware_proxy_o_auth_service import pagers
from google.cloud.iap_v1.types import service
from .transports.base import (
    IdentityAwareProxyOAuthServiceTransport,
    DEFAULT_CLIENT_INFO,
)
from .transports.grpc_asyncio import IdentityAwareProxyOAuthServiceGrpcAsyncIOTransport
from .client import IdentityAwareProxyOAuthServiceClient


class IdentityAwareProxyOAuthServiceAsyncClient:
    """API to programmatically create, list and retrieve Identity
    Aware Proxy (IAP) OAuth brands; and create, retrieve, delete and
    reset-secret of IAP OAuth clients.
    """

    _client: IdentityAwareProxyOAuthServiceClient

    DEFAULT_ENDPOINT = IdentityAwareProxyOAuthServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = IdentityAwareProxyOAuthServiceClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        IdentityAwareProxyOAuthServiceClient.parse_common_location_path
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
            IdentityAwareProxyOAuthServiceAsyncClient: The constructed client.
        """
        return IdentityAwareProxyOAuthServiceClient.from_service_account_info.__func__(IdentityAwareProxyOAuthServiceAsyncClient, info, *args, **kwargs)  # type: ignore

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
            IdentityAwareProxyOAuthServiceAsyncClient: The constructed client.
        """
        return IdentityAwareProxyOAuthServiceClient.from_service_account_file.__func__(IdentityAwareProxyOAuthServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

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
        return IdentityAwareProxyOAuthServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> IdentityAwareProxyOAuthServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            IdentityAwareProxyOAuthServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(IdentityAwareProxyOAuthServiceClient).get_transport_class,
        type(IdentityAwareProxyOAuthServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, IdentityAwareProxyOAuthServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the identity aware proxy o auth service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.IdentityAwareProxyOAuthServiceTransport]): The
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
        self._client = IdentityAwareProxyOAuthServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_brands(
        self,
        request: Union[service.ListBrandsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.ListBrandsResponse:
        r"""Lists the existing brands for the project.

        .. code-block:: python

            from google.cloud import iap_v1

            def sample_list_brands():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceClient()

                # Initialize request argument(s)
                request = iap_v1.ListBrandsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.list_brands(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.iap_v1.types.ListBrandsRequest, dict]):
                The request object. The request sent to ListBrands.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iap_v1.types.ListBrandsResponse:
                Response message for ListBrands.
        """
        # Create or coerce a protobuf request object.
        request = service.ListBrandsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_brands,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def create_brand(
        self,
        request: Union[service.CreateBrandRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.Brand:
        r"""Constructs a new OAuth brand for the project if one
        does not exist. The created brand is "internal only",
        meaning that OAuth clients created under it only accept
        requests from users who belong to the same G Suite
        organization as the project. The brand is created in an
        un-reviewed status. NOTE: The "internal only" status can
        be manually changed in the Google Cloud console.
        Requires that a brand does not already exist for the
        project, and that the specified support email is owned
        by the caller.


        .. code-block:: python

            from google.cloud import iap_v1

            def sample_create_brand():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceClient()

                # Initialize request argument(s)
                request = iap_v1.CreateBrandRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_brand(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.iap_v1.types.CreateBrandRequest, dict]):
                The request object. The request sent to CreateBrand.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iap_v1.types.Brand:
                OAuth brand data.
                NOTE: Only contains a portion of the
                data that describes a brand.

        """
        # Create or coerce a protobuf request object.
        request = service.CreateBrandRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_brand,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_brand(
        self,
        request: Union[service.GetBrandRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.Brand:
        r"""Retrieves the OAuth brand of the project.

        .. code-block:: python

            from google.cloud import iap_v1

            def sample_get_brand():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceClient()

                # Initialize request argument(s)
                request = iap_v1.GetBrandRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_brand(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.iap_v1.types.GetBrandRequest, dict]):
                The request object. The request sent to GetBrand.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iap_v1.types.Brand:
                OAuth brand data.
                NOTE: Only contains a portion of the
                data that describes a brand.

        """
        # Create or coerce a protobuf request object.
        request = service.GetBrandRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_brand,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def create_identity_aware_proxy_client(
        self,
        request: Union[service.CreateIdentityAwareProxyClientRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.IdentityAwareProxyClient:
        r"""Creates an Identity Aware Proxy (IAP) OAuth client.
        The client is owned by IAP. Requires that the brand for
        the project exists and that it is set for internal-only
        use.


        .. code-block:: python

            from google.cloud import iap_v1

            def sample_create_identity_aware_proxy_client():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceClient()

                # Initialize request argument(s)
                request = iap_v1.CreateIdentityAwareProxyClientRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_identity_aware_proxy_client(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.iap_v1.types.CreateIdentityAwareProxyClientRequest, dict]):
                The request object. The request sent to
                CreateIdentityAwareProxyClient.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iap_v1.types.IdentityAwareProxyClient:
                Contains the data that describes an
                Identity Aware Proxy owned client.

        """
        # Create or coerce a protobuf request object.
        request = service.CreateIdentityAwareProxyClientRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_identity_aware_proxy_client,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def list_identity_aware_proxy_clients(
        self,
        request: Union[service.ListIdentityAwareProxyClientsRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListIdentityAwareProxyClientsAsyncPager:
        r"""Lists the existing clients for the brand.

        .. code-block:: python

            from google.cloud import iap_v1

            def sample_list_identity_aware_proxy_clients():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceClient()

                # Initialize request argument(s)
                request = iap_v1.ListIdentityAwareProxyClientsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_identity_aware_proxy_clients(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.iap_v1.types.ListIdentityAwareProxyClientsRequest, dict]):
                The request object. The request sent to
                ListIdentityAwareProxyClients.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iap_v1.services.identity_aware_proxy_o_auth_service.pagers.ListIdentityAwareProxyClientsAsyncPager:
                Response message for
                ListIdentityAwareProxyClients.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        request = service.ListIdentityAwareProxyClientsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_identity_aware_proxy_clients,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListIdentityAwareProxyClientsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_identity_aware_proxy_client(
        self,
        request: Union[service.GetIdentityAwareProxyClientRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.IdentityAwareProxyClient:
        r"""Retrieves an Identity Aware Proxy (IAP) OAuth client.
        Requires that the client is owned by IAP.


        .. code-block:: python

            from google.cloud import iap_v1

            def sample_get_identity_aware_proxy_client():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceClient()

                # Initialize request argument(s)
                request = iap_v1.GetIdentityAwareProxyClientRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_identity_aware_proxy_client(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.iap_v1.types.GetIdentityAwareProxyClientRequest, dict]):
                The request object. The request sent to
                GetIdentityAwareProxyClient.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iap_v1.types.IdentityAwareProxyClient:
                Contains the data that describes an
                Identity Aware Proxy owned client.

        """
        # Create or coerce a protobuf request object.
        request = service.GetIdentityAwareProxyClientRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_identity_aware_proxy_client,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def reset_identity_aware_proxy_client_secret(
        self,
        request: Union[service.ResetIdentityAwareProxyClientSecretRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.IdentityAwareProxyClient:
        r"""Resets an Identity Aware Proxy (IAP) OAuth client
        secret. Useful if the secret was compromised. Requires
        that the client is owned by IAP.


        .. code-block:: python

            from google.cloud import iap_v1

            def sample_reset_identity_aware_proxy_client_secret():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceClient()

                # Initialize request argument(s)
                request = iap_v1.ResetIdentityAwareProxyClientSecretRequest(
                    name="name_value",
                )

                # Make the request
                response = client.reset_identity_aware_proxy_client_secret(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.iap_v1.types.ResetIdentityAwareProxyClientSecretRequest, dict]):
                The request object. The request sent to
                ResetIdentityAwareProxyClientSecret.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.iap_v1.types.IdentityAwareProxyClient:
                Contains the data that describes an
                Identity Aware Proxy owned client.

        """
        # Create or coerce a protobuf request object.
        request = service.ResetIdentityAwareProxyClientSecretRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.reset_identity_aware_proxy_client_secret,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def delete_identity_aware_proxy_client(
        self,
        request: Union[service.DeleteIdentityAwareProxyClientRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes an Identity Aware Proxy (IAP) OAuth client.
        Useful for removing obsolete clients, managing the
        number of clients in a given project, and cleaning up
        after tests. Requires that the client is owned by IAP.


        .. code-block:: python

            from google.cloud import iap_v1

            def sample_delete_identity_aware_proxy_client():
                # Create a client
                client = iap_v1.IdentityAwareProxyOAuthServiceClient()

                # Initialize request argument(s)
                request = iap_v1.DeleteIdentityAwareProxyClientRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_identity_aware_proxy_client(request=request)

        Args:
            request (Union[google.cloud.iap_v1.types.DeleteIdentityAwareProxyClientRequest, dict]):
                The request object. The request sent to
                DeleteIdentityAwareProxyClient.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        request = service.DeleteIdentityAwareProxyClientRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_identity_aware_proxy_client,
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
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-iap",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("IdentityAwareProxyOAuthServiceAsyncClient",)
