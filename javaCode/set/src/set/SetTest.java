package set;

import java.util.*;

public class SetTest {

	public static void main(String[] args) {
		List<Message> received = List.of(new Message(1, "Hello!"), new Message(2, "发工资了吗？"), new Message(2, "发工资了吗？"),
				new Message(3, "去哪吃饭？"), new Message(3, "去哪吃饭？"), new Message(4, "Bye"));
		List<Message> displayMessages = process(received);
		for (Message message : displayMessages) {
			System.out.println(message.text);
		}
	}

	static List<Message> process(List<Message> received) {
		// TODO: 按sequence去除重复消息
		// Set<Message> messSet = new HashSet<>(received);
		Set<Message> messSet = new TreeSet<>(received);
		return new ArrayList<Message>(messSet);
	}
}

class Message implements java.lang.Comparable {
	public final int sequence;
	public final String text;

	public Message(int sequence, String text) {
		this.sequence = sequence;
		this.text = text;
	}

	@Override
	public int compareTo(Object o) { // 实现 Comparable 接口的抽象方法，定义排序规则
		Message p = (Message) o;
		return this.sequence - p.sequence; // 升序排列
	}

//    @Override
//    public boolean equals(Object o) {
//    	if (o instanceof Message) {
//    		Message m = (Message) o;
//    		return this.sequence == m.sequence && Objects.equals(this.text, m.text); 
//    	}
//    	return false;
//    } 
//    @Override
//    public int hashCode() {
//    	int n = 0;
//    	n = 31 * n + this.sequence;
//    	n = 31 * n + this.text.hashCode();
//    	return n;
//    }
}