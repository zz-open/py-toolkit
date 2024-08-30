## 打包成二进制
```shell
pyinstaller --clean --add-data stealth.min.js:stealth.min.js --distpath ./ -n ALiDmsLogin -F main.py
```

## freeze requirements.txt
```shell
pipreqs.exe . --force
```

## 如何使用
### 1. 源码执行
- conda env create -n automation
- pip install -r requirements.txt
- playwright install
- 根据conf.yaml.example模板 创建自己的配置文件，并替换为自己的参数
- windows执行run.bat, Linux执行run.sh
  
### 2.二进制文件
- 项目自带windows exe
- exe同级目录下，根据conf.yaml.example模板 创建自己的配置文件，并替换为自己的参数
- 点击执行
- mac,linux平台请自行打包


## 注意
- playwright运行过程中与浏览器进程进行了捆绑，控制台和浏览器必须同时存在才可正产运行，不可关闭控制台
- playwright没有提供永久阻塞浏览器的机制，目前是通过wait_for_timeout 加一个相对长的时间来达到目的

# FAQ
- 代码中没有对随机出现的滑块验证做逻辑处理，碰见了重新运行脚本即可
- 代码中加入了stealth.min.js 用于防检测



## 备忘录
- playwright codegen
- C:\Users\zaizai\AppData\Local\ms-playwright\chromium-1097