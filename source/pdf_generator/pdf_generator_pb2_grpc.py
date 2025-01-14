# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pdf_generator_pb2 as pdf__generator__pb2


class Pdf_generatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create_pdf = channel.unary_unary(
                '/Pdf_generator/create_pdf',
                request_serializer=pdf__generator__pb2.patient_data.SerializeToString,
                response_deserializer=pdf__generator__pb2.back_response.FromString,
                )


class Pdf_generatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create_pdf(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Pdf_generatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create_pdf': grpc.unary_unary_rpc_method_handler(
                    servicer.create_pdf,
                    request_deserializer=pdf__generator__pb2.patient_data.FromString,
                    response_serializer=pdf__generator__pb2.back_response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Pdf_generator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Pdf_generator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create_pdf(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Pdf_generator/create_pdf',
            pdf__generator__pb2.patient_data.SerializeToString,
            pdf__generator__pb2.back_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
