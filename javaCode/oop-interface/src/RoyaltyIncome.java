
/**
 * 稿费收入税率是20%
 */
public class RoyaltyIncome implements Income {
	
	private double income;
		
    public RoyaltyIncome(double income) {
		this.income = income;
	}

	@Override
    public double getTax() {
        return 0;
    }

}
