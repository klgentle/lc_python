
/**
 * 定义抽象类Income
 */
public abstract class Income {

	protected double income;
	public abstract double getTax();
	
	public Income(double income) {
		this.income = income;
	}
}
