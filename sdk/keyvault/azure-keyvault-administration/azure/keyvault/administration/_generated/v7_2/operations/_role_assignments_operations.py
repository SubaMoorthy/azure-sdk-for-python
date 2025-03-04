# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Iterable, Optional, TypeVar
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_delete_request(
    scope,  # type: str
    role_assignment_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "7.2")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, 'str', skip_quote=True),
        "roleAssignmentName": _SERIALIZER.url("role_assignment_name", role_assignment_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_create_request(
    scope,  # type: str
    role_assignment_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "7.2")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, 'str', skip_quote=True),
        "roleAssignmentName": _SERIALIZER.url("role_assignment_name", role_assignment_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_get_request(
    scope,  # type: str
    role_assignment_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "7.2")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, 'str', skip_quote=True),
        "roleAssignmentName": _SERIALIZER.url("role_assignment_name", role_assignment_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_list_for_scope_request(
    scope,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "7.2")  # type: str
    filter = kwargs.pop('filter', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Authorization/roleAssignments")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, 'str', skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if filter is not None:
        _query_parameters['$filter'] = _SERIALIZER.query("filter", filter, 'str')
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class RoleAssignmentsOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.keyvault.v7_2.KeyVaultClient`'s
        :attr:`role_assignments` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")


    @distributed_trace
    def delete(
        self,
        vault_base_url,  # type: str
        scope,  # type: str
        role_assignment_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.RoleAssignment"
        """Deletes a role assignment.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param scope: The scope of the role assignment to delete.
        :type scope: str
        :param role_assignment_name: The name of the role assignment to delete.
        :type role_assignment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleAssignment, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_2.models.RoleAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RoleAssignment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.2")  # type: str

        
        request = build_delete_request(
            scope=scope,
            role_assignment_name=role_assignment_name,
            api_version=api_version,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('RoleAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    delete.metadata = {'url': "/{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}"}  # type: ignore


    @distributed_trace
    def create(
        self,
        vault_base_url,  # type: str
        scope,  # type: str
        role_assignment_name,  # type: str
        parameters,  # type: "_models.RoleAssignmentCreateParameters"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.RoleAssignment"
        """Creates a role assignment.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param scope: The scope of the role assignment to create.
        :type scope: str
        :param role_assignment_name: The name of the role assignment to create. It can be any valid
         GUID.
        :type role_assignment_name: str
        :param parameters: Parameters for the role assignment.
        :type parameters: ~azure.keyvault.v7_2.models.RoleAssignmentCreateParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleAssignment, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_2.models.RoleAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RoleAssignment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.2")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'RoleAssignmentCreateParameters')

        request = build_create_request(
            scope=scope,
            role_assignment_name=role_assignment_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.create.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('RoleAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': "/{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}"}  # type: ignore


    @distributed_trace
    def get(
        self,
        vault_base_url,  # type: str
        scope,  # type: str
        role_assignment_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.RoleAssignment"
        """Get the specified role assignment.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param scope: The scope of the role assignment.
        :type scope: str
        :param role_assignment_name: The name of the role assignment to get.
        :type role_assignment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleAssignment, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_2.models.RoleAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RoleAssignment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.2")  # type: str

        
        request = build_get_request(
            scope=scope,
            role_assignment_name=role_assignment_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('RoleAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/{scope}/providers/Microsoft.Authorization/roleAssignments/{roleAssignmentName}"}  # type: ignore


    @distributed_trace
    def list_for_scope(
        self,
        vault_base_url,  # type: str
        scope,  # type: str
        filter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.RoleAssignmentListResult"]
        """Gets role assignments for a scope.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param scope: The scope of the role assignments.
        :type scope: str
        :param filter: The filter to apply on the operation. Use $filter=atScope() to return all role
         assignments at or above the scope. Use $filter=principalId eq {id} to return all role
         assignments at, above or below the scope for the specified principal. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either RoleAssignmentListResult or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.keyvault.v7_2.models.RoleAssignmentListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "7.2")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RoleAssignmentListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_for_scope_request(
                    scope=scope,
                    api_version=api_version,
                    filter=filter,
                    template_url=self.list_for_scope.metadata['url'],
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:
                
                request = build_list_for_scope_request(
                    scope=scope,
                    api_version=api_version,
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

                path_format_arguments = {
                    "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
                }
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("RoleAssignmentListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_for_scope.metadata = {'url': "/{scope}/providers/Microsoft.Authorization/roleAssignments"}  # type: ignore
