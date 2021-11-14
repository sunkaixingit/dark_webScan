# web目录扫描

写的太水了，看不下去了~各位自行忽略吧

基于代理的web目录扫描工具
使用python3编写
代理池：https://github.com/jhao104/proxy_pool

## 创建时间 2021-11-14

### 第一次更新：

2021-11-14 19:27:41    版本第一次编写   webScan 1.0

# 工具使用说明
**在渗透测试中扫描web目录会被防火墙等一系列的安全防护措施封禁ip**
**本工具是根据proxy_pool代理池来配置随机代理**
**data目录存放爆破字典**

# proxy_pool配置说明
##### 下载代码：
git clone https://github.com/jhao104/proxy_pool.git
##### 安装依赖：
pip install -r requirements.txt

##### 更新配置:

```
# setting.py 为项目配置文件

# 配置API服务

HOST = "0.0.0.0"               # IP
PORT = 5000                    # 监听端口

# 配置数据库

DB_CONN = 'redis://:pwd@127.0.0.1:6379/0'
#redis无密码 DB_CONN = 'redis://:@127.0.0.1:6379/0'
# 配置 ProxyFetcher
PROXY_FETCHER = [
    "freeProxy01",      # 这里是启用的代理抓取方法名，所有fetch方法位于fetcher/proxyFetcher.py
    "freeProxy02",
    # ....
]
```
启动项目:
##### 如果已经具备运行条件, 可用通过proxyPool.py启动。
###### 程序分为: schedule 调度程序 和 server Api服务

##### 启动调度程序
python3 proxyPool.py schedule

##### 启动webApi服务
python3 proxyPool.py server

##### Docker运行
docker pull jhao104/proxy_pool

docker run --env DB_CONN=redis://:password@ip:port/db -p 5010:5010 jhao104/proxy_pool:latest

-----------------------------------------------------------------------------
### webScan目录扫描

python3 webScan.py 

根据对应提示输入参数即可
