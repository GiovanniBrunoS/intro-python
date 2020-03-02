
public class Desafio104 {

	public static void main(String[] args) {
		
		int x = 2;
		int y = 5;
	
		System.out.println("X: " + x);
		System.out.println("Y: " + y);
		
		int temp = x;
		x = y;
		y = temp;
		
		System.out.println("X: " + x);
		System.out.println("Y: " + y);
		
		x = x + y;
		y = x - y;
		x = x - y;
	
		System.out.println("X: " + x);
		System.out.println("Y: " + y);

	}

}
