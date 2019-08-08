# OWhat数据爬虫
爬取部分Owhat数据的样例，包括集资排行榜和销售情况

## 函数和返回值
getOwhatRankingList用途是抓取集资排行  
返回一个list，类型是自定义的一个类，有四个元素，分别是：  
  nickname：昵称  
  userid：用户ID  
  number：排名  
  amount：总金额  
  
getOwhatSales用途是抓取销售情况  
返回一个list，类型是自定义的一个类，有四个元素，分别是：  
  name：商品名称  
  price：价格  
  salestock：已销售  
  remainstock：库存  
