import java.util.List;


public class ListForEach {
    public static void main(String[] args) {
       List<Integer> l = List.of(1,2,3,4,5);
       l.forEach(System.out::println);
    }
    
}
