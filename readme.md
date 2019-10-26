# 同韵查询 telegram bot
利用`telegram`的`bot`接口，设计了输入汉字即返回与其同韵同调汉字功能的`bot`，可用于编顺口溜、打油诗。 使用`demo`见[TongYunBot](https://t.me/TongYunBot).

#### 代码使用说明
+ 注册`telegram bot`, 记住`token`
+ 安装[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot/)
+ 修改`tongyun_bot.py` 中的token为自己获取的值
```python
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("00000000:xxxxxxxxxxxxxxxxxxxxxxxxxxxx") 
```
+ 执行 `nohup python tongyun_bot.py >/dev/null 2>&1 &` 开始运行
+ 到自己`Telegram`中测试一下是否成功

#### 数据说明
+ `tongyun_bot.py` 修改自[echobot2.py](https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py)
+ `hanzi.txt` 来自于[常用6763个汉字使用频率表](https://github.com/sxei/pinyinjs/blob/master/other/常用6763个汉字使用频率表.txt)
+ `yunbiao.txt` 来自于[同韵字典](http://www.iguci.cn/dictionary/yunzhe.php)，并手动分开u和ü的数据。
+ 感谢上述数据源。