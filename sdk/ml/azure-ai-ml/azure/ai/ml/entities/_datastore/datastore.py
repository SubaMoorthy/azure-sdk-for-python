# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# pylint: disable=protected-access,redefined-builtin,arguments-renamed

from abc import ABC, abstractclassmethod, abstractmethod
from os import PathLike
from pathlib import Path
from typing import IO, Any, AnyStr, Dict, Union

from azure.ai.ml._restclient.v2022_05_01.models import DatastoreData, DatastoreType
from azure.ai.ml._utils.utils import camel_to_snake, dump_yaml_to_file
from azure.ai.ml.constants._common import BASE_PATH_CONTEXT_KEY, PARAMS_OVERRIDE_KEY, CommonYamlFields
from azure.ai.ml.entities._datastore.credentials import NoneCredentials
from azure.ai.ml.entities._mixins import RestTranslatableMixin
from azure.ai.ml.entities._resource import Resource
from azure.ai.ml.entities._util import find_type_in_override
from azure.ai.ml.exceptions import ErrorCategory, ErrorTarget, ValidationErrorType, ValidationException


class Datastore(Resource, RestTranslatableMixin, ABC):

    """Datastore of an Azure ML workspace, abstract class.

    :param name: Name of the datastore.
    :type name: str
    :param description: Description of the resource.
    :type description: str
    :param credentials: Credentials to use for Azure ML workspace to connect to the storage.
    :type credentials: Union[ServicePrincipalSection, CertificateSection]
    :param tags: Tag dictionary. Tags can be added, removed, and updated.
    :type tags: dict[str, str]
    :param properties: The asset property dictionary.
    :type properties: dict[str, str]
    :param kwargs: A dictionary of additional configuration parameters.
    :type kwargs: dict
    """

    def __init__(
        self,
        credentials: Any,
        name: str = None,
        description: str = None,
        tags: Dict = None,
        properties: Dict = None,
        **kwargs,
    ):
        self._type = kwargs.pop("type", None)
        super().__init__(
            name=name,
            description=description,
            tags=tags,
            properties=properties,
            **kwargs,
        )

        self.credentials = NoneCredentials() if credentials is None else credentials

    @property
    def type(self) -> str:
        return self._type

    def dump(
        self, *args, dest: Union[str, PathLike, IO[AnyStr]] = None, path: Union[str, PathLike] = None, **kwargs
    ) -> None:
        """Dump the datastore content into a file in yaml format.

        :param dest: The destination to receive this datastore's content.
            Must be either a path to a local file, or an already-open file stream.
            If dest is a file path, a new file will be created,
            and an exception is raised if the file exists.
            If dest is an open file, the file will be written to directly,
            and an exception will be raised if the file is not writable.
        :type dest: Union[PathLike, str, IO[AnyStr]]
        :param path: Deprecated path to a local file as the target, a new file
            will be created, raises exception if the file exists.
            It's recommended what you change 'path=' inputs to 'dest='.
            The first unnamed input of this function will also be treated like
            a path input.
        :type path: Union[str, Pathlike]
        """
        yaml_serialized = self._to_dict()
        dump_yaml_to_file(dest, yaml_serialized, default_flow_style=False, path=path, args=args, **kwargs)

    @abstractmethod
    def _to_dict(self) -> Dict:
        pass

    @classmethod
    def _load(
        cls,
        data: Dict = None,
        yaml_path: Union[PathLike, str] = None,
        params_override: list = None,
        **kwargs,
    ) -> "Datastore":
        data = data or {}
        params_override = params_override or []

        context = {
            BASE_PATH_CONTEXT_KEY: Path(yaml_path).parent if yaml_path else Path("./"),
            PARAMS_OVERRIDE_KEY: params_override,
        }

        from azure.ai.ml.entities import (
            AzureBlobDatastore,
            AzureDataLakeGen1Datastore,
            AzureDataLakeGen2Datastore,
            AzureFileDatastore,
        )

        # from azure.ai.ml.entities._datastore._on_prem import (
        #     HdfsDatastore
        # )

        ds_type = None
        type_in_override = find_type_in_override(params_override)
        type = type_in_override or data.get(
            CommonYamlFields.TYPE, DatastoreType.AZURE_BLOB
        )  # override takes the priority

        # yaml expects snake casing, while service side constants are camel casing
        if type == camel_to_snake(DatastoreType.AZURE_BLOB):
            ds_type = AzureBlobDatastore
        elif type == camel_to_snake(DatastoreType.AZURE_FILE):
            ds_type = AzureFileDatastore
        elif type == camel_to_snake(DatastoreType.AZURE_DATA_LAKE_GEN1):
            ds_type = AzureDataLakeGen1Datastore
        elif type == camel_to_snake(DatastoreType.AZURE_DATA_LAKE_GEN2):
            ds_type = AzureDataLakeGen2Datastore
        # disable unless preview release
        # elif type == camel_to_snake(DatastoreTypePreview.HDFS):
        #    ds_type = HdfsDatastore
        else:
            msg = f"Unsupported datastore type: {type}."
            raise ValidationException(
                message=msg,
                error_type=ValidationErrorType.INVALID_VALUE,
                target=ErrorTarget.DATASTORE,
                no_personal_data_message=msg,
                error_category=ErrorCategory.USER_ERROR,
            )

        return ds_type._load_from_dict(
            data=data,
            context=context,
            additional_message="If the datastore type is incorrect, change the 'type' property.",
            **kwargs,
        )

    @classmethod
    def _from_rest_object(cls, datastore_resource: DatastoreData) -> "Datastore":

        from azure.ai.ml.entities import (
            AzureBlobDatastore,
            AzureDataLakeGen1Datastore,
            AzureDataLakeGen2Datastore,
            AzureFileDatastore,
        )

        # from azure.ai.ml.entities._datastore._on_prem import (
        #     HdfsDatastore
        # )

        datastore_type = datastore_resource.properties.datastore_type
        if datastore_type == DatastoreType.AZURE_DATA_LAKE_GEN1:
            return AzureDataLakeGen1Datastore._from_rest_object(datastore_resource)
        if datastore_type == DatastoreType.AZURE_DATA_LAKE_GEN2:
            return AzureDataLakeGen2Datastore._from_rest_object(datastore_resource)
        if datastore_type == DatastoreType.AZURE_BLOB:
            return AzureBlobDatastore._from_rest_object(datastore_resource)
        if datastore_type == DatastoreType.AZURE_FILE:
            return AzureFileDatastore._from_rest_object(datastore_resource)
        # disable unless preview release
        # elif datastore_type == DatastoreTypePreview.HDFS:
        #     return HdfsDatastore._from_rest_object(datastore_resource)
        msg = f"Unsupported datastore type {datastore_resource.properties.contents.type}"
        raise ValidationException(
            message=msg,
            error_type=ValidationErrorType.INVALID_VALUE,
            target=ErrorTarget.DATASTORE,
            no_personal_data_message=msg,
            error_category=ErrorCategory.SYSTEM_ERROR,
        )

    @abstractclassmethod
    def _load_from_dict(cls, data: Dict, context: Dict, additional_message: str, **kwargs) -> "Datastore":
        pass

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.type == other.type and self.credentials == other.credentials

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
