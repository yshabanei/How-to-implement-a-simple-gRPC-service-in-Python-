import grpc
import test_pb2
import test_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = test_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(test_pb2.HelloRequest(name='World'))
        print(f"Greeter client received: {response.message}")

if __name__ == '__main__':
    run()
