
/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng
 */
public class Main {

	public static void main(String[] args) {
		// TODO: 用接口给一个有工资收入和稿费收入的小伙伴算税:
		Income[] incomes = new Income[] {new SalaryIncome(7500), new RoyaltyIncome(12000) };
		double total = 0;
		for (Income in : incomes)
		{
			total = total + in.getTax();
		}
		System.out.println(total);
	}

}
