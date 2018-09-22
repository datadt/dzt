# dzt
[模拟登陆店侦探](https://www.dianzhentan.com/base/)
--简单的数字验证码识别学习(Tesseract模块)


一个重要的逻辑思维是：

验证码识别率并非100%，如若错误，

1. 验证码长度不等于4，点击验证码图片刷新，获取新验证码并重新识别；

2. 验证码长度等于4，但识别有误，点击登陆后网址并不跳转变化则认为登陆有误；

3. 发生错误时，重新执行登陆过程中输入用户名、密码、验证码识别整个流程。

![Image](https://github.com/datadt/dzt/blob/master/dzt.jpg)
