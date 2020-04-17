# 百度站长主动推送脚本

> 个人网站建立之后想让搜索引擎收录是一件麻烦事，对于Google还好，但是对于百度而言，可能会相当慢
>
> 主动推送是链接提交最快速，收录最快的方式
>
> 如果按照每天一次的主动推送，可能很快百度就会收录你的URL
>
> 脚本实现百度站长主动推送URLS，以实现最快收录

这里的脚本使用语言为Python，使用很简单。

1. 首先得有Python环境

2. 只需要将 

   1. 你在百度站长注册的网站

   2. 主动推送的token给替换代码中指定的部分即可

      ``` python
      re_try = 50 # 服务器错误之后重新尝试的次数 默认50次
      Your_website = "xxxxxxxx" # the url record in your baidu_website
      Your_token = "xxxxxxxx" # find it in your baidu_token
      sleep_time = 1 # 默认每隔1秒请求一次
      ```

      

3. 然后将url 以每行一条的格式写入 urls.txt文件

4. 将tool.py 和  urls.txt 放在同一文件夹下。

5. 命令行进入这一文件夹下

   ``` python
   python tool.py
   ```

   即可自动执行

这是个简单的脚本，不必多言了。

