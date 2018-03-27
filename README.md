# nginx-grpc

## 测试NGINX的v1.13.10原生支持gRPC通信

**参考文档**

- [Introducing gRPC Support with NGINX 1.13.10](https://www.nginx.com/blog/nginx-1-13-10-grpc/)
- [Module ngx_http_grpc_module](http://nginx.org/en/docs/http/ngx_http_grpc_module.html)

可以使用nginx转发各个服务，相较与服务注册发现，是另一种可选实现方式。

```
location /helloworld.Greeter {
    grpc_pass grpc://127.0.0.1:50051;
}
location /helloworld.Dispatcher {
    grpc_pass grpc://127.0.0.1:50052;
}
```

**示例代码**

- [服务定义proto文件](protos/helloworld.proto)
- [nginx配置](nginx/grpc.conf)
- [gRPC服务端代码](python3/greeter_server.py)
- [gRPC客户端代码](python3/greeter_cient.py)
- [gRPC压力测试代码](python3/greeter_cient_timeit.py)

