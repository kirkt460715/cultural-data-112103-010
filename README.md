# 文创系列组合对库存与销售结构的影响

用于比较虚构文创系列分类、可售时间与销售记录，不预设消费者偏好结论。

`fixtures/records.json` 保存合成演练记录，字段说明见 `docs/数据格式.md`。

需要 Python 3.9 或更新版本，无第三方依赖。运行资料基线检查：

```sh
python3 -m unittest discover -s tests -v
```
项目目前只提供资料读取和结构检查。
