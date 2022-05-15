# shop_api
fast API 기반 프로젝트를 git action으로 배포 연습  
(git action, docker hub, home server 활용)

# 도커를 통한 실행
```shell
$ poetry install
$ uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
