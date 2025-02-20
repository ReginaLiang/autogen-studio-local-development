## 本地调试：
```
uvicorn web.app:app --reload --port 8081
```

## docker 部署
```
docker build -t fastapi-app-new .

docker run -d -p 8081:8081 fastapi-app-new
```
