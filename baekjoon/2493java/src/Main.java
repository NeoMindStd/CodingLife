import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int[] towers = new int[n];
		for(int i=0; i<n; i++) {
			towers[i] = s.nextInt();
		}
		
		for(int i=0; i<n; i++) {
			int dst = 0;
			for(int j=i-1; j>-1; j--) {
				if(towers[i] <= towers[j]) {
					dst = j + 1;
					break;
				}
			}
			System.out.print(dst + " ");
		}
	}
}
