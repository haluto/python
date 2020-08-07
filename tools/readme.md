# Tools

### cutFile

将文件每行的前cutNum个字节删掉，生成新文件。[TODO: 可扩展成删每行的后cutNum个字节。]

```shell
$ cutFile.py <filename> <cutNum>
```

## Old (Before 2017)

- calcLogTime.py <log_file> <begin_tag> <end_tag>
  根据log文件中的开始/结束tag，计算执行时间。

- parseLiveLog.py
  demo，用subprocess执行logcat，按行获取并分析，实时输出需要的状态。