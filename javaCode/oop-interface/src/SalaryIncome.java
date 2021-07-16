
public class SalaryIncome implements Income{
	
	private double income;
		
    public SalaryIncome(double income) {
		this.income = income;
	}

	@Override
    public double getTax() {
        if (income <= 5000) {
            return 0;
        }
        return (income - 5000) * 0.2;
    }
}
