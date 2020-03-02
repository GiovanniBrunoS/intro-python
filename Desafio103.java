
public class Desafio103 {

	public static void main(String[] args) {
		
		String string = "Teste";
		
		char[] chars = string.toCharArray();

		for (int i = chars.length-1; i>=0; i--) 
			System.out.print(chars[i]); 
	}

}
