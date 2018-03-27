## 使用Homebrew安装nginx

编辑配置文件`/usr/local/etc/nginx/servers/grpc.conf`，使用`brew services restart nginx`重启服务

```
server {
    listen 5000 http2;

    access_log /Users/xiaoshuai/Library/Logs/nginx/access-grpc.log main;

    location / {
        grpc_pass grpc://localhost:50050;
    }

    location /helloworld.Greeter {
        grpc_pass grpc://localhost:50051;
    }
}
```


使用`tail -1f /Users/xiaoshuai/Library/Logs/nginx/access-grpc.log`查看日志输出