from __future__ import print_function

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

req_msg = helloworld_pb2.HelloRequest(name='user_name')
channel_f = grpc.insecure_channel('localhost:5000')
stub_f = helloworld_pb2_grpc.GreeterStub(channel_f)


def f():
    stub_f.SayHello(req_msg)


def g():
    channel_g = grpc.insecure_channel('localhost:5000')
    stub_g = helloworld_pb2_grpc.GreeterStub(channel_g)
    stub_g.SayHello(req_msg)


def run_timeit_f():
    import timeit
    # timit grpc call with existing connection: 0.010163834000195493
    stat_cost_time = timeit.timeit('[func() for func in (f,)]', globals=globals(), number=100)
    print('timit grpc call with existing connection:', stat_cost_time)


def run_timeit_g():
    import timeit
    # timit grpc call with new connection: 0.017706901000565267
    stat_cost_time = timeit.timeit('[func() for func in (g,)]', globals=globals(), number=10)
    print('timit grpc call with new connection:', stat_cost_time)


if __name__ == '__main__':
    run_timeit_f()
    run_timeit_g()
