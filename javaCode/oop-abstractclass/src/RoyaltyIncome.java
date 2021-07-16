
/**
 * 稿费收入税率是20%
 */
public class RoyaltyIncome extends Income {

    public RoyaltyIncome(double income) {
		super(income);
		// TODO Auto-generated constructor stub
	}

	@Override
    public double getTax() {
        return 0;
    }

}
