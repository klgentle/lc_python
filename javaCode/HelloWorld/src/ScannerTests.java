import java.util.Scanner;
public class ScannerTests {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // ����Scanner����
        System.out.print("Input your name: "); // ��ӡ��ʾ
        String name = scanner.nextLine(); // ��ȡһ�����벢��ȡ�ַ���
        System.out.print("Input your age: "); // ��ӡ��ʾ
        int age = scanner.nextInt(); // ��ȡһ�����벢��ȡ����
        System.out.printf("Hi, %s, you are %d.\n", name, age); // ��ʽ�����
    }
	
}
