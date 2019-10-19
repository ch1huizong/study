
### 一. docker命令

1. 构建
    + build 
        * -t
        * -q
2. 运行
    + run
        * -it
        * -d
        * --env/e
        * --restart
        * --entrypoint
        * --read-only
        * -v
        * --volumes-from
        * --net
            - none
            - bridge
            - container:<name>
            - host
        * --hostname
        * --dns
        * --dns-search
        * --add-host
        * -p | -P
        * --expose
        * --link
    + exec
    + create
        * --cidfile
    + start

3. 查看
    + ps
        * -lq
        * -a
    + inspect
        * -f
    + logs
        * -f
    + top
    + port
    + diff
    + images

4. 停止
    + stop
    + restart
    + rm
        * -v
        * -f
    + kill

5. 推送
    + push
    + pull
    + tag
    + commit
        * -a
        * -m 
    + rename

---

### 二. docker-compose

1. 文件写法

---

### 三. 设计问题

1. 镜像设计

2. 镜像存储

3. 私密文件的分发?

4. 代码提交/镜像构建/上传/测试/部署 自动化?
