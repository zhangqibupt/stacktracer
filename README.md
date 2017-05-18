#StackTracer

--------------
StackTracer is a sublime plugin to map `ruby` stack backtrace to source code and provide ability to jump between source code quickly.

[![stack tracer](https://nj02all01.baidupcs.com/file/e85af0afb82d4c64fb939317087cf9da?bkt=p3-1400e85af0afb82d4c64fb939317087cf9da8872af3500000003bee7&fid=4245593588-250528-600021547490080&time=1495115748&sign=FDTAXGERLBHS-DCb740ccc5511e5e8fedcff06b081203-xgl9h8ucz8WBJT49g6o0xxy7JWU%3D&to=69&size=245479&sta_dx=245479&sta_cs=1&sta_ft=jpg&sta_ct=0&sta_mt=0&fm2=MH,Nanjing02,Netizen-anywhere,,beijing,cnc&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=1400e85af0afb82d4c64fb939317087cf9da8872af3500000003bee7&sl=76480590&expires=8h&rt=pr&r=229404829&mlogid=3198609294496334832&vuk=4245593588&vbdid=1355571126&fin=%E6%88%AA%E5%9B%BE+2017-05-18+21%E6%97%B655%E5%88%8619%E7%A7%92.jpg&fn=%E6%88%AA%E5%9B%BE+2017-05-18+21%E6%97%B655%E5%88%8619%E7%A7%92.jpg&rtype=1&iv=0&dp-logid=3198609294496334832&dp-callid=0.1.1&hps=1&csl=80&csign=s0ILJ3mG0HUZ2O0S3vp4i8yKWEg%3D&by=themis)](http://recordit.co/WajAtOauVO)

##Usage
1. install stacktracer: press `cmd+shift+p`, select `install package` and then choose 'stacktracer'
2. new a file and paste stack backtrace to it, follow this format:
  ```
  /Users/qzhang/.rvm/gems/ruby-2.1.5/gems/thin-1.6.2/lib/thin/backends/base.rb:73:in `start'
  /Users/qzhang/.rvm/gems/ruby-2.1.5/gems/thin-1.6.2/lib/thin/server.rb:162:in `start'
  /Users/qzhang/.rvm/gems/ruby-2.1.5/gems/rack-1.4.5/lib/rack/handler/thin.rb:13:in `run'
  /Users/qzhang/.rvm/gems/ruby-2.1.5/gems/rack-1.4.5/lib/rack/server.rb:268:in `start'
  ```
3. select the backtrace you paste and press `cmd+shift+p`
4. choose `StackTracer: Build from selection`
5. you can move backward or forward with command `StackTracer: Move backward` and `StackTracer: Move forward`

Also, you can do it with shortcut,
```
ctrl+alt+b : build from selection
ctrl+alt+] : move forward
ctrl+alt+[ : move backward
```

once you run 'build from selection', you can always move forward/backward with shortcut until you run next 'build from selection' command.