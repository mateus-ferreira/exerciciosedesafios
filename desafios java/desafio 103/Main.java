import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    String palavra = "Mateus";
    String inverso = "";

    for(int i = palavra.length()-1; i>=0; i--){
      inverso += palavra.charAt(i);
    }

    System.out.println(inverso);
  }
}