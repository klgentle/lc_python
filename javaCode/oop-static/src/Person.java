
public class Person {

	private int count;

	String name;

	public Person(String name) {
		this.name = name;
		this.count = count + 1;
	}
	
	public int getCount() {
		return this.count;
	}

}
