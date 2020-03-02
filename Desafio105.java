import java.util.ArrayList;
import java.util.stream.*;;


public class Desafio105 {	

	public static void main(String[] args) {
		
		// Não é possível fazer o desafio 1 sem utilizar loops

		ArrayList<Integer> lista = new ArrayList<>();
		
		IntStream.range(0, 1000).forEach(
				n -> {
					if(n%2==0)
						lista.add(n);
				}
			);
		
		System.out.println(lista);
		
		// Não é possível fazer o desafio 2 pois o range é muito grande(99999999999999999999999999)
	
		IntStream.range(0, 999999999).forEach(
				n -> {
					if(n%5==0 && n != 0) {
						System.out.println(n);
						System.exit(0);
					}
				}
			);
		
	}

}
