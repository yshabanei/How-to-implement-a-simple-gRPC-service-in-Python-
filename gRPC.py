from concurrent import futures
import grpc
import test_pb2
import test_pb2_grpc

# پیاده‌سازی سرویس تعریف‌شده
class GreeterServicer(test_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return test_pb2.HelloReply(message=f'Hello, {request.name}!')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
