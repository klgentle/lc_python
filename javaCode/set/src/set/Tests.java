import java.util.*;

public class Tests{

    public static void main(String[] args){
      List<String>list = new ArrayList<String>();
      list.add("保护环境");  //向列表中添加数据
      list.add("爱护地球");  //向列表中添加数据
      list.add("从我做起");  //向列表中添加数据
      list.add("从我做起");  //向列表中添加数据
      boolean ret = list.remove("从我做起");  //移除指定元素
      if(ret){
        System.out.println("元素被移除成功");
      }else{
        System.out.println("列表中不包含此元素");
      }
      for (String l: list) {
        System.out.println(l);
      }
    }
}
