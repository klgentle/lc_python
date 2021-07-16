
public class SalaryIncome extends Income {

    public SalaryIncome(double income) {
		super(income);
		// TODO Auto-generated constructor stub
	}

	@Override
    public double getTax() {
        if (income <= 5000) {
            return 0;
        }
        return (income - 5000) * 0.2;
    }

}
