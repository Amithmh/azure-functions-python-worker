import json
import types
import typing

from azure.functions import _abc as azf_abc
from azure.functions import _http as azf_http

from . import meta
from .. import protos


class HttpRequest(azf_abc.HttpRequest):
    """An HTTP request object."""

    def __init__(self, method: str, url: str,
                 headers: typing.Mapping[str, str],
                 params: typing.Mapping[str, str],
                 body_type: meta.TypedDataKind,
                 body: typing.Union[str, bytes]) -> None:
        self.__method = method
        self.__url = url
        self.__headers = azf_http.HttpRequestHeaders(headers)
        self.__params = types.MappingProxyType(params)
        self.__body_type = body_type
        self.__body = body

    @property
    def url(self):
        return self.__url

    @property
    def method(self):
        return self.__method.upper()

    @property
    def headers(self):
        return self.__headers

    @property
    def params(self):
        return self.__params

    def get_body(self) -> typing.Union[str, bytes]:
        return self.__body

    def get_json(self) -> typing.Any:
        if self.__body_type is meta.TypedDataKind.json:
            return json.loads(self.__body)
        raise ValueError('HTTP request does not have JSON data attached')


class HttpResponseConverter(meta.OutConverter,
                            binding=meta.Binding.http):

    @classmethod
    def check_python_type(cls, pytype: type) -> bool:
        return issubclass(pytype, (azf_abc.HttpResponse, str))

    @classmethod
    def to_proto(cls, obj: typing.Any) -> protos.TypedData:
        if isinstance(obj, str):
            return protos.TypedData(string=obj)

        if isinstance(obj, azf_abc.HttpResponse):
            status = obj.status_code
            headers = dict(obj.headers)
            if 'content-type' not in headers:
                if obj.mimetype.startswith('text/'):
                    ct = f'{obj.mimetype}; charset={obj.charset}'
                else:
                    ct = f'{obj.mimetype}'
                headers['content-type'] = ct

            body = obj.get_body()
            if body is not None:
                body = protos.TypedData(bytes=body)
            else:
                body = protos.TypedData(bytes=b'')

            return protos.TypedData(
                http=protos.RpcHttp(
                    status_code=str(status),
                    headers=headers,
                    is_raw=True,
                    body=body))

        raise NotImplementedError


class HttpRequestConverter(meta.InConverter,
                           binding=meta.Binding.httpTrigger):

    @classmethod
    def check_python_type(cls, pytype: type) -> bool:
        return issubclass(pytype, azf_abc.HttpRequest)

    @classmethod
    def from_proto(cls, data: protos.TypedData,
                   trigger_metadata) -> typing.Any:
        if data.WhichOneof('data') != 'http':
            raise NotImplementedError

        body_rpc_val = data.http.body
        body_rpc_type = body_rpc_val.WhichOneof('data')

        if body_rpc_type == 'json':
            body_type = meta.TypedDataKind.json
            body = body_rpc_val.json
        elif body_rpc_type == 'string':
            body_type = meta.TypedDataKind.string
            body = body_rpc_val.string
        elif body_rpc_type == 'bytes':
            body_type = meta.TypedDataKind.bytes
            body = body_rpc_val.bytes
        elif body_rpc_type is None:
            # Means an empty HTTP request body -- we don't want
            # `HttpResponse.get_body()` to return None as it would
            # make it more complicated to work with than necessary.
            # Therefore we normalize the body to an empty bytes
            # object.
            body_type = meta.TypedDataKind.bytes
            body = ''
        else:
            raise TypeError(
                f'unsupported HTTP body type from the incoming gRPC data: '
                f'{body_rpc_type}')

        return HttpRequest(
            method=data.http.method,
            url=data.http.url,
            headers=data.http.headers,
            params=data.http.query,
            body_type=body_type,
            body=body)
