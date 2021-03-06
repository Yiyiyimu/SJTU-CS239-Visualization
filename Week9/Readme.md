## 作业报告

yiyiyimu

1. 数据描述和分析

   这次作业的数据量较之前并不算大，但难度主要在数据清洗，需要通过与省市经纬度比较，从文字格式的履历整理为“时间-地点-坐标”格式的数据，以便于可视化。

   为了达到上述目的，使用中文NLP常用的结巴分词提取履历中所有可能的文字段，借助省市经纬度数据中的地名数据，清洗出“时间-地点”的数据。为了尽可能完整的保留信息，额外采用的trick包括：

   * ‘中央’视为‘北京’
   * 如果地名包含‘’省‘‘市’‘县’’区‘等后缀词，去掉后缀词的版本也加入经纬度数据中的地名
   * 以坐标为参考对象，如果调任的同时地名坐标不变，则不视为调任（减少冗余箭头，这种情况常出现在从省会单位调任到省级单位）
   * 对于每个人，保证时间升序（数据中经常会出现’其间‘影响时间轴判断）

   尽管使用多种方法，但还是会存在信息提取不完整的情况，如军队位置无法通过地名判断等等，但已尽量获取足够多的信息

2. 设计宗旨

   关注点：

   ​	如何更好的利用地图体现出人物的调任履历过程

   没有完成的：

   ​	如何体现人与人之间可能的关系（在同一时间段在一个省/一个市工作），并由此评价人与人之间的关系

3. 结果描述

   3.1. 作品描述

   ​	起初的想法是做成各人履历随着时间轴变化，但同时显示200人会使屏幕显得很乱，只显示一人又会比较慢。最后就做成了用箭头表示人物轨迹，显示时间和文字说明人物是如何移动的。选择人名用了按钮而不是下拉菜单，因为两百个人下拉菜单反而不容易找得到。

   ​	在个人履历基础上，需要探寻多人之间的关系。原本打算是借助出生地将众人归类，通过热图显示出生在每个省中央委员多少，单击某个省，会显示这个省所有人的轨迹。但最后时间有限没有做到，但参考美国大选的数据分析影响，额外做了一个显示出生在每个省中央委员占该省总人口比例的热图。因为热图不能看清楚最高和最低，因此最后补充了一个上两个热图对应的柱形图。

   3.2. 作品发现

   	* 可以说除去军官以外，绝大多数人都是在多个省之间调任，很少有在一个省一直做高再调到中央的情况，也就是图上会有多条大跨度的直线。
	
   	*  总的来说沿海城市所出的中央委员更多，尤其是山东省达到惊人的31名；但每亿人出的中央委员最多的则是西藏，相对西部也偏多一些，但同时也有包括青海在内的三个省没有中央委员。

   3.3. 收获

   ​	最大的收获应该是不要提前优化。。虽然这应该是写代码的通识了还是前期有大量时间花在了细枝末节的数据清洗和css上，想着做好这一步再做下一步，但最后时间就不够用了。

   ​	其次是现在逐渐有了概念，怎么把一个完整的设想出来的模型拆成一步一步去完成 ，先做出大致框架，再往里填东西。

   ​	最后是对d3更熟练了，这一次明显比前两三次写d3要顺手很多。