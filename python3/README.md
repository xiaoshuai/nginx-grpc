## 使用Python开发gRPC应用

使用`pip install grpcio`安装运行时依赖
使用`pip install grpcio-tools`安装代码生成工具

使用helloworld.proto生成Python版代码

```
python -m grpc.tools.protoc \
     -I../protos --proto_path=../protos \
     --python_out=. \
     --grpc_python_out=grpc_2_0:. \
     ../protos/helloworld.proto
```
