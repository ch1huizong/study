
## 一. k8s基础

1. ### kubectl
    **查看**
    - cluster-info
    - get
    - describe 
    - explain
    - logs

    **创建**
    - create -f
    - run (临时Pod)
    - exec (新开进程)
    - attach

    **标注**
    - label
    - annotate

    **网络**
    - expose
    - port-forward

    **删除**
    - delete

    **修改资源**
    - edit
    - patch
    - apply
    - replace
    - set image

    **升级**
    - rolling-update
    - rollout 
        - status （查看）
        - history (升级历史)
        - undo (回滚)
        - pause (暂停升级)
        - resume (恢复升级)
    - cordon
    - drain
    - taint

2. ### 资源
    **单元**
    - Node
    - Pod (基本单位)
    - 标签 (选择器)
    - 注解 (说明)
    - 命名空间 (空间分离)
    - 存活探针 (容器应用是否健康)

    **副本**
    - rc/rs/ds (副本)
    - job/cronjob (临时或定时任务)

    **网络**
    - svc
    - endpoint
    - NodePort/LoadBalancer(公网)/ingress
    - 就绪探针(应用是否就绪)

    **存储**
    - pv
    - pvc
    - sc

    **应用配置**
    - configmap/secret
    - deploy
    - statefulset
    - hpa

    **权限管理**
    - sa
    - role/rolebinding
    - clusterrole/clusterrolebinding
    - pdb
    - psp
    - networkpolicy

3. ### 选择器
    - 节点选择器
    - Pod选择器

## 二. k8s问题

1. ### 实践

    - 基于阿里云组建Ingress服务?

    - 基于业务或其他标准的自动伸缩?
