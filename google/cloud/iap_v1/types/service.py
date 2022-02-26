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
import proto  # type: ignore

from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import wrappers_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.iap.v1",
    manifest={
        "GetIapSettingsRequest",
        "UpdateIapSettingsRequest",
        "IapSettings",
        "AccessSettings",
        "GcipSettings",
        "CorsSettings",
        "OAuthSettings",
        "ApplicationSettings",
        "CsmSettings",
        "AccessDeniedPageSettings",
        "ListBrandsRequest",
        "ListBrandsResponse",
        "CreateBrandRequest",
        "GetBrandRequest",
        "ListIdentityAwareProxyClientsRequest",
        "ListIdentityAwareProxyClientsResponse",
        "CreateIdentityAwareProxyClientRequest",
        "GetIdentityAwareProxyClientRequest",
        "ResetIdentityAwareProxyClientSecretRequest",
        "DeleteIdentityAwareProxyClientRequest",
        "Brand",
        "IdentityAwareProxyClient",
    },
)


class GetIapSettingsRequest(proto.Message):
    r"""The request sent to GetIapSettings.

    Attributes:
        name (str):
            Required. The resource name for which to retrieve the
            settings. Authorization: Requires the ``getSettings``
            permission for the associated resource.
    """

    name = proto.Field(proto.STRING, number=1,)


class UpdateIapSettingsRequest(proto.Message):
    r"""The request sent to UpdateIapSettings.

    Attributes:
        iap_settings (google.cloud.iap_v1.types.IapSettings):
            Required. The new values for the IAP settings to be updated.
            Authorization: Requires the ``updateSettings`` permission
            for the associated resource.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The field mask specifying which IAP settings
            should be updated. If omitted, the all of the
            settings are updated. See
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
    """

    iap_settings = proto.Field(proto.MESSAGE, number=1, message="IapSettings",)
    update_mask = proto.Field(
        proto.MESSAGE, number=2, message=field_mask_pb2.FieldMask,
    )


class IapSettings(proto.Message):
    r"""The IAP configurable settings.

    Attributes:
        name (str):
            Required. The resource name of the IAP
            protected resource.
        access_settings (google.cloud.iap_v1.types.AccessSettings):
            Top level wrapper for all access related
            setting in IAP
        application_settings (google.cloud.iap_v1.types.ApplicationSettings):
            Top level wrapper for all application related
            settings in IAP
    """

    name = proto.Field(proto.STRING, number=1,)
    access_settings = proto.Field(proto.MESSAGE, number=5, message="AccessSettings",)
    application_settings = proto.Field(
        proto.MESSAGE, number=6, message="ApplicationSettings",
    )


class AccessSettings(proto.Message):
    r"""Access related settings for IAP protected apps.

    Attributes:
        gcip_settings (google.cloud.iap_v1.types.GcipSettings):
            GCIP claims and endpoint configurations for
            3p identity providers.
        cors_settings (google.cloud.iap_v1.types.CorsSettings):
            Configuration to allow cross-origin requests
            via IAP.
        oauth_settings (google.cloud.iap_v1.types.OAuthSettings):
            Settings to configure IAP's OAuth behavior.
    """

    gcip_settings = proto.Field(proto.MESSAGE, number=1, message="GcipSettings",)
    cors_settings = proto.Field(proto.MESSAGE, number=2, message="CorsSettings",)
    oauth_settings = proto.Field(proto.MESSAGE, number=3, message="OAuthSettings",)


class GcipSettings(proto.Message):
    r"""Allows customers to configure tenant_id for GCIP instance per-app.

    Attributes:
        tenant_ids (Sequence[str]):
            GCIP tenant ids that are linked to the IAP resource.
            tenant_ids could be a string beginning with a number
            character to indicate authenticating with GCIP tenant flow,
            or in the format of \_ to indicate authenticating with GCIP
            agent flow. If agent flow is used, tenant_ids should only
            contain one single element, while for tenant flow,
            tenant_ids can contain multiple elements.
        login_page_uri (google.protobuf.wrappers_pb2.StringValue):
            Login page URI associated with the GCIP
            tenants. Typically, all resources within the
            same project share the same login page, though
            it could be overridden at the sub resource
            level.
    """

    tenant_ids = proto.RepeatedField(proto.STRING, number=1,)
    login_page_uri = proto.Field(
        proto.MESSAGE, number=2, message=wrappers_pb2.StringValue,
    )


class CorsSettings(proto.Message):
    r"""Allows customers to configure HTTP request paths that'll
    allow HTTP OPTIONS call to bypass authentication and
    authorization.

    Attributes:
        allow_http_options (google.protobuf.wrappers_pb2.BoolValue):
            Configuration to allow HTTP OPTIONS calls to
            skip authorization. If undefined, IAP will not
            apply any special logic to OPTIONS requests.
    """

    allow_http_options = proto.Field(
        proto.MESSAGE, number=1, message=wrappers_pb2.BoolValue,
    )


class OAuthSettings(proto.Message):
    r"""Configuration for OAuth login&consent flow behavior as well
    as for OAuth Credentials.

    Attributes:
        login_hint (google.protobuf.wrappers_pb2.StringValue):
            Domain hint to send as hd=? parameter in
            OAuth request flow. Enables redirect to primary
            IDP by skipping Google's login screen.
            https://developers.google.com/identity/protocols/OpenIDConnect#hd-param
            Note: IAP does not verify that the id token's hd
            claim matches this value since access behavior
            is managed by IAM policies.
    """

    login_hint = proto.Field(proto.MESSAGE, number=2, message=wrappers_pb2.StringValue,)


class ApplicationSettings(proto.Message):
    r"""Wrapper over application specific settings for IAP.

    Attributes:
        csm_settings (google.cloud.iap_v1.types.CsmSettings):
            Settings to configure IAP's behavior for a
            CSM mesh.
        access_denied_page_settings (google.cloud.iap_v1.types.AccessDeniedPageSettings):
            Customization for Access Denied page.
        cookie_domain (google.protobuf.wrappers_pb2.StringValue):
            The Domain value to set for cookies generated
            by IAP. This value is not validated by the API,
            but will be ignored at runtime if invalid.
    """

    csm_settings = proto.Field(proto.MESSAGE, number=1, message="CsmSettings",)
    access_denied_page_settings = proto.Field(
        proto.MESSAGE, number=2, message="AccessDeniedPageSettings",
    )
    cookie_domain = proto.Field(
        proto.MESSAGE, number=3, message=wrappers_pb2.StringValue,
    )


class CsmSettings(proto.Message):
    r"""Configuration for RCTokens generated for CSM workloads
    protected by IAP. RCTokens are IAP generated JWTs that can be
    verified at the application. The RCToken is primarily used for
    ISTIO deployments, and can be scoped to a single mesh by
    configuring the audience field accordingly

    Attributes:
        rctoken_aud (google.protobuf.wrappers_pb2.StringValue):
            Audience claim set in the generated RCToken.
            This value is not validated by IAP.
    """

    rctoken_aud = proto.Field(
        proto.MESSAGE, number=1, message=wrappers_pb2.StringValue,
    )


class AccessDeniedPageSettings(proto.Message):
    r"""Custom content configuration for access denied page.
    IAP allows customers to define a custom URI to use as the error
    page when access is denied to users. If IAP prevents access to
    this page, the default IAP error page will be displayed instead.

    Attributes:
        access_denied_page_uri (google.protobuf.wrappers_pb2.StringValue):
            The URI to be redirected to when access is
            denied.
        generate_troubleshooting_uri (google.protobuf.wrappers_pb2.BoolValue):
            Whether to generate a troubleshooting URL on
            access denied events to this application.
    """

    access_denied_page_uri = proto.Field(
        proto.MESSAGE, number=1, message=wrappers_pb2.StringValue,
    )
    generate_troubleshooting_uri = proto.Field(
        proto.MESSAGE, number=2, message=wrappers_pb2.BoolValue,
    )


class ListBrandsRequest(proto.Message):
    r"""The request sent to ListBrands.

    Attributes:
        parent (str):
            Required. GCP Project number/id. In the following format:
            projects/{project_number/id}.
    """

    parent = proto.Field(proto.STRING, number=1,)


class ListBrandsResponse(proto.Message):
    r"""Response message for ListBrands.

    Attributes:
        brands (Sequence[google.cloud.iap_v1.types.Brand]):
            Brands existing in the project.
    """

    brands = proto.RepeatedField(proto.MESSAGE, number=1, message="Brand",)


class CreateBrandRequest(proto.Message):
    r"""The request sent to CreateBrand.

    Attributes:
        parent (str):
            Required. GCP Project number/id under which the brand is to
            be created. In the following format:
            projects/{project_number/id}.
        brand (google.cloud.iap_v1.types.Brand):
            Required. The brand to be created.
    """

    parent = proto.Field(proto.STRING, number=1,)
    brand = proto.Field(proto.MESSAGE, number=2, message="Brand",)


class GetBrandRequest(proto.Message):
    r"""The request sent to GetBrand.

    Attributes:
        name (str):
            Required. Name of the brand to be fetched. In the following
            format: projects/{project_number/id}/brands/{brand}.
    """

    name = proto.Field(proto.STRING, number=1,)


class ListIdentityAwareProxyClientsRequest(proto.Message):
    r"""The request sent to ListIdentityAwareProxyClients.

    Attributes:
        parent (str):
            Required. Full brand path. In the following format:
            projects/{project_number/id}/brands/{brand}.
        page_size (int):
            The maximum number of clients to return. The
            service may return fewer than this value.
            If unspecified, at most 100 clients will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListIdentityAwareProxyClients`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListIdentityAwareProxyClients`` must match the call that
            provided the page token.
    """

    parent = proto.Field(proto.STRING, number=1,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)


class ListIdentityAwareProxyClientsResponse(proto.Message):
    r"""Response message for ListIdentityAwareProxyClients.

    Attributes:
        identity_aware_proxy_clients (Sequence[google.cloud.iap_v1.types.IdentityAwareProxyClient]):
            Clients existing in the brand.
        next_page_token (str):
            A token, which can be send as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    identity_aware_proxy_clients = proto.RepeatedField(
        proto.MESSAGE, number=1, message="IdentityAwareProxyClient",
    )
    next_page_token = proto.Field(proto.STRING, number=2,)


class CreateIdentityAwareProxyClientRequest(proto.Message):
    r"""The request sent to CreateIdentityAwareProxyClient.

    Attributes:
        parent (str):
            Required. Path to create the client in. In the following
            format: projects/{project_number/id}/brands/{brand}. The
            project must belong to a G Suite account.
        identity_aware_proxy_client (google.cloud.iap_v1.types.IdentityAwareProxyClient):
            Required. Identity Aware Proxy Client to be
            created.
    """

    parent = proto.Field(proto.STRING, number=1,)
    identity_aware_proxy_client = proto.Field(
        proto.MESSAGE, number=2, message="IdentityAwareProxyClient",
    )


class GetIdentityAwareProxyClientRequest(proto.Message):
    r"""The request sent to GetIdentityAwareProxyClient.

    Attributes:
        name (str):
            Required. Name of the Identity Aware Proxy client to be
            fetched. In the following format:
            projects/{project_number/id}/brands/{brand}/identityAwareProxyClients/{client_id}.
    """

    name = proto.Field(proto.STRING, number=1,)


class ResetIdentityAwareProxyClientSecretRequest(proto.Message):
    r"""The request sent to ResetIdentityAwareProxyClientSecret.

    Attributes:
        name (str):
            Required. Name of the Identity Aware Proxy client to that
            will have its secret reset. In the following format:
            projects/{project_number/id}/brands/{brand}/identityAwareProxyClients/{client_id}.
    """

    name = proto.Field(proto.STRING, number=1,)


class DeleteIdentityAwareProxyClientRequest(proto.Message):
    r"""The request sent to DeleteIdentityAwareProxyClient.

    Attributes:
        name (str):
            Required. Name of the Identity Aware Proxy client to be
            deleted. In the following format:
            projects/{project_number/id}/brands/{brand}/identityAwareProxyClients/{client_id}.
    """

    name = proto.Field(proto.STRING, number=1,)


class Brand(proto.Message):
    r"""OAuth brand data.
    NOTE: Only contains a portion of the data that describes a
    brand.

    Attributes:
        name (str):
            Output only. Identifier of the brand.
            NOTE: GCP project number achieves the same brand
            identification purpose as only one brand per
            project can be created.
        support_email (str):
            Support email displayed on the OAuth consent
            screen.
        application_title (str):
            Application name displayed on OAuth consent
            screen.
        org_internal_only (bool):
            Output only. Whether the brand is only
            intended for usage inside the G Suite
            organization only.
    """

    name = proto.Field(proto.STRING, number=1,)
    support_email = proto.Field(proto.STRING, number=2,)
    application_title = proto.Field(proto.STRING, number=3,)
    org_internal_only = proto.Field(proto.BOOL, number=4,)


class IdentityAwareProxyClient(proto.Message):
    r"""Contains the data that describes an Identity Aware Proxy
    owned client.

    Attributes:
        name (str):
            Output only. Unique identifier of the OAuth
            client.
        secret (str):
            Output only. Client secret of the OAuth
            client.
        display_name (str):
            Human-friendly name given to the OAuth
            client.
    """

    name = proto.Field(proto.STRING, number=1,)
    secret = proto.Field(proto.STRING, number=2,)
    display_name = proto.Field(proto.STRING, number=3,)


__all__ = tuple(sorted(__protobuf__.manifest))
