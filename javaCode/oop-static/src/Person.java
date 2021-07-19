
public class Person {

	private static int count;

	String name;

	public Person(String name) {
		this.name = name;
		count = count + 1;
	}
	
	public static int getCount() {
		return count;
	}

}
