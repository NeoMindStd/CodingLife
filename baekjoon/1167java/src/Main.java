import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		//Node tree = new Node(0);
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int v = Integer.parseInt(br.readLine());
		
		System.out.println(v);
		
		br.close();
	}
}

class Node {
	int no;
	ArrayList<Data> children;
	
	public Node(int no) {
		this.no = no;
	}
}

class Data {
	int d;
	Node child;
	
	Data(int d, Node child) {
		this.d = d;
		this.child = child;
	}
}