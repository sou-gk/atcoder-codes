import java.util.*;

class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
		long m = sc.nextLong();
		long scc = 0;
		if(n >= m) scc = m / 2;
		else{
			scc += n + (m - 2 * n) / 4;
		}
		System.out.println(scc);
  }
}
