# StackTracer

--------------
StackTracer is a sublime plugin to map `ruby` stack backtrace to source code and provide ability to jump between source code quickly.

[![stack tracer](http://i4.buimg.com/519918/2ce6d6b1a6364837.png)](http://recordit.co/WajAtOauVO)

## Usage
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
