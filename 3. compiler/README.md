
### go build 如何编译 gin项目

```shell


go mod init projectName 
go mod tidy   



```
* 在同一目录下运行以下命令，以编译 Gin 项目：

```shell

go build

```

如果您的项目中有多个文件，您可以使用以下命令：
```shell

go build -o <可执行文件名> <项目入口文件>
chmod 777 <可执行文件名>

```


其中 <可执行文件名> 是您想要生成的可执行文件的名称， <项目入口文件> 是您的项目中包含 main 函数的文件的路径。

编译成功后，您可以在同一目录下找到可执行文件并运行它：
```shell

./<可执行文件名>
or 

nohub ./<可执行文件名> &
```

如果您的项目中没有指定可执行文件的名称，则可以使用以下命令运行生成的可执行文件：
```shell

./<项目名称>
```

* 其中 <项目名称> 是您的项目的根目录的名称。



#### beego框架使用bee交叉编译linux执行文件命令
```shell
bee pack -be GOOS=linux -be GOARCH=amd64
```

